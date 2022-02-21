# Generated by Django 3.2.12 on 2022-02-18 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='content',
        ),
        migrations.AddField(
            model_name='page',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
