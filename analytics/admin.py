from django.contrib import admin
from analytics.models import PageVisit


@admin.register(PageVisit)
class PageVisitAdmin(admin.ModelAdmin):
    list_display = (
        "session_key", "path", "country", "city", "created_at", "user_agent"
    )
    search_fields = ("session_key", "path", "country", "city")
    list_filter = ("country", "city", "created_at")
    date_hierarchy = "created_at"
