from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import display_file, download_pdf, display_pdf, get_pdf_url


urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('display-file/<str:file_name>/', display_file, name='display_file'),
    path('news/media/uploads/<str:filename>/', download_pdf, name='download_pdf'),


    path('news/media/uploads/<str:pdf_filename>/', display_pdf, name='display_pdf'),
    path('<str:pdf_filename>/', get_pdf_url, name='get_pdf_url'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
