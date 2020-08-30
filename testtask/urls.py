from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include(('chat.urls', 'chat'))),
    path('accounts/', include(('accounts.urls', 'accounts'))),
    path('admin/', admin.site.urls),
]
