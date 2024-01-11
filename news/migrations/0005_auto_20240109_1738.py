# Generated by Django 3.0.7 on 2024-01-09 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_uploadfile_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadfile',
            name='name',
        ),
        migrations.AddField(
            model_name='uploadfile',
            name='title',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='uploadfile',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]
