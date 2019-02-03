from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta: #이 폼을 만들기 위해 필요한 모델정의
        model = Post
        fields = ('author','title', 'text')