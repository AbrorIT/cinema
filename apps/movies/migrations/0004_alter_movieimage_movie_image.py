# Generated by Django 4.0.4 on 2022-05-10 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_alter_movie_movie_trailer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movieimage',
            name='movie_image',
            field=models.FileField(null=True, upload_to='videos_trailers'),
        ),
    ]