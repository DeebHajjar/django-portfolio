from django.contrib import admin
from . import models

@admin.register(models.About)
class AboutAdmin (admin.ModelAdmin):
    list_per_page = 20


@admin.register(models.Home)
class HomeAdmin (admin.ModelAdmin):
    list_per_page = 20


@admin.register(models.SocialMedia)
class SocialMediaAdmin (admin.ModelAdmin):
    list_per_page = 20


@admin.register(models.Skills)
class SkillsAdmin (admin.ModelAdmin):
    list_per_page = 20


@admin.register(models.Project)
class ProjectAdmin (admin.ModelAdmin):
    list_per_page = 20


@admin.register(models.Images)
class ImagesAdmin (admin.ModelAdmin):
    list_per_page = 20


@admin.register(models.ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('created_at',)


@admin.register(models.ProjectRating)
class ProjectRatingAdmin(admin.ModelAdmin):
    list_display = ['project', 'name', 'rating', 'created_at']
    list_filter = ['rating', 'created_at']
    search_fields = ['project__title', 'name', 'message']
