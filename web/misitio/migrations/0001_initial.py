# Generated by Django 4.1.1 on 2022-10-31 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('dni', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=150, null=True)),
                ('alta', models.DateTimeField(null=True, verbose_name='Fecha Alta')),
                ('direccion', models.CharField(max_length=150, null=True)),
                ('movil', models.CharField(max_length=14, null=True)),
            ],
        ),
    ]