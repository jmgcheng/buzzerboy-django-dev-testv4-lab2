from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from company.models import Company
from account.models import UserProfile

User = get_user_model()

class Command(BaseCommand):
    help = 'Seed initial data: system user + HelloWorld Company + profiles'

    def handle(self, *args, **options):
        self.stdout.write("Seeding initial data...")

        # Create system superuser
        if not User.objects.filter(username='system').exists():
            system_user = User.objects.create_superuser(
                username='system',
                email='system@helloworld.com',
                password='system123'
            )
            self.stdout.write(self.style.SUCCESS('Created system user'))
        else:
            system_user = User.objects.get(username='system')
            self.stdout.write('System user already exists')


        # Create Blizzard Company
        company, created = Company.objects.get_or_create(
            name='Blizzard',
            defaults={'description': 'We "were" awesome at creating single player games'}
        )
        if created:
            self.stdout.write(self.style.SUCCESS('Created Blizzard Company'))

        # Create HelloWorld Company
        company, created = Company.objects.get_or_create(
            name='HelloWorld Company',
            defaults={'description': 'Default company for demo and system user'}
        )
        if created:
            self.stdout.write(self.style.SUCCESS('Created HelloWorld Company'))


        # Create company profile (unique: user + company)
        UserProfile.objects.get_or_create(
            user=system_user,
            company=company,
            defaults={
                'display_name': 'System',
                'language': 'EN'
            }
        )

        # Create personal profile (unique: user + company is null)
        UserProfile.objects.get_or_create(
            user=system_user,
            company__isnull=True,  # ← THIS IS THE FIX
            defaults={
                'display_name': 'System Personal',
                'language': 'EN'
            }
        )

        # Set last active profile if not set
        if not system_user.last_active_profile:
            system_user.last_active_profile = system_user.profiles.order_by('-created_at').first()
            system_user.save(update_fields=['last_active_profile'])

        self.stdout.write(self.style.SUCCESS('Initial data seeded successfully!'))