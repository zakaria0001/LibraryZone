from django.shortcuts import redirect, render
import requests
from sqlalchemy import null




def api(request):
    args = {}
    bookname = request.GET.get('book', False)
    response = requests.get(
        f"https://www.googleapis.com/books/v1/volumes?q=intitle:{bookname}")
    args['items'] = response.json()
    return render(request, 'api.html', args)

def dashboard(request):
   
    return render(request, 'Dashboard.html')

