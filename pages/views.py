from django.shortcuts import render
from pages.models import Page


# Create your views here.
def home(request):
    order_page = request.GET.get('order', 'recent')
    if order_page == 'old':
        pages = Page.objects.all()
    else:
        pages = Page.objects.all().order_by('-created')

    return render(request, 'pages/home.html', {'pages': pages})
