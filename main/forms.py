from django import forms #장고 기본 제공 기능
from .models import Post

class PostForm(forms.ModelForm): #모델 기반 폼

    class Meta: #이 폼을 만들기 위해 필요한 모델정의
        model = Post
        fields = ('title', 'text') #폼에서 어떤 항목을 입력 받을 것인지

