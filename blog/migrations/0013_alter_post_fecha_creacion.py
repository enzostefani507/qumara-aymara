# Generated by Django 3.2.4 on 2021-07-17 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_alter_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='fecha_creacion',
            field=models.CharField(default='17/07/2021', max_length=50),
        ),
    ]
