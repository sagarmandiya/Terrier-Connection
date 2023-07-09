# Model View Template (MVT)

from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

# def home_page(request):
#     return HttpResponse("<h1>Hello World!</h1>")

# def about_page(request):
#     return HttpResponse("<h1>About page</h1>")

# def contact_page(request):
#     return HttpResponse("<h1>Contact page</h1>")

def home_page(request):
    home_title = "Tercon - Home"
    # title = "Hello there..."
    # doc = "<h1>{title}</h1>".format(title=title)
    # django_rendered_doc = "<h1>{{title}}</h1>".format(title=title)
    return render(request, "home.html", {"page_title": home_title})

def about_page(request):
    about_title = "Django - About"
    return render(request, "about.html", {"page_title": about_title})

def contact_page(request):
    contact_title = "Django - Contact"
    return render(request, "home.html", {"page_title": contact_title})

def example_page(request):
    context       = {"title": "Example"}
    template_name = "home.html"
    template_obj = get_template(template_name=template_name)
    return HttpResponse(template_obj.render(context))
