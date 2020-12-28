from django.contrib import admin
from django.urls import path, include

handler404 = "memories.views.page_not_found"
handler500 = "memories.views.server_error"

urlpatterns = [
    path('', include('memories.urls')),
    path('admin/', admin.site.urls),
]
