from django.contrib import admin
from .models import Contact, Gallery, Books, PortfolioCategory, Portfolio

admin.site.register((Contact, Gallery, Books, PortfolioCategory, Portfolio)) 
