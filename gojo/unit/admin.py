from django.contrib import admin
from import_export.resources import ModelResource
from import_export.admin import ImportMixin
from import_export.formats import base_formats
from import_export.fields import Field
from .models import Post
from .models import Minyuka
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
        import_order = ('p_no', 'o_no', 'c_name', 'c_date', 'text', 'published_date', '購入納期', '出荷日', '手配残')
        import_id_fields = ['p_no']
        skip_unchanged = False
        
class UnitAdmin(ImportMixin, admin.ModelAdmin):
    list_display = ('p_no', 'o_no', 'c_name', 'c_date', 'text', 'published_date', '購入納期', '出荷日', '手配残')
    resource_class = UnitResource
    formats = [base_formats.CSV]

class MinyukaResource(ModelResource):
    class Meta:
        model = Minyuka
        inport_order = ('発注番号', '発注先', '納期', '個数', '読込日', '品名', 'mmm', '備考', '入荷FLG')
        import_id_fields = ['mmm']
        skip_unchanged = False

class MinyukaAdmin(ImportMixin, admin.ModelAdmin):
    list_display = ('発注番号', '発注先', '納期', '個数', '読込日', '品名', 'mmm', '備考', '入荷FLG')
    resource_class = MinyukaResource
    formats = [base_formats.CSV]

admin.site.register(Post,UnitAdmin)
admin.site.register(Minyuka,MinyukaAdmin)
