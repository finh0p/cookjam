from django.urls import path, include
from . import views

app_name = 'nutrition'

urlpatterns = [
    path('', views.index, name='index'),
    path('account/<int:id>', views.account_page, name='account'),
    # path('', include('django.contrib.auth.urls')),
    path('account/registration/', views.registration, name='signup'),
    path('account/logout/', views.logout_view, name='logout'),
    path('account/login', views.log_in, name='login'),
    path('meals/add/<int:id>', views.add_meals, name='add_meals'),
]
