from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def madhu(request):
    return HttpResponse('<h1><marquee><b>madhu is a good boy</marquee></b></h>')

def abijith(request):
    return HttpResponse('abhi is a intelligent boy')
def abi(request):
    return HttpResponse('<b><marquee>good night</marquee></b>')
def fourth(request):
    return HttpResponse('<b> HELLO HOW ARE YOU ...<b>')
def fifth(request):
    return HttpResponse('hello')