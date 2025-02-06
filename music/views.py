from django.shortcuts import render, redirect
from .forms import UploadForm
from .models import Song


def index(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = UploadForm()

    return render(request, 'music/upload.html', {'form': form})