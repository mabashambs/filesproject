from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from filesapp import forms
from filesapp.models import Book
# Create your views here.
def home_view(request):
    return render(request,'filesapp/home2.html')

def book_list(request):
    books=Book.objects.all()
    return render(request,'filesapp/booklist.html',{'books':books})

def upload_book(request):
    if request.method == 'POST':
        form=forms.bookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return home_view(request)
    else:
        form=forms.bookForm()
    return render(request,'filesapp/uploadbook.html',{'form':form})
