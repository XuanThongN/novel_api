# Generated by Django 5.0.3 on 2024-03-30 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novel_api', '0002_novel_description_novel_image_path_novel_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='novel',
            name='image_path',
            field=models.ImageField(blank=True, upload_to='photos/'),
        ),
    ]
