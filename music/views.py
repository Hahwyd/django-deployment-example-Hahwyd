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
                logger.debug("Файл успешно сохранен в S3")
                return redirect("success")
            except Exception as e:
                logger.error(f"Ошибка при сохранении формы: {e}")
                return render(request, "music/upload.html", {"form": form, "error": str(e)})
        else:
            logger.debug("Форма не валидна")
            return render(request, "music/upload.html", {"form": form, "error": "Форма не валидна"})
    else:
        form = UploadForm()
        logger.debug("GET запрос, отображение формы")

    return render(request, "music/upload.html", {"form": form})

def success_view(request):
    return render(request, "music/success.html")
