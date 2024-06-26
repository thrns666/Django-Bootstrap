from django.contrib import admin
from .models import *


class MainsiteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'availability', 'cat')
    list_display_links = ('title',)
    search_fields = ('title', 'description')
    list_editable = ('availability', 'price')
    list_filter = ('cat', 'price', 'availability')
    prepopulated_fields = {'slug': ('title',)}


class LastCategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class SubCategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'main_cat', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class MainCategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, MainsiteAdmin)
admin.site.register(LastCategories, LastCategoriesAdmin)
admin.site.register(SubCategories, SubCategoriesAdmin)
admin.site.register(MainCategories, MainCategoriesAdmin)


