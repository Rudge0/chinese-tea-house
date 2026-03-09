from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from catalog.models import Tea, Supplier, TeaCategory, Province


@admin.register(Tea)
class TeaAdmin(admin.ModelAdmin):
    list = ["name", "price", "harvest_year"]
    search_fields = ["name", ]
    list_display = list
    list_filter = list


@admin.register(Supplier)
class SupplierAdmin(UserAdmin):
    list_display = ["first_name", "last_name", "website", ]
    UserAdmin.fieldsets[1][1]["fields"] = ("first_name", "last_name", "email", "website")
    add_fieldsets = UserAdmin.add_fieldsets + (("Additional info",
                                                {"fields": ("first_name", "last_name", "website", "email")}
                                                ),)


admin.site.register(TeaCategory)
admin.site.register(Province)
