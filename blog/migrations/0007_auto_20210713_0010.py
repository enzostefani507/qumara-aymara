# Generated by Django 3.2.4 on 2021-07-13 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
        ('blog', '0006_auto_20210713_0006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='ingredientes',
        ),
        migrations.AddField(
            model_name='post',
            name='ingredientes',
            field=models.ManyToManyField(blank=True, null=True, to='catalogo.Producto'),
        ),
    ]
