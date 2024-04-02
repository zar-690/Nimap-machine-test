from django.contrib import admin
from django.urls import path, include
from infotech import views
from rest_framework.routers import DefaultRouter

#Creating Router object
router = DefaultRouter()

#Register StudentViewSet with Router
router.register('user', views.UserViewSet, basename='user')
router.register('clients', views.ClientViewSet, basename='clients')
router.register('projects', views.ProjectViewSet, basename='projects')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
     path('auth/', include('rest_framework.urls')),
     

]
