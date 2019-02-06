from django.db import models
from django.utils import timezone

# Create your models here.
class Portfolio(models.Model):
    author = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    title = models.CharField(max_length=100, verbose_name='제목', help_text='포트폴리오 제목을 입력해 주세요. 최대 100자')
    image = models.ImageField(upload_to = 'images/')
    # 업로드된 이미지들을 images 폴더안에 넣으라
    category = models.CharField( max_length=10, default = True,
    choices = (
        ('자격증', '자격증'),
        ('교내활동', '교내활동'),
        ('교외활동', '교외활동'),
    ))
    description = models.CharField(max_length = 500)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(blank=True, null=True)
    #file upload!
    def publish(self):
        self.published_at = timezone.new()
        self.save

    def __str__(self):
        return self.title

    def summary(self):
        return self.description[:50]