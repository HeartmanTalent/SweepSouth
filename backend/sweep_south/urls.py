from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core import views



router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'jobs', views.JobViewSet)
router.register(r'tags', views.TagViewSet)
router.register(r'job-types', views.JobTypeViewSet)
router.register(r'job-tag-link', views.JobTagLinkViewSet)
router.register(r'job-type-link', views.JobTypeLinkiewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls'))
]
