# Generated by Django 4.1 on 2022-09-19 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0003_alter_movie_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='img',
            field=models.ImageField(upload_to='pictures'),
        ),
    ]
