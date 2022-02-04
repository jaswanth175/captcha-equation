from django.shortcuts import render,redirect
from .models import *
import json
from django.http import HttpResponse
# Create your views here.
from rest_framework.parsers import JSONParser

# Create your views here.
def home(request):
    questions=QuesModel.objects.all()
    if request.method == 'GET': 
        if "message" in request.session: 
            if request.session["count"]>5:
                context = {
                    'reply':"SORRY YOU HAVE REACHED MAXIMUM NUMBER OF TRIES"
                }
                return render(request,'response.html',context)
            else:
                context = {'questions':questions[request.session["count"]:request.session["count"]+1]}
                context["message"] = request.session["message"]+" retry count :"+str(request.session["count"])
                return render(request,'home.html',context)
        else:
           request.session["i"]=0
           context = {'questions':questions[0:1]}
           return render(request,'home.html',context)
    
    if request.method == 'POST':
        questions=QuesModel.objects.all()
        if "count" not in request.session : 
            request.session["count"] = 0 
        
        for q in questions:
            print(request.POST.get(q.question))
            if q.ans ==  request.POST.get(q.question):
                context = {
                    'reply':"successfully verified captcha"
                }
                return render(request,'response.html',context)
        else:   
                request.session["count"] = request.session["count"]+1
                request.session["message"] = " incorrect answer try again"
                context = {
                    'reply':"incorrect answer"
                }
                
                return redirect('home')