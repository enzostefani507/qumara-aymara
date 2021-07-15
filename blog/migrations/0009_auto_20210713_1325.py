# Generated by Django 3.2.4 on 2021-07-13 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_post_ingredientes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('mensaje', models.CharField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='comentarios',
            field=models.ManyToManyField(to='blog.Comentario'),
        ),
    ]