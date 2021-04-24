from django import forms

from .models import Post
from .models import Minyuka

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('p_no','o_no', 'c_name', 'c_date', 'text', '購入納期', 'published_date', '出荷日')

class MinyukaForm(forms.ModelForm):

    class Meta:
        model = Minyuka
        fields = ('発注番号', '発注先', '納期', '個数', '読込日', '品名', 'mmm')
        