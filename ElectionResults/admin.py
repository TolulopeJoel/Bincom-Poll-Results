from django.contrib import admin

from .models import *

# Inlines
class WardInline(admin.TabularInline):
    model = Ward
    extra = 0


class PollingUnitInline(admin.TabularInline):
    model = PollingUnit
    extra = 0


class AnnouncedPollingUnitResultInline(admin.TabularInline):
    model = AnnouncedPollingUnitResult
    extra = 0


# Model Admins
class WardAdmin(admin.ModelAdmin):
    list_display = ['name', 'lga']
    

class MainWardAdmin(admin.ModelAdmin):
    inlines = [WardInline]


class PollingUnitAdmin(admin.ModelAdmin):
    list_display = ['name', 'number', 'ward', 'lga']
    list_filter = ['lga']
    inlines = [AnnouncedPollingUnitResultInline]


class LGAAdmin(admin.ModelAdmin):
    list_display = ['name', 'state']
    inlines = [PollingUnitInline]


class MainPollingUnitAdmin(admin.ModelAdmin):
    inlines = [PollingUnitInline]


class AnnouncedPollingUnitResultAdmin(admin.ModelAdmin):
    list_display = ['polling_unit', 'party', 'party_score']
    list_filter = ['party']


admin.site.register(State)
admin.site.register(Party)
admin.site.register(Lga, LGAAdmin)
admin.site.register(Ward, WardAdmin)
admin.site.register(PollingUnit, PollingUnitAdmin)
admin.site.register(AnnouncedPollingUnitResult, AnnouncedPollingUnitResultAdmin)
