from django.shortcuts import render, redirect
from sections.models import Post, Gallery


# Create your views here.
def page(request):
    id = request.GET.get('id', None)

    if not id:
        return redirect('home')

    try:
        id = int(id)
    except ValueError:
        return redirect('home')

    order_page = request.GET.get('order', 'recent')
    if order_page == 'old':
        posts = Post.objects.filter(page_id=id).all()
    else:
        posts = Post.objects.filter(page_id=id).all().order_by('-created')

    image = posts[0].page.image
    title = posts[0].page.title
    return render(request, 'sections/inner_pages.html', {'posts': posts, 'title': title, 'image': image, 'page_id': id})
