# Generated by Django 2.1.5 on 2019-02-03 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20190203_2314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='portfolio',
            name='published_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
