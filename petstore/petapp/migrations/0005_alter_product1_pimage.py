# Generated by Django 5.0 on 2024-01-01 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petapp', '0004_product1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product1',
            name='pimage',
            field=models.ImageField(upload_to='images/image/'),
        ),
    ]
