# Generated by Django 3.2.4 on 2021-07-18 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0003_auto_20210717_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='comentario',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]