# Generated by Django 3.2 on 2021-09-11 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_user_user_page_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='desc',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='skills',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
