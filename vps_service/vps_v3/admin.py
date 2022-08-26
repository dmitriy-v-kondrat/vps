from django.contrib import admin

# Register your models here.
from vps_v3.models import CPU, RAM, HDD


class CPUAdmin(admin.ModelAdmin):
    model = CPU


class RAMAdmin(admin.ModelAdmin):
    model = RAM


class HDDAdmin(admin.ModelAdmin):
    model = HDD


admin.site.register(CPU, CPUAdmin)
admin.site.register(RAM, RAMAdmin)
admin.site.register(HDD, HDDAdmin)
