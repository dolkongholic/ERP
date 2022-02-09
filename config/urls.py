from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("core.urls", namespace="core")),
    path("groupware/", include("groupware.urls", namespace="groupware")),
    path("schedules/", include("schedules.urls", namespace="schedules")),
    path("products/", include("products.urls", namespace="products")),
    path("educations/", include("educations.urls", namespace="educations")),
    path("consultings/", include("consultings.urls", namespace="consultings")),
    path("etc/", include("etc.urls", namespace="etc")),
    path("accounts/", include("accounts.urls", namespace="accounts")),
    path("users/", include("users.urls", namespace="users")),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
