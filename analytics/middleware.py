from datetime import timedelta

from .models import PageVisit
from django.utils.timezone import now

from portfolio_app.utils import get_client_ip


class AnalyticsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if (request.path.startswith("/static/")
                or request.path.startswith("/admin/")
                or request.path.startswith("/accept-cookies/")):
            return response

        session_key = request.session.session_key or "anonymous"
        path = request.path.rstrip("/") + "/"
        user_agent = request.META.get("HTTP_USER_AGENT", "unknown")

        cookies_accepted = request.COOKIES.get("cookiesAccepted") == "true"
        ip_address = None

        if cookies_accepted:
            ip_address = get_client_ip(request)

        PageVisit.objects.create(
            session_key=session_key[:10],
            path=path,
            ip_address=ip_address,
            user_agent=user_agent,
            created_at=now(),
            )

        return response
