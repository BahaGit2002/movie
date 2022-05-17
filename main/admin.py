from django.contrib import admin
from .models import Category, Actor, Genre, Movie, MovieShots, Rating, RatingStar, Reviews
from django.utils.safestring import mark_safe
from .forms import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class MovieAdminForm(forms.ModelForm):
    discriptions = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

    class Meta:
        model = Movie
        fields = '__all__'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')
    list_display_links = ('id', 'name')


class ReviewInline(admin.TabularInline):
    model = Reviews
    extra = 1
    readonly_fields = ('name', 'email')


class MovieShotsInline(admin.TabularInline):
    model = MovieShots
    extra = 1
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="80"')

    get_image.short_description = "Изображение"


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'Category', 'url', 'draft')
    list_filter = ('Category', 'year')
    search_fields = ('title', 'Category__name',)
    inlines = [MovieShotsInline, ReviewInline]
    save_on_top = True
    save_as = True
    actions = ['publish', 'unpublish']
    form = MovieAdminForm
    list_editable = ('draft', )
    readonly_fields = ('get_image', )
    fieldsets = (
        (None, {
            "fields": (('title', 'tagline'), )
        }),
        (None, {
            "fields": ('discriptions', 'poster', 'get_image', )
        }),
        (None, {
            "fields": (('year', 'world_premiere', 'country'),)
        }),
        ('Actors', {
            'classes': ('collapse',),
            "fields": (('actors', 'genres', 'directors', 'Category'), )
        }),
        (None, {
            "fields": (('budget', 'fees_in_usa', 'fees_in_world'), )
        }),
        ('Options', {
            "fields": (('url', 'draft'),)
        }),
    )

    def get_image(self, obj):
        '''Снять с публикации'''
        return mark_safe(f'<img src={obj.poster.url} width="100" height="80"')

    def unpublish(self, request, queryset):
        row_update = queryset.update(draft=True)
        if row_update == 1:
            message_bit = '1 запис была обновлена'
        else:
            message_bit = f'{row_update} записей были обновлены'
        self.message_user(request, f'{message_bit}')

    def publish(self, request, queryset):
        '''Опубликовать'''
        row_update = queryset.update(draft=False)
        if row_update == 1:
            message_bit = '1 запис была обновлена'
        else:
            message_bit = f'{row_update} записей были обновлены'
        self.message_user(request, f'{message_bit}')

    publish.short_description = 'Опубликовать'
    publish.allowed_permissions = ('change', )

    unpublish.short_description = 'Снять с публикации'
    unpublish.allowed_permissions = ('change',)

    get_image.short_description = 'Постер'


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'parent', 'movie', 'id')
    readonly_fields = ('name', 'email')


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'get_image')
    readonly_fields = ('get_image', )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="80"')

    get_image.short_description = "Изображение"


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')


# admin.site.register(Rating)
@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('movie', 'ip')


@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    list_display = ('title', 'movie', 'get_image')
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="80"')

    get_image.short_description = "Изображение"


admin.site.register(RatingStar)

admin.site.site_title = "django Movies"
admin.site.site_header = "django Movies"



