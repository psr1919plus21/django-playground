from django.shortcuts import render

def index(request):
  return render(request, 'personal/home.html')

def contact(request):
  return render(request, 'personal/basic.html', {'content': ['If you want contact me, please send your message to email', 'psr1919plus21@gmail.com']})
