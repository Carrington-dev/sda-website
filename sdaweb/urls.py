from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('blog/', include('blog.urls')),
    # path('', Home.as_view(), name='home'),
    # path('', views.home, name='home')
]
