from django.conf import settings
import geoip2.database
import geoip2.errors
from django.db import models


class PageVisit(models.Model):
    session_key = models.CharField(max_length=40)
    path = models.CharField(max_length=255)
    ip_address = models.GenericIPAddressField()
    country = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    user_agent = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = "analytics"
        verbose_name = "Page Visit"
        verbose_name_plural = "Page Visits"

    def __str__(self):
        return (f"{self.path} - {self.ip_address} - "
                f"{self.user_agent} - {self.created_at}")

    def save(self, *args, **kwargs):
        self.ip_address = ".".join(self.ip_address.split(".")[:3])
        try:
            reader = geoip2.database.Reader(settings.GEOIP_DATABASE_PATH)
            response = reader.city(self.ip_address)
            self.country = response.country.name
            self.city = response.city.name
        except geoip2.errors.AddressNotFoundError:
            self.country = None
            self.city = None
        except Exception as e:
            print(f"Can not detect location: {e}")
        super().save(*args, **kwargs)
