from django.contrib import admin
from craft_manager_app.models import *

admin.site.site_header = "Menadżer Craftów"
admin.site.site_title = "Menadżer Craftów"


@admin.register(LabStation)
class AbilityAdmin(admin.ModelAdmin):
    model = LabStation

    list_display = ("name",)
