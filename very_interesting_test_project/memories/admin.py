from django.contrib import admin

from .models import Memory


class MemoriesAdmin(admin.ModelAdmin):
    list_display = ('place_name', 'text', 'pub_date', 'author')
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


admin.site.register(Memory, MemoriesAdmin)
