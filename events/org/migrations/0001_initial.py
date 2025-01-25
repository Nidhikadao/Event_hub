# Generated by Django 5.1.1 on 2024-09-11 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=250)),
                ('College', models.CharField(max_length=250)),
                ('content', models.TextField()),
                ('venue', models.CharField(max_length=100)),
                ('connect', models.CharField(max_length=500)),
                ('timeStamp', models.DateTimeField(blank=True)),
                ('registerurl', models.URLField()),
                ('reachurl', models.URLField()),
            ],
        ),
    ]
