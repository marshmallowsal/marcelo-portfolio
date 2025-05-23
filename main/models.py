from django.db import models
from django.core.validators import FileExtensionValidator

class HeroSection(models.Model):
    greeting = models.CharField(max_length=100, default="HELLO, I'M")
    name = models.CharField(max_length=100, default="MARCELO SALINAS")
    title = models.CharField(max_length=200, default="Mechanical Engineering Student & Designer")
    description = models.TextField(default="Specializing in innovative mechanical solutions and 3D modeling for complex engineering challenges. I transform concepts into functional products with precision and creativity.")
    model_3d = models.FileField(
        upload_to='hero_models/',
        validators=[FileExtensionValidator(allowed_extensions=['glb', 'gltf'])],
        blank=True,
        null=True,
        help_text="Upload a .glb or .gltf file for the 3D model"
    )
    primary_button_text = models.CharField(max_length=50, default="VIEW MY WORK")
    secondary_button_text = models.CharField(max_length=50, default="GET IN TOUCH")
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Hero Section"
        verbose_name_plural = "Hero Section"
    
    def __str__(self):
        return f"Hero Section - {self.name}"

class FeaturedProject(models.Model):
    CATEGORY_CHOICES = [
        ('cad', 'CAD Design'),
        ('prototypes', 'Prototypes'),
        ('simulations', 'Simulations'),
        ('consulting', 'Consulting'),
    ]
    
    title = models.CharField(max_length=200)
    excerpt = models.TextField(help_text="Brief description for the project card")
    image = models.URLField(help_text="URL to project image")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    date = models.CharField(max_length=50, help_text="e.g., 'December 2024'")
    duration = models.CharField(max_length=50, help_text="e.g., '6 weeks'")
    tags = models.CharField(max_length=200, help_text="Comma-separated tags")
    project_url = models.URLField(blank=True, help_text="Link to full project details")
    order = models.PositiveIntegerField(default=0, help_text="Order of appearance")
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order', '-id']
        verbose_name = "Featured Project"
        verbose_name_plural = "Featured Projects"
    
    def __str__(self):
        return self.title
    
    def get_tags_list(self):
        return [tag.strip() for tag in self.tags.split(',') if tag.strip()]

class Model3D(models.Model):
    name = models.CharField(max_length=100)
    model_file = models.FileField(
        upload_to='3d_models/',
        validators=[FileExtensionValidator(allowed_extensions=['glb', 'gltf'])],
        help_text="Upload a .glb or .gltf file"
    )
    parts_count = models.CharField(max_length=50, help_text="e.g., '142 components'")
    created_date = models.CharField(max_length=50, help_text="e.g., 'June 12, 2023'")
    software_used = models.CharField(max_length=100, help_text="e.g., 'SolidWorks 2023'")
    dimensions = models.CharField(max_length=100, help_text="e.g., '450mm × 320mm × 280mm'")
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order', 'name']
        verbose_name = "3D Model"
        verbose_name_plural = "3D Models"
    
    def __str__(self):
        return self.name

class AboutSection(models.Model):
    content = models.TextField(default="I am a dedicated Mechanical Engineering student at Texas State University with a passion for design, innovation, and problem-solving. With hands-on experience in CAD software, 3D printing technologies, and automotive maintenance, I am constantly seeking opportunities to apply engineering principles to real-world challenges.")
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "About Section"
        verbose_name_plural = "About Section"
    
    def __str__(self):
        return "About Section"

class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    graduation_date = models.CharField(max_length=100)
    gpa = models.CharField(max_length=20, blank=True)
    honors = models.TextField(blank=True, help_text="Comma-separated honors/achievements")
    coursework = models.TextField(blank=True, help_text="Relevant coursework description")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order', '-id']
        verbose_name = "Education"
        verbose_name_plural = "Education"
    
    def __str__(self):
        return f"{self.degree} - {self.institution}"

class SkillCategory(models.Model):
    name = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order', 'name']
        verbose_name = "Skill Category"
        verbose_name_plural = "Skill Categories"
    
    def __str__(self):
        return self.name

class Skill(models.Model):
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)
    proficiency = models.CharField(max_length=50, blank=True, help_text="e.g., 'Expert', 'Intermediate'")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order', 'name']
        verbose_name = "Skill"
        verbose_name_plural = "Skills"
    
    def __str__(self):
        return f"{self.name} ({self.category.name})"

class Experience(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    achievements = models.TextField(help_text="Bullet points separated by newlines")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order', '-id']
        verbose_name = "Experience"
        verbose_name_plural = "Experience"
    
    def __str__(self):
        return self.title
    
    def get_achievements_list(self):
        return [achievement.strip() for achievement in self.achievements.split('\n') if achievement.strip()]

class WorkExperience(models.Model):
    job_title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50, help_text="Use 'Present' for current jobs")
    responsibilities = models.TextField(help_text="Bullet points separated by newlines")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order', '-id']
        verbose_name = "Work Experience"
        verbose_name_plural = "Work Experience"
    
    def __str__(self):
        return f"{self.job_title} at {self.company}"
    
    def get_responsibilities_list(self):
        return [resp.strip() for resp in self.responsibilities.split('\n') if resp.strip()]
    
    def get_date_range(self):
        return f"{self.start_date} - {self.end_date}"

class Achievement(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    link = models.URLField(blank=True, help_text="Optional link for more details")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order', '-id']
        verbose_name = "Achievement"
        verbose_name_plural = "Achievements"
    
    def __str__(self):
        return self.title

class ContactInfo(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=200)
    availability = models.CharField(max_length=100, default="Mon-Fri: 9am - 6pm CST")
    linkedin_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Contact Information"
        verbose_name_plural = "Contact Information"
    
    def __str__(self):
        return f"Contact Info - {self.email}"

class ResumeSection(models.Model):
    title = models.CharField(max_length=100, default="RESUME")
    description = models.TextField(default="Want my resume as a PDF?")
    button_text = models.CharField(max_length=50, default="Download Resume")
    resume_url = models.URLField(help_text="Direct link to resume PDF")
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Resume Section"
        verbose_name_plural = "Resume Section"
    
    def __str__(self):
        return "Resume Section"

class SiteSettings(models.Model):
    site_title = models.CharField(max_length=200, default="Marcelo Salinas - Portfolio")
    footer_text = models.CharField(max_length=200, default="© 2024 Marcelo Salinas. All rights reserved.")
    projects_section_title = models.CharField(max_length=100, default="FEATURED PROJECTS")
    projects_section_description = models.TextField(default="Explore my latest mechanical engineering projects including 3D models, prototypes, and functional designs.")
    models_section_title = models.CharField(max_length=100, default="3D MODEL EXPLORER")
    models_section_description = models.TextField(default="Interact with some of my detailed 3D models. Rotate, zoom, and explore the engineering details.")
    contact_section_title = models.CharField(max_length=100, default="CONTACT ME")
    contact_section_description = models.TextField(default="Interested in working together? Feel free to reach out for collaborations or just a friendly hello.")
    
    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"
    
    def __str__(self):
        return "Site Settings"
