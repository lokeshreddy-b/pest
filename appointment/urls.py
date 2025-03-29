from django.urls import path
from .views import book_appointment

urlpatterns = [
    path('api/book-appointment/', book_appointment, name='book_appointment'),
]
