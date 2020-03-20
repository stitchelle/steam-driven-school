import sqlite3
from django.shortcuts import redirect, render, reverse
from sdsapp.models import Project
from ..connection import Connection
from django.contrib.auth.decorators import login_required


@login_required
def project_list(request):
    if request.method == 'GET':

        all_projects = Project.objects.all()
        grade_id = request.GET.get('grade', None)
        subject_id = request.GET.get('subject',None)

        template = 'projects/list.html'
        context = {
            'all_projects': all_projects
        }

        return render(request, template, context)
    elif request.method == 'POST':
        form_data = request.POST

        current_user = request.user.teacher_parent

        # instantiate...
        new_project = Project(
            name = form_data['project'],
            supplies_needed = form_data['supplies'],
            description = form_data['description'],
            instruction = form_data['instruction'],
            grade_id = form_data["grade"],
            subject_id = form_data["subject"],
            teacher_parent_id = current_user.id
        )

        # and then save to the db
        print(new_project.name)
        new_project.save()

        return redirect(reverse('sdsapp:projects'))