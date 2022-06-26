from django.contrib import admin
from django.urls import path, include, re_path
from basic_app import views

# SET THE NAMESPACE!
app_name = 'basic_app'


urlpatterns=[
    re_path(r'^register/$',views.register,name='register'),
    re_path(r'^user_login/$',views.user_login,name='user_login'),
#    re_path(r'^platforms/$',views.list_platforms,name='list_platforms'),
    re_path(r'^platforms/$',views.PlatformsListView.as_view(),name='list_platforms'),
#    path('platforms/<str:plat_slug>/',views.show_platform,name='show_platform'),
    path('platforms/<str:plat_slug>/',views.PlatformShowView.as_view(),name='show_platform'),
#    path('platforms/<str:plat_slug>/products/',views.list_products,name='list_products'),
    path('platforms/<str:plat_slug>/products/',views.ProductsListView.as_view(),name='list_products'),
    #path('platforms/<str:plat_slug>/products/<str:prod_slug>/',views.show_product,name='show_product'),
    path('platforms/<str:plat_slug>/products/<str:prod_slug>/',views.ProductShowView.as_view(),name='show_product'),
    #path('platforms/<str:plat_slug>/products/<str:prod_slug>/create_query',views.create_query,name='create_query'),
    # a linha seguinte fica em cada uma das applicaoes S1
    path('platforms/<str:plat_slug>/products/<str:prod_slug>/create_query',views.CreateQueryView.as_view(),name='create_query'),
    path('platforms/<str:plat_slug>/products/<str:prod_slug>/query_results',views.ola,name='query_results'),
    #importr S1.urls
]
