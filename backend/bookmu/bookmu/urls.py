from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('posts.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('dj_rest_auth.urls')),
]
