from django.urls import path

from portfolio_app.views import (
    index,
    custom_404_view,
    EducationListView,
    ExperienceListView,
    SkillsListView,
    ProjectsListView,
    LanguagesListView,
    private_view,
    accept_cookies,
)

urlpatterns = [
    path("", index, name="index"),
    path('accept-cookies/', accept_cookies, name='accept-cookies'),
    path("educations/", EducationListView.as_view(), name="education"),
    path("experiences/", ExperienceListView.as_view(), name="experience"),
    path("skills/", SkillsListView.as_view(), name="skills"),
    path("projects/", ProjectsListView.as_view(), name="projects"),
    path("languages/", LanguagesListView.as_view(), name="languages"),
    path("private/", private_view, name="private"),
]

handler404 = custom_404_view

app_name = "portfolio"
