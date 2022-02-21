# Generated by Django 3.2.12 on 2022-02-18 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0003_alter_gallery_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='content',
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='created',
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='updated',
        ),
        migrations.AddField(
            model_name='gallery',
            name='image',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='gallery',
            name='post',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='gallery', to='sections.post'),
        ),
    ]
