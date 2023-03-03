import uuid

from django.contrib import admin
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStampedMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UUIDMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class Genre(UUIDMixin, TimeStampedMixin):
    name = models.CharField(_("genre_name"), max_length=255, unique=True)
    description = models.TextField(_("genre_desc"), blank=True, default="Без описания")

    class Meta:
        db_table = 'content"."genre'
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    def __str__(self) -> str:
        return self.name


class Person(UUIDMixin):
    id = models.UUIDField(
        primary_key=True, editable=False, default=uuid.uuid4, db_column="id"
    )
    full_name = models.CharField(_("full_name"), max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'content"."person'
        verbose_name = "Персона"
        verbose_name_plural = "Персоны"

    def __str__(self) -> str:
        return self.full_name


class Filmwork(TimeStampedMixin):
    TYPES_OF_FILMWORK_CHOICES = [("movie", "movie"), ("tv_show", "tv_show")]
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, max_length=255
    )
    title = models.CharField(
        _("title"), null=False, max_length=255, default="Без названия"
    )
    genres = models.ManyToManyField(Genre, through="GenreFilmwork")
    persons = models.ManyToManyField(Person, through="PersonFilmwork")
    description = models.TextField(_("filmwork_desc"), max_length=2048)
    creation_date = models.DateField(
        _("creation_date"),
    )
    rating = models.FloatField(
        _("rating"),
        blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        default=0,
    )
    type = models.CharField(
        _("type"), choices=TYPES_OF_FILMWORK_CHOICES, max_length=128, default="movie"
    )

    class Meta:
        db_table = 'content"."film_work'

        verbose_name = "Кинопроизведение"
        verbose_name_plural = "Кинопроизведения"
        ordering = ["title"]


    def __str__(self) -> str:
        return self.title


class PersonFilmwork(UUIDMixin):
    class PersonRoles(models.TextChoices):
        ACTOR = "actor", _("Actor")
        DIRECTOR = "director", _("Director")
        WRITER = "writer", _("Writer")

    film_work = models.ForeignKey(
        Filmwork, related_name="film_work", on_delete=models.CASCADE
    )
    person = models.ForeignKey(
        Person, related_name="fw_person", on_delete=models.CASCADE
    )
    role = models.CharField(
        _("role"),
        choices=PersonRoles.choices,
        default=PersonRoles.ACTOR,
        max_length=35,
        null=True,
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'content"."person_film_work'
        verbose_name = "Роль в кинопроизведениях"
        verbose_name_plural = "Роли в кинопроизведениях"
        constraints = [
            models.UniqueConstraint(fields=["film_work", "person"], name="person_filmwork_idx")
        ]


class GenreFilmwork(UUIDMixin):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    film_work = models.ForeignKey(
        Filmwork, on_delete=models.CASCADE, to_field="id", db_column="film_work_id"
    )
    genre = models.ForeignKey(
        Genre,
        to_field="id",
        db_column="genre_id",
        related_name="genres",
        on_delete=models.CASCADE,
    )
    created = models.DateTimeField(_("created"), auto_now_add=True)

    class Meta:
        verbose_name = "Жанр фильма"
        verbose_name_plural = "Жанры фильма"
        db_table = 'content"."genre_film_work'
        constraints = [
            models.UniqueConstraint(
                fields=["film_work", "genre"], name="film_work_genre"
            )
        ]
        indexes = [
            models.Index(fields=["film_work", "genre"], name="film_work_genre_idx")
        ]
