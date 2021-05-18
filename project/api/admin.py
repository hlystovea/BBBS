from django import forms
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .fields import fields
from .models import Article, History, Movie, Place, Question, Tag, Video


class MixinAdmin(admin.ModelAdmin):
    empty_value_display = _('-пусто-')


@admin.register(Article)
class ArticleAdmin(MixinAdmin):
    list_display = ('id', 'title', 'color')
    search_fields = ('title', 'color')
    formfield_overrides = {
        fields.ColorField: {'widget': forms.TextInput(attrs={'type': 'color',
                            'style': 'height: 100px; width: 100px;'})}
    }


@admin.register(History)
class HistoryAdmin(MixinAdmin):
    list_display = ('id', 'title', 'image_url')
    search_fields = ('title', 'image_url')


@admin.register(Movie)
class MovieAdmin(MixinAdmin):
    list_display = ('id', 'title', 'image_url', 'link')
    search_fields = ('title',)
    list_filter = ('tags', )
    autocomplete_fields = ('tags', )


@admin.register(Question)
class QuestionAdmin(MixinAdmin):
    list_display = ('id', 'title', )
    search_fields = ('title', )
    list_filter = ('tags', )
    autocomplete_fields = ('tags', )


@admin.register(Place)
class PlaceAdmin(MixinAdmin):
    list_display = ('id', 'title', 'name', 'info', 'image_url', 'link')
    search_fields = ('title', 'name', 'info')


@admin.register(Tag)
class TagAdmin(MixinAdmin):
    list_display = ('id', 'name', 'slug')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Video)
class VideoAdmin(MixinAdmin):
    list_display = ('id', 'title', 'image_url', 'link', 'duration')
    search_fields = ('title',)
