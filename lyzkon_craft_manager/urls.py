"""
URL configuration for lyzkon_craft_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from craft_manager_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name="index"),
    path('lab_list/', LabListView.as_view(), name="lab_list"),
    path('new_craft/', NewCraftView.as_view(), name="new_craft"),
    path('craft_failed/', CraftFailedView.as_view(), name="craft_failed"),
    path('craft_success/', CraftSuccessView.as_view(), name="craft_success"),
    path('accreditation/', AccreditationView.as_view(), name="accreditation"),
    path('accreditation_success/', AccreditationSuccessView.as_view(), name="accreditation_success"),
]
