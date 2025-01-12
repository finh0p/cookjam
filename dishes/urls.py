from django.urls import path
from . import views

app_name = 'dishes'

urlpatterns = [
    path('', views.dishes_list, name='dishes_list'),
    path('<int:id>/', views.dish_detail, name='dish_detail'),
    path('add-dish/', views.add_dish, name='add_dish'), 
]
