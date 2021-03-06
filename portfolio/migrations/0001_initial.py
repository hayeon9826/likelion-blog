# Generated by Django 2.1.5 on 2019-02-03 17:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='포트폴리오 제목을 입력해 주세요. 최대 100자', max_length=100, verbose_name='제목')),
                ('image', models.ImageField(upload_to='images/')),
                ('category', models.CharField(choices=[('제목1', '자격증'), ('제목2', '교내활동'), ('제목3', '교외활동')], default=True, max_length=10)),
                ('discription', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
