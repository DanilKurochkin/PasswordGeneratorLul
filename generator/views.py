from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    min_num = 6
    max_num = 26
    
    nums = list(range(min_num, max_num+1))
    return render(request, 'generator/home.html', {'nums' : nums})
 
def password(request):
    
    characters = list('abcdefghijklmnopqrstuvwxyz')
    
    length = int(request.GET.get('length', 12))
    if request.GET.get('uppercase', False):
        characters += list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if request.GET.get('numbers', False):
        characters += [str(x) for x in range(10)]
    if request.GET.get('specialCharacters', False):
        characters += list('!@#$%^&*+-/?.')
    
    thepassword = ''
    for i in range(int(length)):
        thepassword += random.choice(characters)
    
    return render(request, 'generator/password.html', {'password' : thepassword})

def about(request):
    return render(request, 'generator/about.html')