from django.contrib import admin

from .models import Course, Group, Loop, Person, LoopCourse

admin.site.register(Course)
admin.site.register(Group)
admin.site.register(Person)

class LoopCourseAdminInline(admin.TabularInline):
    model = LoopCourse
    extra = 1

@admin.register(Loop)
class LoopAdmin(admin.ModelAdmin):
    inlines = (LoopCourseAdminInline,)

