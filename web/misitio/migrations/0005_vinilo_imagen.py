# Generated by Django 4.1.1 on 2022-11-30 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misitio', '0004_vinilo'),
    ]

    operations = [
        migrations.AddField(
            model_name='vinilo',
            name='imagen',
            field=models.ImageField(default='rbmkgb', upload_to=''),
            preserve_default=False,
        ),
    ]