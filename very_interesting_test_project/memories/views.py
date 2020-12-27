from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import Memory

def login(request):
    return render(request, 'login.html')


@login_required
def profile(request):
    memories_list = Memory.objects.filter(author=request.user)
    paginator = Paginator(memories_list, 5)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(
        request,
        'profile.html',
        {'page': page, 'paginator': paginator}
    )
