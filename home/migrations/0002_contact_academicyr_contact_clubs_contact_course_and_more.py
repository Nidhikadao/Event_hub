# Generated by Django 5.1.1 on 2024-09-06 20:11

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='academicyr',
            field=models.CharField(choices=[('1', '1st year'), ('2', '2nd year'), ('3', '3rd year'), ('4', '4th year')], default='1', max_length=20),
        ),
        migrations.AddField(
            model_name='contact',
            name='clubs',
            field=models.CharField(choices=[('1', 'Technology'), ('2', 'Creativity'), ('3', 'Sports'), ('4', 'Cultural'), ('5', 'Reasearch')], default='1', max_length=20),
        ),
        migrations.AddField(
            model_name='contact',
            name='course',
            field=models.CharField(choices=[('1', 'Btech'), ('2', 'Polytech'), ('3', 'BCA'), ('4', 'BSC'), ('5', 'BBA')], default='1', max_length=20),
        ),
        migrations.AddField(
            model_name='contact',
            name='timeStamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
