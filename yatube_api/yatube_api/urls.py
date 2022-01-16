from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path(
        'redoc/',
        # его не видит в шаблонах, в чем может бать проблема?
        TemplateView.as_view(template_name='api/redoc.html'),
        name='redoc'
    ),
]
