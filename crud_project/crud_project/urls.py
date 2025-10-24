
from django.contrib import admin
from django.urls import path, include
from api.views import home  # import the home view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', home, name='home'),  # homepage route
]
