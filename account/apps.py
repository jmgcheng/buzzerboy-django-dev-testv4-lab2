from django.apps import AppConfig
from django.db.models.signals import post_migrate


class AccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'account'
    
    def ready(self):
        import account.signals 
        
        def run_seed(sender, **kwargs):
            # Only run if DB is empty (no users yet)
            from django.contrib.auth import get_user_model
            User = get_user_model()
            if not User.objects.exists():
                from django.core.management import call_command
                call_command('seed_initial_data', verbosity=0)
        post_migrate.connect(run_seed, sender=self)