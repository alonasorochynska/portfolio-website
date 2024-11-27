from django.db import connections
from django.db.utils import OperationalError, InterfaceError
from django.core.management.base import BaseCommand
import time


class Command(BaseCommand):
    help = "Your app waits for the database to be available"

    def add_arguments(self, parser):
        parser.add_argument(
            '--database',
            default='default',
            help='Specify the database to wait for (default is "default").',
        )

    def handle(self, *args, **options):
        db_name = options['database']
        self.stdout.write(f"Waiting for database '{db_name}'...")
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections[db_name]
                db_conn.cursor().execute("SELECT 1")
                self.stdout.write(self.style.SUCCESS(f"Database '{db_name}' is available!"))
            except (OperationalError, InterfaceError):
                self.stdout.write(f"Database '{db_name}' unavailable, waiting 1 second...")
                db_conn = None
                time.sleep(1)
