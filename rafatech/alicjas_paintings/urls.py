from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import create_painting
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.template_index, name='template_index'),
    path('create', views.create_painting),
    path('signup', views.signup),
    #path('logout', views.logout_view),
    path( 'login',auth_views.LoginView.as_view(template_name="ap/en/login.html"), name="login"),
    path( 'logout',auth_views.LogoutView.as_view(template_name="ap/en/logout.html"), name="logout"),

    #url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #    views.activate, name='activate'),
    path('painting/<int:painting_id>', views.template_painting),
    path('painting/rm/<int:painting_id>', views.painting_rm),
    path('img/<int:painting_id>', views.upload_image ),
    path('cart/add/<int:painting_id>', views.cart_add),
    path('cart/rm/<int:painting_id>', views.cart_rm),
    path('cart/ls.json', views.cart_index_json, name='cart_index_json'),
    path('user/cart/<int:painting_id>', views.cart_index, name='cart_index'),
    path('user/cart', views.cart_index, name='cart_index'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
