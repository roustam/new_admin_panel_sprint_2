from django.contrib import admin

from .models import Filmwork, Genre, GenreFilmwork, Person, PersonFilmwork


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name", "description")


class GenreFilmworkInline(admin.TabularInline):
    model = GenreFilmwork
    autocomplete_fields = ("genre",)


class PersonFilmworkInline(admin.TabularInline):
    model = PersonFilmwork
    list_display = ("title", "type", "rating")
    autocomplete_fields = ("film_work",)


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    inlines = (PersonFilmworkInline,)
    list_display = ("full_name", "created")
    search_fields = ("full_name",)


@admin.register(Filmwork)
class FilmworkAdmin(admin.ModelAdmin):
    inlines = (GenreFilmworkInline,)
    list_prefetch_related = ("genres",)

    def get_queryset(self, request):
        queryset = (
            super().get_queryset(request).prefetch_related(*self.list_prefetch_related)
        )
        return queryset

    def get_genres(self, obj):
        return " ,".join([genre.name for genre in obj.genres.all()])

    get_genres.short_description = "Жанры фильма"

    # Отображение полей в списке
    list_display = ("title", "type", "creation_date", "rating", "get_genres")
    list_filter = ("type",)

    search_fields = (
        "title",
        "description",
        "id",
    )
