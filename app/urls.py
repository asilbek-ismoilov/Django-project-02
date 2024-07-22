from django.urls import path
from .views import home_view, portfolio_view, books_view, gallery_view, about_view, singlegal_view, blogmas_view, blogsid_view, form_view,ContactFormView

urlpatterns = [
    path('',home_view,name='home-page'),
    path('portfolio/',portfolio_view,name='portfolio-page'),
    path('books/',books_view,name='books-page'),
    path('gallery/',gallery_view,name='gallery-page'),
    path('about/',about_view,name='about-page'),
    path('contact/',ContactFormView.as_view(),name='contact-page'),
    path('single-gallery/',singlegal_view,name='singlegal-page'),
    path('blog-mas/',blogmas_view,name='blogmas-page'),
    path('blog-sid/',blogsid_view,name='blogsid-page'),
    path('form/',form_view,name='form-page'),
]
