from django.contrib import admin
from quiz.models import *
# Register your models here.
from django.contrib import admin
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'question_number', 'total_marks')

from django.contrib import admin
from .models import Question

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('course', 'marks', 'question', 'answer')
    list_filter = ('course',)
    search_fields = ('question',)


from django.contrib import admin
from .models import Result

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('student', 'exam', 'marks', 'date')
    list_filter = ('student', 'exam')
    search_fields = ('student__name', 'exam__course_name')
