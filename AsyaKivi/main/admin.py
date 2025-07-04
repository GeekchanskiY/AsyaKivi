from django.contrib import admin

from main.models import Color, Item, ColorRequirement, ItemImage


# Register your models here.
@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    pass

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass

@admin.register(ColorRequirement)
class ColorRequirementAdmin(admin.ModelAdmin):
    pass

@admin.register(ItemImage)
class ItemImageAdmin(admin.ModelAdmin):
    pass