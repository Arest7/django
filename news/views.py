from django.shortcuts import render, redirect
from .models import Articles, UploadFile
from django.http import HttpResponse, Http404, FileResponse
from django.shortcuts import get_object_or_404
from django.conf import settings
import os
import mimetypes
from django.urls import reverse

def download_pdf(request, filename):
    file_path = os.path.join(settings.MEDIA_ROOT, filename)

    # Check if the file exists
    if os.path.exists(file_path):
        with open(file_path, 'rb') as pdf_file:
            response = HttpResponse(pdf_file.read(), content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{filename}"'

            # Set the Content-Length header to the size of the file
            response['Content-Length'] = os.path.getsize(file_path)

            return response
    else:
        raise Http404("File not found")

def news_home(request):
    news =  Articles.objects.all()
    documents = UploadFile.objects.all()
    return render(request, 'news/news_home.html', {'news': news})

import os
from django.conf import settings

def display_file(request, file_name):
  
    file_path = os.path.join(settings.MEDIA_ROOT, file_name)

    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/octet-stream')

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    return response

from urllib.parse import unquote

def display_pdf(request, pdf_filename):
    try:
        # Decode the URL-encoded filename
        pdf_filename = unquote(pdf_filename)

        pdf_file_path = os.path.join(settings.MEDIA_ROOT, 'uploads', pdf_filename)

        # Rest of the view code...
    except FileNotFoundError:
        return HttpResponse("File not found", status=404)
    except Exception as e:
        # Log the error for debugging purposes
        print(f"Error in display_pdf: {str(e)}")
        return HttpResponse("Internal Server Error", status=500)

from django.http import JsonResponse

def get_pdf_url(request, pdf_filename):
    pdf_url = reverse('display_pdf', kwargs={'pdf_filename': pdf_filename})
    return JsonResponse({'pdf_url': pdf_url})