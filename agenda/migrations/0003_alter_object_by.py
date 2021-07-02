# Generated by Django 3.2.5 on 2021-07-02 19:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('agenda', '0002_object_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='object',
            name='by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]