from django.shortcuts import render

def home_view(request):
    return render(request, "index.html")

def portfolio_view(request):
    return render(request, "portfolio.html")

def books_view(request):
    return render(request, "books.html")

def gallery_view(request):
    return render(request, "gallery.html")

def about_view(request):
    return render(request, "about.html")

def contact_view(request):
    return render(request, "contact.html")

def singlegal_view(request):
    return render(request, "gallery-single.html")

def blogmas_view(request):
    return render(request, "blog-masonry.html")

def blogsid_view(request):
    return render(request, "blog-sidebar.html")

def form_view(request):
    return render(request, "form-elem.html")