from django.contrib import admin
from .models import Category, Actor, Genre, Movie, MovieShots, Rating, RatingStar, Reviews


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')
    list_display_links = ('id', 'name')


class ReviewInline(admin.TabularInline):
    model = Reviews
    extra = 1
    readonly_fields = ('name', 'email')


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'Category', 'url', 'draft')
    list_filter = ('Category', 'year')
    search_fields = ('title', 'Category__name',)
    inlines = [ReviewInline]
    save_on_top = True
    save_as = True
    list_editable = ('draft', )
    fields = (("actors", "directors", "genres"), )


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'parent', 'movie', 'id')
    readonly_fields = ('name', 'email')


admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(MovieShots)
admin.site.register(Rating)
admin.site.register(RatingStar)





