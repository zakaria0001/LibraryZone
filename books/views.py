from django.http import HttpResponse
from django.shortcuts import redirect, render
import requests
from .models import User,book_fav,FeedBack,book
from sqlalchemy import null



def home(request):
    args = {}
    bookname = request.GET.get('book', False)
    response = requests.get(
        f"https://www.googleapis.com/books/v1/volumes?q=intitle:Books")
    args['items'] = response.json()
    return render(request, 'index.html',{'args':args})

def api(request):
    args = {}
    bookname = request.GET.get('book', False)
    response = requests.get(
        f"https://www.googleapis.com/books/v1/volumes?q=intitle:{bookname}")
    args['items'] = response.json()
    return render(request, 'checkout.html', {'args':args,'CurrSearch':bookname})

def dashboard(request):
   
    return render(request, 'templates/Dashboard.html')

def checkout(request):
    args = {}
    bookname = request.GET.get('book', False)
    response = requests.get(
        f"https://www.googleapis.com/books/v1/volumes?q=intitle:{bookname}")
    args['items'] = response.json()
    return render(request,'checkout.html',  {'args':args,'CurrSearch':bookname})

def services(request):
    return render(request,'templates/services.html')

def contact(request):
    return render(request,'templates/contact.html')

# def Auths(request):
#     if request.method == 'POST':
#         if User.objects.filter(Username=request.POST['username'], MotDePasse=request.POST['password']).exists():
#             currentuser = User.objects.filter(
#                 Email=request.POST['email'], MotDePasse=request.POST['password'])
#             return render(request,'index.html',{'CurrentUser':currentuser})
#         else :
#             ErrMessage="Nom D'utilisateur Ou Mot De Passe Incorrects !"
#             return render(request,'signin.html',{'ErrMessage':ErrMessage})
#     else :
#         return render(request,'signin.html')


def Auths(request):
    if 'login' in request.POST:
        if request.method == 'POST':
            if User.objects.filter(Username=request.POST['username'], MotDePasse=request.POST['password']).exists():
                adminusr = User.objects.get(
                        Username=request.POST['username'], MotDePasse=request.POST['password'])
                if adminusr.Username=="Admin" and adminusr.MotDePasse=="123":
                    countUser = User.objects.all().count()
                    countBooks = book.objects.all().count()
                    FeedBacks=FeedBack.objects.all()
                    return render(request,'Dashboard.html',{'FeedBacks':FeedBacks,'adminusr':adminusr,'CountUser':countUser,'countBooks':countBooks})


            if User.objects.filter(Username=request.POST['username'], MotDePasse=request.POST['password']).exists():
                currentuser = User.objects.get(
                        Username=request.POST['username'], MotDePasse=request.POST['password'])
                args = {}
                response = requests.get(
                f"https://www.googleapis.com/books/v1/volumes?q=intitle:Books")
                args['items'] = response.json()
                return render(request,'index.html',{'CurrentUser':currentuser,'args':args})
            
            else :
                ErrMessage="Nom D'utilisateur Ou Mot De Passe Incorrects !"
                return render(request,'signin.html',{'ErrMessage':ErrMessage})  
        return render(request, 'signin.html')
    if 'signup' in request.POST:
         if request.method == 'POST':
            if User.objects.filter(Username=request.POST['username'], MotDePasse=request.POST['password']).exists():
                
                return render(request, 'signin.html', {'msgerr': 'Utilisateur Existe Deja '})
            else :
                Users = User(Username=request.POST['username'], MotDePasse=request.POST['password'],
                            Nom=request.POST['nom'], Prenom=request.POST['prenom'], Email=request.POST['email'])
            Users.save()
            a = True

            if a == True:
                return render(request, 'signin.html', {'msg': 'Utilisateur Créé AVec Succès !'}) 
    else: 
          return render(request,'signin.html')  



def LikedBooks(request):
    if request.method=='POST':
        LikedB = book_fav(NomLivre=request.POST['NomLivre'], Username=request.POST['Utilisateur'])
        LikedB.save()
        currentuser = User.objects.get(
                    Username=request.POST['Utilisateur'])
        args = {}
        response = requests.get(
              f"https://www.googleapis.com/books/v1/volumes?q=intitle:Books")
        args['items'] = response.json()
        return render(request,'index.html',{'Liked':'Liked','LikedBook':LikedB,'args':args,'CurrentUser':currentuser})    

def FeedBacks(request):
    if request.method=='POST':
        FeedBacks=FeedBack(Nom=request.POST['nomCl'],Prenom=request.POST['prenomCl'],
                           Email=request.POST['email'],Message=request.POST['message'],NumeroDeTelephone=request.POST['NumTel'])  
        FeedBacks.save()
        return render(request,'contact.html',{'Done':'Message Envoyé'})     
