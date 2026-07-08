from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
from django.http import HttpResponse
from django.urls import path

def home(request):
    return HttpResponse("API is Live! Go to /admin/")

urlpatterns = [
    path('', home),  # add this
    path('admin/', admin.site.urls),
    # ... your other urls
]
