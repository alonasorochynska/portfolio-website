from django.contrib import admin
from analytics.models import PageVisit


@admin.register(PageVisit)
class PageVisitAdmin(admin.ModelAdmin):
    list_display = ("session_key", "path", "ip_address", "country", "city", "created_at")
    search_fields = ("session_key", "path", "ip_address", "country", "city")
    list_filter = ("country", "city", "created_at")
    date_hierarchy = "created_at"
