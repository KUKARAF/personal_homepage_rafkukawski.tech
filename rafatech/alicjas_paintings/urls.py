from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import create_painting


urlpatterns = [
    path('', views.template_index, name='template_index'),
    path('create', views.create_painting),
    path('signup', views.signup),
    #url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #    views.activate, name='activate'),
    path('account_activation_sent', views.account_activation_sent, name='account_activation_sent'),
    path('painting/<int:painting_id>', views.template_painting),
    path('img/<int:painting_id>', views.upload_image ),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
