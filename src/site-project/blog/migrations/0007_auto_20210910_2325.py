# Generated by Django 3.2 on 2021-09-10 18:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_category_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='is_admin',
        ),
        migrations.AddField(
            model_name='comment',
            name='admin',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
