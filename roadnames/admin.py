from django.contrib import admin

from roadnames.models import RoadName


@admin.register(RoadName)
class RoadNameAdmin(admin.ModelAdmin):
    pass
