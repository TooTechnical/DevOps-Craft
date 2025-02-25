from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel
    path('services/', include('services.urls')),  # Include URLs from services app
    path('checkout/', include('payments.urls')),  # Include URLs from payments app
]
