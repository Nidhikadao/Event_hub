# Generated by Django 5.1.1 on 2024-09-24 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('org', '0007_alter_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
