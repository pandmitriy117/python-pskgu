from django.urls import path
from .views import index, contacts, blog

urlpatterns = [
    path('', index),
    path('contacts/', contacts),
    path('blog/', blog),
]
