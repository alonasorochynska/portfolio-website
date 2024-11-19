from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views.generic import ListView

from portfolio_app.models import Education, Experience, Skills, Projects, Languages


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
