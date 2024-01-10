# Generated by Django 5.0 on 2024-01-01 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petapp', '0003_rename_contacts_contact1'),
    ]

    operations = [
        migrations.CreateModel(
            name='product1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=50)),
                ('pcategory', models.CharField(default='', max_length=50)),
                ('psubcategory', models.CharField(default='', max_length=50)),
                ('pprice', models.IntegerField(default=0)),
                ('pdesc', models.CharField(max_length=300)),
                ('pimage', models.ImageField(upload_to='images/image')),
            ],
        ),
    ]