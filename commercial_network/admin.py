from django.contrib import admin

from commercial_network.models import Contact, Products, Provider

admin.site.register(Contact)
admin.site.register(Products)


@admin.register(Provider)
class CityAdmin(admin.ModelAdmin):
    search_fields = ("contact__city__icontains", )
