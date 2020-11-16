from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/polls/', include('polls_api.urls'), name='api'),
    path('', include('polls.urls')),
]
