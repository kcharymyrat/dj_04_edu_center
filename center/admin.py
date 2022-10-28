from django.contrib import admin

from .models import Category, Course

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'is_active']
    prepopulated_fields = {"slug": ('name',)}
    search_fields = ["name"]
    list_filter = ["is_active"]
    list_editable = ["is_active"]


admin.site.register(Category, CategoryAdmin)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'rayat_price', 'student_price', 'discount_amount', 'is_active']
    prepopulated_fields = {"slug": ('title',)}
    list_editable = ['rayat_price', 'student_price', 'discount_amount', 'is_active']
    list_filter = ['is_active', 'category', 'title', 'rayat_price']