from django.contrib import admin
# from django.urls import reverse
# from django.utils.html import format_html
# from django.utils.http import urlencode

from commercial_network.models import Contact, Products, Provider

admin.site.register(Contact)
admin.site.register(Products)


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    search_fields = ("contact__city__icontains", )
    # list_display = ("name", "credit", "view_provider_link")
    #
    # def view_provider_link(self, obj):
    #     # count = obj.provider.count()
    #     url = (
    #         reverse("admin:commercial_network_provider_changelist")
    #         + "?"
    #         + urlencode({"contact__id": f"{obj.id}"})
    #     )
    #     return format_html('<a href="{}">{} Email</a>', url)
    # view_provider_link.short_description = "Email"
