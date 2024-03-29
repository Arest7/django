# Generated by Django 3.0.7 on 2024-01-08 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=550, verbose_name='Title')),
                ('abstract', models.CharField(max_length=5550, verbose_name='Abstract')),
                ('owner', models.CharField(max_length=250, verbose_name='Owner')),
                ('date', models.DateTimeField(verbose_name='Published')),
            ],
        ),
    ]
