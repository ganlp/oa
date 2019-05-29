from django.shortcuts import render
from django.http import HttpResponse
from io import StringIO

# Create your views here.

depts_list=[
    {"no":"10","name":"财务部","location":"北京"},
    {"no":"20","name":"研发部","location":"上海"},
    {"no":"30","name":"销售部","location":"武汉"}        
 ]


def index(request):
    return render(request,'index.html',{'depts_list':depts_list})
