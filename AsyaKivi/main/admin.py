from django.contrib import admin

from main.models import Item, ItemImage, Category, Collection, ItemCollection, CollectionImage, Session, CartItem


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'amount', 'price', 'category')


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

@admin.register(CollectionImage)
class CollectionImageAdmin(admin.ModelAdmin):
    pass

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    pass

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    pass