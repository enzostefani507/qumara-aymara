# Generated by Django 3.2.4 on 2021-07-28 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0003_auto_20210728_0013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='is_staff',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]