# Generated by Django 5.0 on 2024-01-01 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petapp', '0005_alter_product1_pimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product1',
            name='pimage',
            field=models.ImageField(upload_to='images/image'),
        ),
    ]