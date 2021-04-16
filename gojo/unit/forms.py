from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('p_no','o_no', 'c_name', 'c_date', 'text', '購入納期', 'published_date', '出荷日')