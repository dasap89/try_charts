from django.contrib import admin

# Register your models here.
from charts.models import DataModel

class DataModelAdmin(admin.ModelAdmin):
    # fields = ('region', 'country', 'value')
    fields = ('region', 'country', 'value')

# admin.site.register(DataModel)
admin.site.register(DataModel, DataModelAdmin)
