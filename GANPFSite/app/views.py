"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from app.forms import ContactForm

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/indexBS.cshtml',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def blog(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/blogBS.cshtml',
        {
            'title':'Blog',
            'year':datetime.now().year,
        }
    )

def resources(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/resources.cshtml',
        {
            'title':'Resources',
            'year':datetime.now().year,
        }
    )

def products(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/products.cshtml',
        {
            'title':'Products',
            'year':datetime.now().year,
        }
    )

def contact(request):
    form_class = ContactForm
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contactBS.cshtml',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
            'form': form_class,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/aboutBS.cshtml',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
