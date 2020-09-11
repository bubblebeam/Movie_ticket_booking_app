"""movie_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from movie import views as movie_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', movie_views.home, name='home'),
    path('register/', movie_views.register, name='register'),
    path('bookings/', movie_views.bookings, name='bookings'),
    path('book/<int:movie_id>/', movie_views.book, name='book'),
    path('view_details/<int:movie_id>', movie_views.view_details, name='view_details'),
    path('customer_booking/<int:customer_id>/', movie_views.customer_booking, name='customer_booking'),
    path('cancel/<int:ticket_id>', movie_views.cancel, name='cancel'),

]
