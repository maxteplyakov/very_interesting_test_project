from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.conf import settings

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
        memory = form.save(commit=False)
        memory.author = request.user
        memory.img_url = "https://maps.googleapis.com/maps/api/" \
                         "staticmap?center={}&zoom=13&size=600x300&" \
                         "maptype=roadmap&markers=color:red%7Clabel:C%7C" \
                         "{}&key={}".format(
            memory.geolocation, memory.geolocation, settings.GOOGLE_MAPS_API_KEY
        )
        form.save()
        return redirect('/')
    return render(request, 'new_memory_form.html', {'form': form})


def page_not_found(request, exception):
    return render(
        request,
        "misc/404.html",
        {"path": request.path},
        status=404
    )


def server_error(request):
    return render(
        request,
        "misc/500.html",
        status=500
    )