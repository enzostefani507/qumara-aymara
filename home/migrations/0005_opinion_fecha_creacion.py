# Generated by Django 3.2.4 on 2021-06-20 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_opinion_fecha_creacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='opinion',
            name='fecha_creacion',
            field=models.CharField(default='20/06/2021', max_length=50),
        ),
    ]
