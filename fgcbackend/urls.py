"""
URL configuration for fgcbackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from characters.views import CharacterViewSet
from characters.views import MoveViewSet
from django.conf import settings
from django.conf.urls.static import static

# create a new router
router = routers.DefaultRouter()
# register our viewsets
router.register(r'characters', CharacterViewSet) #register "/todos" routes
router.register(r'moves', MoveViewSet)

urlpatterns = [
    # add all of our router urls
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('moves/character/<str:character_name>/', MoveViewSet.as_view({'get': 'character_moves'}), name='character-moves'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)