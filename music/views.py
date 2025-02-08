from django.shortcuts import render, redirect
from .forms import UploadForm
from .models import Song
import logging

logger = logging.getLogger(__name__)

def index(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect("success")
            except Exception as e:
                logger.error(f"Error saving form: {e}")
                return render(request, "music/upload.html", {"form": form, "error": str(e)})
    else:
        form = UploadForm()

    return render(request, "music/upload.html", {"form": form})


def success_view(request):
    return render(request, "music/success.html")
