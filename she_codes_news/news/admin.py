from django.contrib import admin

from .models import NewsStory


# Register your models here.

class NewsAdmin(admin.ModelAdmin):

    list_display = ["author", "title", "view_birth_date"]

    @admin.display(empty_value="???")
    def view_birth_date(self, obj):
        return obj.pub_date


admin.site.register(NewsStory, NewsAdmin)
