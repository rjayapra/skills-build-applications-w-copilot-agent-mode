"""octofit_tracker URL Configuration."""
import os

from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path
from rest_framework.routers import DefaultRouter

codespace_name = os.environ.get('CODESPACE_NAME')
if codespace_name:
    base_url = f"https://{codespace_name}-8000.app.github.dev"
else:
    base_url = "http://localhost:8000"

router = DefaultRouter()


def api_root(request):
    codespace_name = os.environ.get('CODESPACE_NAME')
    if codespace_name:
        base_url = f"https://{codespace_name}-8000.app.github.dev"
    else:
        base_url = "http://localhost:8000"
    return JsonResponse(
        {
            "message": "OctoFit Tracker API",
            "base_url": base_url,
            "admin": f"{base_url}/admin/",
            "api": f"{base_url}/api/",
            "activities": f"{base_url}/api/activities/",
            "users": f"{base_url}/api/users/",
            "teams": f"{base_url}/api/teams/",
            "leaderboards": f"{base_url}/api/leaderboards/",
            "workouts": f"{base_url}/api/workouts/",
        }
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_root, name='api-root'),
    path('api/', include(router.urls)),
]
