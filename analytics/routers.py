class AnalyticsRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == "analytics":
            return "analytics"
        return "default"

    def db_for_write(self, model, **hints):
        if model._meta.app_label == "analytics":
            return "analytics"
        return "default"

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == "analytics":
            return db == "analytics"
        if db == "default":
            return app_label != "analytics"
        return db == "default"
