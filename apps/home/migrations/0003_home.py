# Generated by Django 4.0.4 on 2022-05-03 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_about_setting_delete_home'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=130)),
            ],
            options={
                'verbose_name': 'Главная страница',
            },
        ),
    ]
