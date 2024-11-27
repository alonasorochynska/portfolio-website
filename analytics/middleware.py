from .models import PageVisit
from django.utils.timezone import now


class AnalyticsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.path.startswith("/static/") or request.path.startswith("/admin/"):
            return response

        session_key = request.session.session_key or "anonymous"
        path = request.path
        ip_address = self.get_client_ip(request)
        user_agent = request.META.get("HTTP_USER_AGENT", "unknown")

        PageVisit.objects.using("analytics").create(
            session_key=session_key,
            path=path,
            ip_address=ip_address,
            user_agent=user_agent,
            created_at=now(),
        )

        return response

    @staticmethod
    def get_client_ip(request):
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            ip = x_forwarded_for.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
        return ip
