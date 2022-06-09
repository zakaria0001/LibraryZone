from django.shortcuts import redirect, render
import requests
from .models import Utilisateur

def api(request):
    args = {}
    bookname = request.GET.get('book', False)
    response = requests.get(
        f"https://www.googleapis.com/books/v1/volumes?q=intitle:{bookname}")
    args['items'] = response.json()
    return render(request, 'api.html', args)

def dashboard(request):
    return render(request, 'Dashboard.html')

def Signup(request):
    if request.method == 'POST':
        member = Utilisateur(Nom=request.POST['Nom'], Prenom=request.POST['Prenom'],
                        Email=request.POST['email'], MotDePasse=request.POST['pswd'])
        member.save()
        return render(request, 'Login.html', {'msgsucc': 'User Created Succesfully You Can Login !!'})
    else:
        return render(request, 'Login.html')

def ConnectionAuth(request):
    return render(request,'Login.html')



    
def login (request):
    if request.method == 'POST':
        if Utilisateur.objects.filter(Email=request.POST['email'], MotDePasse=request.POST['pswd']).exists():
            currentuser = Utilisateur.objects.filter(
                Email=request.POST['email'], MotDePasse=request.POST['pswd'])
            return render(request,'Dashboard.html',{'CurrentUser':currentuser})
