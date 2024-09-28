from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Darkstain API",
        default_version='v1',
        description="Hotel management API",
        terms_of_service="",
        contact=openapi.Contact(email="pzaloznyi@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
