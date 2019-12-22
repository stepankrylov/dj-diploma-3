from django.contrib import admin
from app.models import Phones, Review, Cart


class PhonesAdmin(admin.ModelAdmin):
    ordering = ('id', 'name', 'price',)
    list_display = ('id', 'name', 'image', 'price', 'description', 'slug',)
    list_filter = ('name', 'price',)
    search_fields = ('id', 'name', 'price',)


admin.site.register(Phones, PhonesAdmin)




