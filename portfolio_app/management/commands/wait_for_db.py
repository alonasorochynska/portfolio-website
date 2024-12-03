import time
from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError, InterfaceError


class Command(BaseCommand):
    help = "Your app waits for the database to be available"

    def handle(self, *args, **kwargs):
        self.stdout.write("Waiting for database...")
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections["default"]
                db_conn.cursor().execute("SELECT 1")
                self.stdout.write(self.style.SUCCESS("Database available!"))
            except (OperationalError, InterfaceError):
                self.stdout.write("Database unavailable, waiting 1 second...")
                db_conn = None
                time.sleep(1)
