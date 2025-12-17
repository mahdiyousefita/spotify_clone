from django.urls import path

from music import views

urlpatterns = [
    path('', views.home, name='home'),
    path('artist/<int:artist_id>', views.artist_detail, name='artist_detail'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
