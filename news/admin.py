from django.contrib import admin

from news.models import Topic, Newspaper


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    pass


@admin.register(Newspaper)
class NewspaperAdmin(admin.ModelAdmin):
    pass
