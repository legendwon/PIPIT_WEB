import os

from django.urls import include, path, re_path
from django.conf import settings
from django.contrib import admin

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from api.versions.v1.users.urls import urlpatterns as user_urls

from common.statics import static
from common.environments import get_env


urlpatterns = [path("", include(user_urls))] + static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT
)

if "test" in get_env("DJANGO_SETTINGS_MODULE"):
    urlpatterns.append(
        path("admin/", admin.site.urls),
    )

schema_view = get_schema_view(
    openapi.Info(
        title="DRF Practice Backend API",
        default_version="v1",
        description=f"DRF Practice Backend Swagger.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="rootsik1221@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

if settings.DEBUG:
    urlpatterns += [
        re_path(
            r"swagger(?P<format>\.json|\.yaml)$",
            schema_view.without_ui(cache_timeout=0),
            name="schema-json",
        ),
        re_path(
            r"swagger/$",
            schema_view.with_ui("swagger", cache_timeout=0),
            name="schema-swagger-ui",
        ),
        re_path(
            r"redoc/$",
            schema_view.with_ui("redoc", cache_timeout=0),
            name="schema-redoc",
        ),
    ]
