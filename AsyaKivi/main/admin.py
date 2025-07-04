from django.contrib import admin

from main.models import Item, ItemImage, Category, Collection, ItemCollection


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass


@admin.register(ItemImage)
class ItemImageAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    pass


@admin.register(ItemCollection)
class ItemCollectionAdmin(admin.ModelAdmin):
    pass