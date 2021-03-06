# Generated by Django 4.0.4 on 2022-05-10 08:13

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('main_movie_image', models.ImageField(blank=True, null=True, upload_to='main_movie_image')),
                ('year_of_issue', models.DateField()),
                ('genre', models.CharField(choices=[('Драма/мелодрама', 'Драма/мелодрама'), ('Комедия', 'Комедия'), ('Фантастика', 'Фантастика'), ('Боевики', 'Боевики'), ('Ужасы', 'Ужасы'), ('Мультфильмы', 'Мультфильмы'), ('Аниме', 'Аниме'), ('Триллер', 'Триллер'), ('Детектив', 'Детектив'), ('Исторические', 'Исторические'), ('Документальные', 'Документальные'), ('Криминал', 'Криминал')], default='Боевики', max_length=250)),
                ('rating', models.IntegerField()),
                ('description', models.TextField()),
                ('slug', models.SlugField()),
                ('movie_trailer', models.FileField(null=True, upload_to='videos_uploaded', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_category', to='categories.category')),
            ],
            options={
                'verbose_name': 'Фильм',
                'verbose_name_plural': 'Фильмы',
            },
        ),
        migrations.CreateModel(
            name='RatingStar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.SmallIntegerField(default=0, verbose_name='Значение')),
            ],
            options={
                'verbose_name': 'Звезда рейтинга',
                'verbose_name_plural': 'Звезды рейтинга',
                'ordering': ['-value'],
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('text', models.TextField(max_length=5000, verbose_name='Сообщение')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_reviews', to='movies.movie', verbose_name='фильм')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='movies.reviews', verbose_name='Родитель')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=15, verbose_name='IP адрес')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_rating', to='movies.movie', verbose_name='фильм')),
                ('star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='star_rating', to='movies.ratingstar', verbose_name='звезда')),
            ],
            options={
                'verbose_name': 'Рейтинг',
                'verbose_name_plural': 'Рейтинги',
            },
        ),
        migrations.CreateModel(
            name='MovieImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_image', models.FileField(null=True, upload_to='videos_trailers', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])),
                ('movie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='movie_image', to='movies.movie')),
            ],
            options={
                'verbose_name': 'Картинка фильма',
                'verbose_name_plural': 'Картинки фильмов',
            },
        ),
        migrations.CreateModel(
            name='MovieComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_comment', to='movies.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_movie', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Коментарий',
                'verbose_name_plural': 'Коментарии',
            },
        ),
    ]
