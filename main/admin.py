from django.contrib import admin
from .models import (
    HeroSection, FeaturedProject, Model3D, AboutSection, Education,
    SkillCategory, Skill, Experience, WorkExperience, Achievement,
    ContactInfo, ResumeSection, SiteSettings
)

@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'is_active']
    list_filter = ['is_active']
    search_fields = ['name', 'title']
    fieldsets = (
        ('Basic Information', {
            'fields': ('greeting', 'name', 'title', 'description')
        }),
        ('3D Model', {
            'fields': ('model_3d',),
            'description': 'Upload a .glb or .gltf file for the hero 3D model'
        }),
        ('Button Text', {
            'fields': ('primary_button_text', 'secondary_button_text')
        }),
        ('Settings', {
            'fields': ('is_active',)
        })
    )

@admin.register(FeaturedProject)
class FeaturedProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'date', 'order', 'is_active']
    list_filter = ['category', 'is_active']
    search_fields = ['title', 'excerpt']
    list_editable = ['order', 'is_active']
    ordering = ['order', '-id']
    fieldsets = (
        ('Project Information', {
            'fields': ('title', 'excerpt', 'image')
        }),
        ('Classification', {
            'fields': ('category', 'tags')
        }),
        ('Timeline', {
            'fields': ('date', 'duration')
        }),
        ('Display Settings', {
            'fields': ('order', 'is_active')
        })
    )

@admin.register(Model3D)
class Model3DAdmin(admin.ModelAdmin):
    list_display = ['name', 'software_used', 'parts_count', 'order', 'is_active']
    list_filter = ['software_used', 'is_active']
    search_fields = ['name', 'description']
    list_editable = ['order', 'is_active']
    ordering = ['order', 'name']
    fieldsets = (
        ('Model Information', {
            'fields': ('name', 'model_file', 'description')
        }),
        ('Technical Details', {
            'fields': ('parts_count', 'created_date', 'software_used', 'dimensions')
        }),
        ('Display Settings', {
            'fields': ('order', 'is_active')
        })
    )

@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'is_active']
    fields = ['content', 'is_active']
    
    def has_add_permission(self, request):
        # Only allow one AboutSection instance
        return not AboutSection.objects.exists()

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1
    fields = ['name', 'proficiency', 'order', 'is_active']
    ordering = ['order', 'name']

@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    ordering = ['order', 'name']
    inlines = [SkillInline]

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency', 'order', 'is_active']
    list_filter = ['category', 'is_active']
    search_fields = ['name']
    list_editable = ['order', 'is_active']
    ordering = ['category__order', 'order', 'name']

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['institution', 'degree', 'graduation_date', 'order', 'is_active']
    list_filter = ['is_active']
    search_fields = ['institution', 'degree']
    list_editable = ['order', 'is_active']
    ordering = ['order', '-id']
    fieldsets = (
        ('Institution', {
            'fields': ('institution', 'location')
        }),
        ('Degree Information', {
            'fields': ('degree', 'graduation_date', 'gpa')
        }),
        ('Additional Information', {
            'fields': ('honors', 'coursework')
        }),
        ('Display Settings', {
            'fields': ('order', 'is_active')
        })
    )

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'is_active']
    list_filter = ['is_active']
    search_fields = ['title', 'description']
    list_editable = ['order', 'is_active']
    ordering = ['order', '-id']
    fieldsets = (
        ('Experience Information', {
            'fields': ('title', 'description')
        }),
        ('Achievements', {
            'fields': ('achievements',),
            'description': 'Enter each achievement on a new line'
        }),
        ('Display Settings', {
            'fields': ('order', 'is_active')
        })
    )

@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ['job_title', 'company', 'get_date_range', 'order', 'is_active']
    list_filter = ['is_active']
    search_fields = ['job_title', 'company']
    list_editable = ['order', 'is_active']
    ordering = ['order', '-id']
    fieldsets = (
        ('Job Information', {
            'fields': ('job_title', 'company', 'location')
        }),
        ('Timeline', {
            'fields': ('start_date', 'end_date')
        }),
        ('Responsibilities', {
            'fields': ('responsibilities',),
            'description': 'Enter each responsibility on a new line'
        }),
        ('Display Settings', {
            'fields': ('order', 'is_active')
        })
    )

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'is_active']
    list_filter = ['is_active']
    search_fields = ['title', 'description']
    list_editable = ['order', 'is_active']
    ordering = ['order', '-id']

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ['email', 'phone', 'location', 'is_active']
    list_filter = ['is_active']
    fieldsets = (
        ('Contact Details', {
            'fields': ('email', 'phone', 'location', 'availability')
        }),
        ('Social Media', {
            'fields': ('linkedin_url', 'github_url', 'twitter_url', 'instagram_url')
        }),
        ('Settings', {
            'fields': ('is_active',)
        })
    )
    
    def has_add_permission(self, request):
        # Only allow one ContactInfo instance
        return not ContactInfo.objects.exists()

@admin.register(ResumeSection)
class ResumeSectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'button_text', 'is_active']
    list_filter = ['is_active']
    fieldsets = (
        ('Resume Information', {
            'fields': ('title', 'description', 'button_text')
        }),
        ('Download Link', {
            'fields': ('resume_url',),
            'description': 'Paste the direct link to your resume PDF'
        }),
        ('Settings', {
            'fields': ('is_active',)
        })
    )
    
    def has_add_permission(self, request):
        # Only allow one ResumeSection instance
        return not ResumeSection.objects.exists()

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Site Information', {
            'fields': ('site_title', 'footer_text')
        }),
        ('Projects Section', {
            'fields': ('projects_section_title', 'projects_section_description')
        }),
        ('3D Models Section', {
            'fields': ('models_section_title', 'models_section_description')
        }),
        ('Contact Section', {
            'fields': ('contact_section_title', 'contact_section_description')
        })
    )
    
    def has_add_permission(self, request):
        # Only allow one SiteSettings instance
        return not SiteSettings.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        # Don't allow deletion of site settings
        return False

# Customize admin site headers
admin.site.site_header = 'Marcelo Salinas Portfolio Admin'
admin.site.site_title = 'Portfolio Admin'
admin.site.index_title = 'Welcome to Portfolio Administration'
