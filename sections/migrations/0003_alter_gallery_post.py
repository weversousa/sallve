# Generated by Django 3.2.12 on 2022-02-16 21:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0002_post_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery', to='sections.post'),
        ),
    ]