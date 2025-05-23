from django.core.management.base import BaseCommand
from main.models import FeaturedProject

class Command(BaseCommand):
    help = 'Update featured projects to match website display (Lego Collection and Project Gata)'

    def handle(self, *args, **options):
        self.stdout.write('Updating featured projects to match website...')

        # Clear existing featured projects
        deleted_count = FeaturedProject.objects.all().count()
        FeaturedProject.objects.all().delete()
        self.stdout.write(f'✓ Deleted {deleted_count} old featured projects')

        # Create the two projects that are actually displayed on the website
        projects_data = [
            {
                'title': 'Lego Collection',
                'excerpt': 'A comprehensive collection of detailed LEGO models designed with precision engineering. Features custom builds, modifications, and innovative building techniques showcasing mechanical engineering principles.',
                'image': 'https://via.placeholder.com/400x250/e20000/ffffff?text=LEGO+Collection',
                'category': 'cad',
                'date': 'December 2024',
                'duration': '6 months',
                'tags': 'LEGO, 3D MODELING, DESIGN, ENGINEERING',
                'order': 1,
                'is_active': True
            },
            {
                'title': 'Project Gata',
                'excerpt': 'An innovative mechanical engineering project focused on advanced prototype development and testing. Combines theoretical engineering concepts with practical application and real-world problem solving.',
                'image': 'https://via.placeholder.com/400x250/333333/e20000?text=Project+GATA',
                'category': 'prototypes',
                'date': 'November 2024',
                'duration': '4 months',
                'tags': 'PROTOTYPING, MECHANICAL, TESTING, INNOVATION',
                'order': 2,
                'is_active': True
            }
        ]

        for project_data in projects_data:
            project = FeaturedProject.objects.create(**project_data)
            self.stdout.write(f'✓ Created featured project: {project.title}')

        self.stdout.write(self.style.SUCCESS('✅ Featured projects updated successfully!'))
        self.stdout.write(self.style.SUCCESS('Now the admin panel will only show the two projects displayed on the website.')) 