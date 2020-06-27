from django.urls import path
from .views import CRUD_apiView
app_name = "CRUD_api"
# app_name will help us do a reverse look-up latter.

urlpatterns = [
    path('cells/', CRUD_apiView.as_view()),
    path('cells/<int:pk>', CRUD_apiView.as_view()),
]