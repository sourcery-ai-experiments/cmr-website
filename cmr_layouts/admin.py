from django.contrib import admin

from cmr_layouts.models import Customer, Location, Locomotive, RollingStock


@admin.register(Locomotive)
class LocomotiveAdmin(admin.ModelAdmin):
    list_display = (
        'modelName',
        'roadName',
        'roadNumber',
        'member',
        'dccID',
        'manufacturer',
        'scale',
        'status',
    )
    list_filter = ('roadName', 'member', 'manufacturer', 'scale', 'status')
    search_fields = (
        'modelName',
        'roadName',
        'roadNumber',
        'member',
        'dccID',
        'manufacturer',
        'scale',
        'status',
    )
    ordering = ('modelName', 'roadName', 'roadNumber')
    fieldsets = (
        (
            None,
            {
                'fields': (
                    'modelName',
                    'roadName',
                    'roadNumber',
                    'member',
                    'dccID',
                    'manufacturer',
                    'scale',
                    'image',
                    'status',
                    'description',
                )
            },
        ),
    )
    readonly_fields = ('id',)


@admin.register(RollingStock)
class RollingStockAdmin(admin.ModelAdmin):
    list_display = (
        'modelName',
        'roadName',
        'roadNumber',
        'member',
        'manufacturer',
        'scale',
        'status',
    )
    list_filter = ('roadName', 'member', 'manufacturer', 'scale', 'status')
    search_fields = (
        'modelName',
        'roadName',
        'roadNumber',
        'member',
        'manufacturer',
        'scale',
        'status',
    )
    ordering = ('modelName', 'roadName', 'roadNumber')
    fieldsets = (
        (
            None,
            {
                'fields': (
                    'modelName',
                    'roadName',
                    'roadNumber',
                    'member',
                    'manufacturer',
                    'scale',
                    'image',
                    'status',
                    'description',
                )
            },
        ),
    )
    readonly_fields = ('id',)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'shortName', 'scale')
    list_filter = ('scale',)
    search_fields = ('name', 'shortName')
    ordering = ('name',)
    fieldsets = ((None, {'fields': ('name', 'shortName', 'scale', 'description')}),)
    readonly_fields = ('id',)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'shortName', 'industry', 'location', 'scale', 'active')
    list_filter = ('industry', 'location', 'active', 'scale')
    search_fields = ('name', 'shortName', 'industry', 'location')
    ordering = ('name', 'industry')
    fieldsets = (
        (
            None,
            {'fields': ('name', 'shortName', 'industry', 'location', 'description')},
        ),
        (
            'Advanced options',
            {'classes': ('collapse',), 'fields': ('website', 'logo', 'active')},
        ),
    )
    readonly_fields = ('id',)
