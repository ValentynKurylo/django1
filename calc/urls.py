from django.urls import path
from .views import calc, main_Calc

urlpatterns = [
    path('', calc),
    path('/<int:number1>/<str:command>/<int:number2>', main_Calc)
]