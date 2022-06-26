from django.shortcuts import render
from basic_app.forms import UserForm
#from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from basic_app.models import Platform, Product

from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django_tables2 import Table, TemplateColumn
from django_tables2.views import SingleTableView

from django.shortcuts import redirect
from django.apps import apps

from django.conf import settings

from basic_app.forms import S1QueryForm, S2QueryForm, S5PQueryForm
import S_1.models 
import S_2.models 
import S_5P.models 
from basic_app.code import APIfunc


# Create your views here.
def index(request):

    return render(request,'basic_app/index.html')

@login_required
def special(request):
    return HttpResponse('YOU R IN')

@login_required
def user_logout(request):
    logout(request)
    return render(request,'basic_app/index.html')
def register(request):
    registerd=False

    if request.method=='POST':
        user_form=UserForm(data=request.POST)

        if user_form.is_valid():
            user=user_form.save()

            user.set_password(user.password)
            user.save()

            registerd=True

        else:
            print(user_form.errors)
    else:
        user_form=UserForm()

    return render(request,'basic_app/registration.html',{'user_form':user_form,'registerd':registerd})

def user_login(request):

    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return render(request,'basic_app/index.html')
            else:
                return HttpResponse('account not active')
        else:
            print ('someone failed login')
            print ('username: {} and password{}'.format(username,password))

            return HttpResponse('invalid login')
    else:
        return render(request,'basic_app/login.html',{})

      
'''
@login_required
def list_platforms(request):
    platform_list = Platform.objects.order_by("name")
    platform_dict = {"platforms": platform_list}
    return render(request, "basic_app/platforms.html", platform_dict)
'''

class PlatformsListView(LoginRequiredMixin,TemplateView):
    template_name = 'basic_app/platforms.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        platform_list = Platform.objects.order_by("name")
        context['platforms'] = platform_list
        
        return context
'''
@login_required
def show_platform(request, plat_slug):
    platform_list = Platform.objects.get(slug=plat_slug)
    platform_dict = {"platform": platform_list}
    return render(request, "basic_app/show_platform.html", platform_dict)
'''

class PlatformShowView(LoginRequiredMixin,TemplateView):
    template_name = 'basic_app/show_platform.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        plat_slug = kwargs['plat_slug'] 
        platform = Platform.objects.get(slug=plat_slug)
        
        context['platform'] = platform
        
        return context

'''
@login_required
def list_products(request, plat_slug):
    product_l = Product.objects.filter(platform=plat_slug)
    product_list = list(product_l)
    product_dict = {"products": product_list}
    return render(request, "basic_app/products.html", product_dict)
'''

class ProductsTable(Table):
    action = TemplateColumn(template_name='basic_app/product_link.html')

    class Meta:
        model = Product
        fields = ['platform', 'name', 'slug']


class ProductsListView(LoginRequiredMixin,SingleTableView):
    template_name = 'basic_app/products.html'
    table_class = ProductsTable

    def get_queryset(self):
        return Product.objects.filter(platform=self.kwargs['plat_slug'])

'''  
@login_required
def show_product(request, plat_slug, prod_slug):
    prod_list = Product.objects.get(slug=prod_slug, platform=plat_slug)
    prod_dict = {"product": prod_list}
    return render(request, "basic_app/"+plat_slug+"/show_product.html", prod_dict)
    #return render(request, "basic_app/show_product.html", prod_dict)
'''
class ProductShowView(LoginRequiredMixin,TemplateView):
    def get_template_names(self):
        #template_name = '%s/templates/basic_app/show_product.html' % self.kwargs['plat_slug'] 
        template_name = 'basic_app/show_product.html'
        return [template_name]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        plat_slug = kwargs['plat_slug'] 
        prod_slug = kwargs['prod_slug']
        product = Product.objects.get(slug=prod_slug, platform=plat_slug)
        
        context['product'] = product
        
        return context

class CreateQueryView(CreateView):
    #model = S1_Query
    
    # 1 criar o modelo dentro da app chamada S1
    # 2 fazer o formulario dentro da app S1
    # 3 declarar nos setting um dionario  {"S1":S1.form, "S2":S2.form}
  
    
    #form_class = QueryForm
    #success_url = '/'
    def setup(self, *args, **kwargs):
        super().setup(*args,**kwargs)
        #self.model = apps.get_model('slug.Query') #substituir basic_app.query por slug.query
        model_name = self.kwargs['plat_slug'] +'.'+'Query' 
        self.model = apps.get_model(model_name)
        '''
        if self.kwargs['plat_slug'] == "S_1":
            self.model = apps.get_model('S_1.S1Query')
        elif self.kwargs['plat_slug'] == "S_2":
            self.model = apps.get_model('S_2.S2Query')
        elif self.kwargs['plat_slug'] == "S_5P":
            self.model = apps.get_model('S_5P.S5PQuery')
        '''

    def get_form_class(self):
        form_class = settings.KEY[self.kwargs['plat_slug']]
        #form_class = S1QueryForm
        return form_class # return a query form especifica para o slug
    def get_template_names(self):
        #template_name = 'basic_app/%s/create_query.html' % self.kwargs['plat_slug']
        template_name = 'basic_app/create_query.html'
        return [template_name]
    
    def dispatch(self, *args, **kwargs):
        return super(CreateQueryView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        prod = Product.objects.get(slug=self.kwargs['prod_slug'], platform=self.kwargs['plat_slug'])
        plat = Platform.objects.get(slug=self.kwargs['plat_slug'])
        obj.platform = plat.name
        obj.product = prod
        obj.save()        
        #return redirect('/')
       
'''
@login_required
def create_query(request, plat_slug, prod_slug):
    prod = Product.objects.get(slug=prod_slug, platform=plat_slug)
    if request.method=='POST':
        query_form= QueryForm(data=request.POST)
        
        if query_form.is_valid():
            
            query=query_form.save(commit=False)
            query.product = prod
            query.user = request.user
            query.save()
            
        else:
            print(query_form.errors)
    else:
        query_form= QueryForm()
        
    return render(request, "basic_app/"+plat_slug+"/create_query.html", {'query_form':query_form, 'product':prod})

'''
"""
from django_tables2 import Table, TemplateColumn, Column
from django_tables2.views import SingleTableView

class ExecutionsTable(Table):
    action = TemplateColumn(template_name='free/execution_link.html') a proxima linha e o template:
    <a href="{% url 'free:execution' record.pk %}"><button class='ui button'>Show</button></a>

    class Meta:
        model = Execution
        fields = ['apparatus', 'name', 'protocol', 'status', 'start', 'end']
"""
def ola(request,plat_slug,prod_slug):
    
    return render(request,'basic_app/query_results.html',{'products': APIfunc.products})