from django.contrib import admin
from .models import ThingType, Thing


@admin.register(ThingType)
class ThingTypeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'created_at',
        'edited_at',
    )

    search_fields = (
        'title',
    )


@admin.register(Thing)
class ThingAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'type',
        'created_at',
        'edited_at',
    )

    list_filters = (
        'type',
    )

    autocomplete_fields = (
        'type',
    )
