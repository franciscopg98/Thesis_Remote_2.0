from django.contrib import admin
from basic_app.models import Product, Platform,Query
import S_1.models
import S_2.models
import S_5P.models
from leaflet.admin import LeafletGeoAdmin, LeafletGeoAdminMixin


admin.site.register(Product)
admin.site.register(Platform)
#admin.site.register(Query, LeafletGeoAdmin)
admin.site.register(S_1.models.Query)
admin.site.register(Query,LeafletGeoAdmin)
admin.site.register(S_2.models.Query,LeafletGeoAdmin)
admin.site.register(S_5P.models.Query,LeafletGeoAdmin)