# Generated by Django 3.2.4 on 2021-07-06 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_opinion_fecha_creacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opinion',
            name='fecha_creacion',
            field=models.CharField(default='06/07/2021', max_length=50),
        ),
    ]