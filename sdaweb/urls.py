from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('security.urls')),
    # path('', Home.as_view(), name='home'),
    # path('', views.home, name='home')
]
