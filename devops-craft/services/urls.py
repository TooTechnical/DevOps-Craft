from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [
    path('', views.list_services, name='list_services'),  # URL for listing services
    path('create/', views.create_service, name='create_service'),  # URL for creating a new service
    path('<int:pk>/', views.detail_service, name='detail_service'),  # URL for service details
    path('<int:pk>/update/', views.update_service, name='update_service'),  # URL for updating a service
    path('<int:pk>/delete/', views.delete_service, name='delete_service'),  # URL for deleting a service
]from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [
    path('', views.list_services, name='list'),  # URL for listing services
]
