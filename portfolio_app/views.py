from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.timezone import now
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView

from analytics.models import PageVisit
from portfolio_app.models import (
    Education,
    Experience,
    Skills,
    Projects,
    Languages
)
from portfolio_app.utils import get_client_ip


def index(request):
    user_model = get_user_model()
    user = user_model .objects.first()
    user_info = [
        f"Hi! My name is {user.first_name} :)",
        user.about,
    ]

    return render(request, "index.html", {"user_info": user_info})


def custom_404_view(request, exception=None):
    return render(request, "404.html", status=404)


def private_view(request):
    return render(request, "private.html")


@csrf_exempt
def accept_cookies(request):
    if request.method == "POST":
        session_key = request.session.session_key or "anonymous"
        ip_address = get_client_ip(request)
        user_agent = request.META.get("HTTP_USER_AGENT", "unknown")

        last_visit = PageVisit.objects.filter(
            session_key=session_key[:10],
            ip_address=None,
            user_agent=user_agent
        ).order_by('-created_at').first()

        if last_visit:
            last_visit.ip_address = ip_address
            last_visit.save()
            updated = 1
        else:
            updated = 0

        response = JsonResponse({
            "message": "Cookies accepted",
            "ip_address": ip_address,
            "updated_rows": updated
        })
        response.set_cookie(
            "cookiesAccepted",
            "true",
            max_age=31536000,
            path="/",
            secure=True,
            samesite="Lax"
        )
        return response

    return JsonResponse({"error": "Invalid request"}, status=400)


class EducationListView(ListView):
    model = Education
    template_name = "education.html"
    context_object_name = "educations"

    def get_queryset(self):
        return Education.objects.all().order_by("order")


class ExperienceListView(ListView):
    model = Experience
    template_name = "experience.html"
    context_object_name = "experiences"

    def get_queryset(self):
        return Experience.objects.all().order_by("order")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_date"] = now()
        return context


class SkillsListView(ListView):
    model = Skills
    template_name = "skills.html"
    context_object_name = "skills"

    def get_queryset(self):
        return Skills.objects.all().order_by("order")


class ProjectsListView(ListView):
    model = Projects
    template_name = "projects.html"
    context_object_name = "projects"

    def get_queryset(self):
        return Projects.objects.all().order_by("order")


class LanguagesListView(ListView):
    model = Languages
    template_name = "languages.html"
    context_object_name = "languages"

    def get_queryset(self):
        return Languages.objects.all().order_by("order")
