from django.contrib import admin
from .models import StudentClass

# Register your models here.

class StudentClassAdmin(admin.ModelAdmin):
    list_display = [
        'get_class',
        'student',
        'grade',
    ]

    def get_class(self, ins):
        return ins.get_class_id_display()
    get_class.short_description = "Class"

admin.site.register(StudentClass, StudentClassAdmin)

