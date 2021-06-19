# Generated by Django 3.2.4 on 2021-06-18 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=500)),
                ('imagen', models.CharField(max_length=500)),
                ('en_stock_actual', models.BooleanField(default=False)),
            ],
        ),
    ]