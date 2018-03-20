from django.shortcuts import render, redirect
from django.views import View
from openpyxl import load_workbook
from datetime import datetime

from .models import Project


# Create your views here.


class HomeView(View):
    template_name = 'home/index.html'

    def get(self, request, *args, **kwargs):
        projects = Project.objects.filter(active='Y')
        data = {
            'projects': projects,
            'searchType': 'sponsor',
            'search': '',
            'deadline_from': '',
            'deadline_to': '',
        }
        return render(request, self.template_name, data)

    def post(self, request, *args, **kwargs):
        search_type = request.POST.get('searchType')
        search = ''
        deadline_from = ''
        deadline_to = ''

        if search_type == 'sponsor':
            search = request.POST.get('search')
            if search:
                projects = Project.objects.filter(sponsor__contains=search, active='Y')
            else:
                projects = Project.objects.filter(active='Y')
        else:
            deadline_from = request.POST.get('deadline_from')
            deadline_to = request.POST.get('deadline_to')
            if deadline_from and deadline_to:
                projects = Project.objects.filter(deadline__range=[deadline_from, deadline_to]).order_by('deadline')
            elif deadline_from:
                projects = Project.objects.filter(deadline__gte=deadline_from).order_by('deadline')
            elif deadline_to:
                projects = Project.objects.filter(deadline__lte=deadline_to).order_by('deadline')
            else:
                projects = Project.objects.all().order_by('deadline')

        data = {
            'projects': projects,
            'searchType': search_type,
            'search': search,
            'deadline_from': deadline_from,
            'deadline_to': deadline_to,
        }
        return render(request, self.template_name, data)


class ImportDataView(View):
    def post(self, request, *args, **kwargs):
        print('import data')
        file = request.FILES['file']
        wb = load_workbook(filename=file)
        ws = wb[wb.sheetnames[0]]
        for row in ws.iter_rows(row_offset=1):
            sponsor = row[4].value
            if sponsor is None:
                continue
            title = row[6].value
            link = row[7].value
            amount = row[9].value
            deadline = row[13].value
            if isinstance(deadline, str):
                deadline = None
            synopsis = row[17].value
            active = row[41].value
            project = Project.objects.create(sponsor=sponsor, title=title, link=link, amount=amount, deadline=deadline,
                                             synopsis=synopsis, active=active)
            project.save()

        return redirect('home')
