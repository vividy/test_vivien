from django.shortcuts import render
# from .models import Post


def index(request):
    # context = {
    #     'posts': Post.objects.order_by('-date')
    #     if request.user.is_authenticated else []
    # }

    return render(request, 'index.html')#, context)