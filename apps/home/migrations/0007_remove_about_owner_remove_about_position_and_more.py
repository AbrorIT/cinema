# Generated by Django 4.0.4 on 2022-05-07 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_about_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='about',
            name='position',
        ),
        migrations.AlterField(
            model_name='about',
            name='image_about',
            field=models.ImageField(upload_to='about/'),
        ),
    ]
