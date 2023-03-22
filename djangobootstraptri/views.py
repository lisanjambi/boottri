from django.shortcuts import render

def index(request):
    return render(request,'index.html')
def contacts(request):
    return render(request,'contact.html')
def about(request):
    return render(request, 'contact.html')
def testimonials(request):
    return render(request,'testimonial.html')
def fruits(request):
    return render(request,'fruit.html')