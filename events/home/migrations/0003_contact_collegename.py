# Generated by Django 5.1.1 on 2024-09-07 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_contact_academicyr_contact_clubs_contact_course_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='collegename',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
