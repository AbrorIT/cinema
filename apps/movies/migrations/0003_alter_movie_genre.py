# Generated by Django 4.0.4 on 2022-05-01 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(choices=[('Драма/мелодрама', 'Драма/мелодрама'), ('Комедии', 'Комедии'), ('Фантастика', 'Фантастика'), ('Боевики', 'Боевики'), ('Мультфильмы', 'Мультфильмы'), ('Аниме', 'Аниме'), ('Ужасы', 'Ужасы'), ('Документальные', 'Документальные')], default='Боевики', max_length=250),
        ),
    ]
