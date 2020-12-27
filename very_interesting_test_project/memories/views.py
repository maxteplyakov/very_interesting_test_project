from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import Memory
from .forms import MemoryForm

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


@login_required()
def new_memory(request):
    if request.method != 'POST':
        form = MemoryForm()
        return render(request, 'new_memory_form.html', {
            'form': form,
        })

    form = MemoryForm(request.POST, files=request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        form.save()
        return redirect('/')
    return render(request, 'new_memory_form.html', {'form': form})
