# Generated by Django 3.2.4 on 2021-07-18 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_alter_opinion_fecha_creacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opinion',
            name='fecha_creacion',
            field=models.CharField(default='18/07/2021', max_length=50),
        ),
    ]
