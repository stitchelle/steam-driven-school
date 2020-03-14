import sqlite3
from django.shortcuts import redirect, render, reverse
from sdsapp.models import Grade
from ..connection import Connection


def grade_list(request):
    if request.method == 'GET':
        all_grades = Grade.objects.all()

        template = 'grades/list.html'
        context = {
            'all_grades': all_grades
        }

        return render(request, template, context)