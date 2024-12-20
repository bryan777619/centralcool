from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path("pembayaran/", include('pembayaran.urls')),
    path("reservasi/", include('reservasi.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin_dashboard/', include('admin_dashboard.urls', namespace='admin_dashboard')),
    path('ratings/', include('ratings.urls', namespace='ratings')),
]