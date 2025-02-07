from django.contrib.auth.models import AbstractUser
from django.db import models

from portfolio import settings


class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    information = models.TextField(null=True, blank=True)
    cv = models.TextField(null=True, blank=True)


class Education(models.Model):
    institution = models.CharField(max_length=255)
    field_of_study = models.CharField(max_length=255)
    degree = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_educations"
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]


class Experience(models.Model):
    company = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)
    location = models.CharField(max_length=255, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_experiences"
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]


class Skills(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="user_skills",
        null=True,
        blank=True
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]


class Projects(models.Model):
    type = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_projects"
    )
    date = models.DateField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    use = models.URLField(null=True, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]


class SocialMedia(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_social_media"
    )
    media = models.URLField(null=True, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]


class Languages(models.Model):
    name = models.CharField(max_length=55)
    level = models.CharField(max_length=55, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_languages"
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]
