"""
URL configuration for my_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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

from django.urls import path, include
from hello import views
from django.contrib import admin
 
urlpatterns = [
    path("", views.index),
    path("contacts/", views.contacts),
    path("database/", views.database),
    path("database/create/", views.create),
    path("database/edit/<int:id>/", views.edit),
    path("database/delete/<int:id>/", views.delete),
    path("projects/", views.projects),
    path("comments/", views.comments),
    path("comments/create-comment/", views.create_comment),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]