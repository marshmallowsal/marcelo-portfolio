from django.core.management.base import BaseCommand
from main.models import (
    HeroSection, FeaturedProject, Model3D, AboutSection, Education,
    SkillCategory, Skill, Experience, WorkExperience, Achievement,
    ContactInfo, ResumeSection, SiteSettings
)

class Command(BaseCommand):
    help = 'Populate the database with initial portfolio data'

    def handle(self, *args, **options):
        self.stdout.write('Populating database with initial data...')

        # Create Hero Section
        hero, created = HeroSection.objects.get_or_create(
            id=1,
            defaults={
                'greeting': "HELLO, I'M",
                'name': 'MARCELO SALINAS',
                'title': 'Mechanical Engineering Student & Designer',
                'description': 'Specializing in innovative mechanical solutions and 3D modeling for complex engineering challenges. I transform concepts into functional products with precision and creativity.',
                'primary_button_text': 'VIEW MY WORK',
                'secondary_button_text': 'GET IN TOUCH',
                'is_active': True
            }
        )
        if created:
            self.stdout.write('✓ Hero Section created')

        # Create Featured Projects
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
            project, created = FeaturedProject.objects.get_or_create(
                title=project_data['title'],
                defaults=project_data
            )
            if created:
                self.stdout.write(f'✓ Featured Project created: {project.title}')

        # Create 3D Models
        models_data = [
            {
                'name': 'Turbine Engine',
                'parts_count': '142 components',
                'created_date': 'June 12, 2023',
                'software_used': 'SolidWorks 2023',
                'dimensions': '450mm × 320mm × 280mm',
                'description': 'High-efficiency turbine engine model with detailed blade design.',
                'order': 1
            },
            {
                'name': 'Inspection Drone',
                'parts_count': '67 components',
                'created_date': 'November 15, 2024',
                'software_used': 'Fusion 360',
                'dimensions': '350mm × 350mm × 120mm',
                'description': 'Lightweight autonomous inspection drone with custom components.',
                'order': 2
            },
            {
                'name': 'Robotic Arm',
                'parts_count': '89 components',
                'created_date': 'October 3, 2024',
                'software_used': 'SolidWorks 2023',
                'dimensions': '800mm × 200mm × 150mm',
                'description': 'Six-axis precision robotic arm for manufacturing applications.',
                'order': 3
            },
            {
                'name': 'Suspension Component',
                'parts_count': '45 components',
                'created_date': 'September 20, 2024',
                'software_used': 'ANSYS Mechanical',
                'dimensions': '300mm × 250mm × 400mm',
                'description': 'Optimized automotive suspension component with FEA analysis.',
                'order': 4
            }
        ]

        for model_data in models_data:
            model, created = Model3D.objects.get_or_create(
                name=model_data['name'],
                defaults=model_data
            )
            if created:
                self.stdout.write(f'✓ 3D Model created: {model.name}')

        # Create About Section
        about, created = AboutSection.objects.get_or_create(
            id=1,
            defaults={
                'content': 'I am a dedicated Mechanical Engineering student at Texas State University with a passion for design, innovation, and problem-solving. With hands-on experience in CAD software, 3D printing technologies, and automotive maintenance, I am constantly seeking opportunities to apply engineering principles to real-world challenges.',
                'is_active': True
            }
        )
        if created:
            self.stdout.write('✓ About Section created')

        # Create Education
        education, created = Education.objects.get_or_create(
            institution='TEXAS STATE UNIVERSITY, SAN MARCOS, TX',
            defaults={
                'degree': 'Bachelor of Science in Mechanical Engineering',
                'location': 'San Marcos, TX',
                'graduation_date': 'Expected Graduation: June 2027',
                'gpa': '3.5/4.0',
                'honors': 'Dean\'s List: Fall 2023, Fall 2024',
                'coursework': 'Relevant Coursework: Integral Calculus with Multivariables, Statics, Physics, Chemistry, Engineering Graphics',
                'order': 1,
                'is_active': True
            }
        )
        if created:
            self.stdout.write('✓ Education entry created')

        # Create Skill Categories and Skills
        design_category, created = SkillCategory.objects.get_or_create(
            name='DESIGN',
            defaults={'order': 1, 'is_active': True}
        )
        if created:
            self.stdout.write('✓ Design skill category created')

        technical_category, created = SkillCategory.objects.get_or_create(
            name='TECHNICAL',
            defaults={'order': 2, 'is_active': True}
        )
        if created:
            self.stdout.write('✓ Technical skill category created')

        design_skills = [
            ('SolidWorks', 'Expert'),
            ('Computer-Aided Design (CAD)', ''),
            ('3D Printing Technologies', ''),
        ]

        technical_skills = [
            ('Python Programming', ''),
            ('Physics & Chemistry Lab Equipment', ''),
            ('Automotive Maintenance', ''),
        ]

        for skill_name, proficiency in design_skills:
            skill, created = Skill.objects.get_or_create(
                name=skill_name,
                category=design_category,
                defaults={'proficiency': proficiency, 'is_active': True}
            )
            if created:
                self.stdout.write(f'✓ Skill created: {skill_name}')

        for skill_name, proficiency in technical_skills:
            skill, created = Skill.objects.get_or_create(
                name=skill_name,
                category=technical_category,
                defaults={'proficiency': proficiency, 'is_active': True}
            )
            if created:
                self.stdout.write(f'✓ Skill created: {skill_name}')

        # Create Experience entries
        experiences_data = [
            {
                'title': 'ADVANCED CAD AND ADDITIVE MANUFACTURING PROJECTS',
                'description': 'Various personal and academic projects involving advanced design and manufacturing.',
                'achievements': 'Developed intricate mechanical components using SolidWorks, emphasizing precision and adherence to complex specifications.\nLeveraged CAD software for detailed simulations and modifications, enhancing project outcomes.\nUtilized additive manufacturing techniques to prototype designs, refining processes and outcomes through iterative testing.',
                'order': 1
            },
            {
                'title': 'AUTOMOTIVE MAINTENANCE PROJECTS',
                'description': 'Hands-on automotive repair and maintenance experience.',
                'achievements': 'Performed comprehensive maintenance on Mazda Miata including differential and transmission fluid changes.\nDiagnosed and executed brake system repairs including pad replacement.\nConducted regular preventative maintenance and oil changes.\nDeveloped systematic approach to vehicle diagnostics and repair, integrating CAD tools for custom solutions.',
                'order': 2
            }
        ]

        for exp_data in experiences_data:
            experience, created = Experience.objects.get_or_create(
                title=exp_data['title'],
                defaults=exp_data
            )
            if created:
                self.stdout.write(f'✓ Experience created: {experience.title}')

        # Create Work Experience
        work_experiences_data = [
            {
                'job_title': 'GYMNASTICS COACH',
                'company': 'Olympia Hills',
                'location': 'Buda, TX',
                'start_date': 'August 2024',
                'end_date': 'Present',
                'responsibilities': 'Instruct students in proper technique and safety protocols.\nDevelop and implement progressive training programs.\nFoster an environment promoting teamwork and skill development.\nCommunicate effectively with parents regarding student progress.',
                'order': 1
            },
            {
                'job_title': 'SALES ASSOCIATE',
                'company': 'Foot Locker/Champs Sports',
                'location': 'Various Locations',
                'start_date': '2022',
                'end_date': '2024',
                'responsibilities': 'Three-time consecutive employee of the month.\nConsistently met and exceeded sales targets through customer-focused service.\nManaged inventory and maintained organized product displays.\nCollaborated with team members during high-volume periods.\nDeveloped strong problem-solving skills through customer conflict resolution.',
                'order': 2
            }
        ]

        for work_data in work_experiences_data:
            work_exp, created = WorkExperience.objects.get_or_create(
                job_title=work_data['job_title'],
                company=work_data['company'],
                defaults=work_data
            )
            if created:
                self.stdout.write(f'✓ Work Experience created: {work_exp.job_title} at {work_exp.company}')

        # Create Achievements
        achievements_data = [
            {
                'title': 'High School Rotary Club Member',
                'description': 'Active member of high school Rotary Club',
                'order': 1
            },
            {
                'title': 'Dean\'s List Recognition (Freshman and Sophomore Year)',
                'description': 'Achieved Dean\'s List recognition for academic excellence',
                'order': 2
            },
            {
                'title': 'First Summer Internship at CamelAI',
                'description': 'Completed first summer internship at CamelAI',
                'link': 'https://camelai.com',
                'order': 3
            }
        ]

        for ach_data in achievements_data:
            achievement, created = Achievement.objects.get_or_create(
                title=ach_data['title'],
                defaults=ach_data
            )
            if created:
                self.stdout.write(f'✓ Achievement created: {achievement.title}')

        # Create Contact Info
        contact, created = ContactInfo.objects.get_or_create(
            id=1,
            defaults={
                'email': 'marceloa.salinas2@gmail.com',
                'phone': '956-293-0882',
                'location': 'San Marcos, TX',
                'availability': 'Mon-Fri: 9am - 6pm CST',
                'linkedin_url': 'https://linkedin.com/in/yourusername',
                'github_url': 'https://github.com/yourusername',
                'twitter_url': 'https://twitter.com/yourusername',
                'instagram_url': 'https://instagram.com/yourusername',
                'is_active': True
            }
        )
        if created:
            self.stdout.write('✓ Contact Info created')

        # Create Resume Section
        resume, created = ResumeSection.objects.get_or_create(
            id=1,
            defaults={
                'title': 'RESUME',
                'description': 'Want my resume as a PDF?',
                'button_text': 'Download Here',
                'resume_url': 'https://doc-0c-2k-docstext.googleusercontent.com/export/57i112uop5cv1fgkr7tufitffo/u7duls3omejr6sektf65s5u3kk/1747945850000/114178005989514986377/114178005989514986377/15l5KmRoohZDm5Ie23LZ1e7w8pVUbYzfk9JF2CXw9oLI?format=pdf&id=15l5KmRoohZDm5Ie23LZ1e7w8pVUbYzfk9JF2CXw9oLI&token=AC4w5Vh086FUWMc6c5gdgKspH8u3CzMyAQ:1747945846894&ouid=114178005989514986377&includes_info_params=true&usp=docs_home&cros_files=false&tab=t.0&inspectorResult=%7B%22pc%22:2,%22lplc%22:21%7D&dat=AOBvIb2E10zxe2s0lgbpjhFHDPMe9QrdSfHUq4ghuRTod1lbKPa-e7UAyjsZAflDnzLcQPxA1m4z6AlLzld956vLb5L_3oo8Q8Srcq6dCg5Mzm9dnp_pzRSTHsp7ORIG4oHoPyndYNbsNQIn-MA0pKZCXdmbXhsTazE5xT_vSNTW1PaYFHoz8-F_oCb80WsnDUe_CjRoZndMn2UL0XdbK56vmkNR3C98s-DmQ0rpvow6phu7tSvnWnRLdzMswpB0rIm6jACsaAPDpLqhzKGBVwi2jYbZF_rgiGskIOLZF5D6rKb6PgpdgQeRY4NJ28Mv2Y2-BgPd_L2pBIk0vXz-3KfpYbmZNA08D6flagcEYWF28Je43KMxuFbKt9zDY3aoruKrilne53AjABHgwhPM2YDGmbDF9r3jHEtVIohHAAFY8A7296_XPgVDEi8OsiKSGHZSXASh_KBr3l_IlGoT9z7VX8zqlLAIpfjuEJCxqYcyHMgd-hlapfhtVtT_G0WNghZlQfVJMYBDQtQ07eIY0jonDEmkcIXjr7ntgx2yCHRpD5sni2YXEtg85Jk4McJGVauCLhHmkUyceMSw6dZEXwlnnstsGKGBN3SBKB8yXsX0weVCcqTZD87bnbmSFtSOrhuxHD6qAOOHKXnq7lAQM5gqGxq4msvDJ0VmIwJBwclNWYQykfMjEUrC82bEHYTyl5JC-3E_hO2kZGSdu2r5Hsz1JcDwIl0euidKVHbRa-MS70MmuUJU7XwcX52K2uIokj88r7pvdQgQzFVyZ8kkfvO5tCuppB8aIdJFcR2__Z22ljbQhaL1iDeCFPsnl7PfZf543jeUpDJWogPNSlgQ3HeGqLYI_BWyzKXclGewMQSDDcLLLKqQafbj5vmwNCNMLtlP5BrF1jd5cXtY3Je7vonF_kGNdmHgpEDiHV-MadnOjShgcyn19PPoUk4k5OU-LBEA',
                'is_active': True
            }
        )
        if created:
            self.stdout.write('✓ Resume Section created')

        # Create Site Settings
        site_settings, created = SiteSettings.objects.get_or_create(
            id=1,
            defaults={
                'site_title': 'Marcelo Salinas - Portfolio',
                'footer_text': '© 2024 Marcelo Salinas. All rights reserved.',
                'projects_section_title': 'FEATURED PROJECTS',
                'projects_section_description': 'Explore my latest mechanical engineering projects including 3D models, prototypes, and functional designs.',
                'models_section_title': '3D MODEL EXPLORER',
                'models_section_description': 'Interact with some of my detailed 3D models. Rotate, zoom, and explore the engineering details.',
                'contact_section_title': 'CONTACT ME',
                'contact_section_description': 'Interested in working together? Feel free to reach out for collaborations or just a friendly hello.'
            }
        )
        if created:
            self.stdout.write('✓ Site Settings created')

        self.stdout.write(self.style.SUCCESS('✅ Database populated successfully!'))
        self.stdout.write(self.style.SUCCESS('🔐 Admin login: username=admin, password=admin123'))
        self.stdout.write(self.style.SUCCESS('🌐 Admin URL: http://localhost:8080/admin/')) 