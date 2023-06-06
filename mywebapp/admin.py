from django.contrib import admin
from .models import Home, About, Profile, Category, Skills, Techer, Techert,Blog


# Home
admin.site.register(Home)


# About
class ProfileInline(admin.TabularInline):
    model = Profile
    extra = 1

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
     inlines = [
        ProfileInline,
    ]

# Skills
class SkillsInline(admin.TabularInline):
    model = Skills
    extra = 2

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
     inlines = [
        SkillsInline,
    ]

# Portfolio
admin.site.register(Techer)

#techer2

admin.site.register(Techert)

#blog post
admin.site.register(Blog)


# class StudentAdmin(admin.ModelAdmin):
#     list_display = ['user', 'first_name', 'last_name', 'show_image_pic']
#     search_fields = []
#     list_filter = []

# admin.site.register(Student, StudentAdmin)