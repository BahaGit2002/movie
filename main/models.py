from django.db import models
from datetime import date
from django.urls import reverse


class Category(models.Model):
    '''Категория'''
    name = models.CharField('Категория', max_length=150)
    discriptions = models.TextField('Описание')
    url = models.SlugField(max_length=360)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Actor(models.Model):
    '''Актеры и режиссеры'''
    name = models.CharField('Имя', max_length=100)
    age = models.PositiveSmallIntegerField('Возраст', default=0)
    discriptions = models.TextField('Описание')
    image = models.ImageField('Изоброжение', upload_to='actors/')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('actor_detail', kwargs={'slug': self.name})

    class Meta:
        verbose_name = 'Актер и режиссер'
        verbose_name_plural = 'Актеры и режиссеры'


class Genre(models.Model):
    '''Жанры'''
    name = models.CharField('Имя', max_length=100)
    discriptions = models.TextField('Описание')
    url = models.SlugField(max_length=360, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Movie(models.Model):
    '''Фильмы'''
    title = models.CharField('Названия', max_length=100)
    tagline = models.CharField('Слоган', max_length=100, default='')
    discriptions = models.TextField('Описание')
    poster = models.ImageField('Постер', upload_to='movies/')
    year = models.PositiveSmallIntegerField('Дата выхода', default=2022)
    country = models.CharField('Страна', max_length=30)

    directors = models.ManyToManyField(Actor, verbose_name='Режиссер', related_name='film_director', blank=True)
    actors = models.ManyToManyField(Actor, verbose_name='Актеры', related_name='film_actor', blank=True)
    genres = models.ManyToManyField(Genre, verbose_name='Жанры', blank=True)

    world_premiere = models.DateField('Примьера в мире', default=date.today)
    budget = models.PositiveIntegerField('Бюджет', default=0, help_text='Указать сумму в долларах')
    fees_in_world = models.PositiveIntegerField('Сборы в мире', default=0, help_text='Указать сумму в долларах')
    fees_in_usa = models.PositiveIntegerField('Сборы в США', default=0, help_text='Указать сумму в долларах')
    Category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=130, unique=True)
    draft = models.BooleanField('Черновик', default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movie_detail', kwargs={'slug': self.url})

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


class MovieShots(models.Model):
    '''Кадры из фильма'''
    title = models.CharField('Заголовок', max_length=100)
    discriptions = models.TextField('Описание')
    image = models.ImageField('Изоброжения', upload_to='movie_shots/')
    movie = models.ForeignKey(Movie, verbose_name='Фильм', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Кадр из фильма'
        verbose_name_plural = 'Кадры из фильма'


class RatingStar(models.Model):
    '''Звезда рейтинга'''
    value = models.PositiveSmallIntegerField('Значение', default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Звезда рейтинга'
        verbose_name_plural = 'Звезда рейтинга'


class Rating(models.Model):
    '''Рейтинг'''
    ip = models.CharField('', max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name='звезда')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name='фильм')

    def __str__(self):
        return f'{self.star} = {self.movie}'

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'


class Reviews(models.Model):
    '''Отзыв'''
    email = models.EmailField()
    name = models.CharField('Имя', max_length=100)
    text = models.TextField('Сообщение', max_length=5000)
    parent = models.ForeignKey('self', verbose_name='Родитель', on_delete=models.SET_NULL, blank=True, null=True, related_name='children')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name='фильм', related_name='reviews')

    def __str__(self):
        return f'{self.name} = {self.movie}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

