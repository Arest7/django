# Generated by Django 3.0.7 on 2024-01-08 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20240109_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfile',
            name='file',
            field=models.FileField(upload_to='uploads/'),
        ),
    ]