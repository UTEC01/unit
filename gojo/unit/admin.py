from django.contrib import admin
from import_export.resources import ModelResource
from import_export.admin import ImportMixin
from import_export.formats import base_formats
from import_export.fields import Field
from .models import Post
# Register your models here.

class UnitResource(ModelResource):
    p_no = Field(attribute='p_no', column_name='制作番号')
    o_no = Field(attribute='o_no', column_name='手配番号')
    c_name = Field(attribute='c_name', column_name='製品名')
    #c_date = Field(attribute='c_date', column_name='ユニット納期')
    text = Field(attribute='text', column_name='備考')
    #購入納期 = Field(attribute='購入納期', column_name='購入納期ｔ')
    class Meta:
        model=Post
        import_order = ('p_no', 'o_no', 'c_name', 'c_date', 'text', '購入納期')
        import_id_fields = ['p_no']

class UnitAdmin(ImportMixin, admin.ModelAdmin):
    list_display = ('p_no', 'o_no', 'c_name', 'c_date', 'text', '購入納期')
    resource_class = UnitResource
    formats = [base_formats.CSV]

#admin.site.register(Post)
admin.site.register(Post,UnitAdmin)
