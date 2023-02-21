from django.shortcuts import render
from .models import User, Post
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render, redirect
from django.db.models import Q

import csv

def export_csv(request):
    students=User.objects.all()
    response=HttpResponse('text/cvs')
    response['Content-Disposition'] = 'attachment; filename=export_csv' + str(datetime.now()) + '.csv'

    write=csv.writer(response)
    write.writerow([ 'id',  'name', "username", "phone_number", "message", "create_at"])
    students_fields=students.values_list('id', 'name', 'username', "phone_number", "message", "create_at")
    for student in students_fields:
        write.writerow(student)
    return response

def Post_today(request):
    if 'q' in request.GET:
        q = request.GET['q']
        articles = Post.objects.filter(Q(title__icontains=q) | Q(address__icontains=q))
    else:
        articles = Post.objects.all().order_by('-id')
        q = None
    return render(request, 'post.html', {"articles": articles, "q": q})



def user_page(request):
    if request.method == "POST":
        model = User()
        model.name = request.POST.get("name")
        model.username = request.POST.get("username")
        model.phone_number = request.POST.get("phone_number")
        model.message = request.POST.get("message")

        model.save()
        return render(request, "index.html")

    else:
        return render(request, "index.html")




