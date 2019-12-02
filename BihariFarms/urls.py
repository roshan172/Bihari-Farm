from django.contrib import admin
from django.urls import path
from farmsite import views
from django.contrib.auth import views as authViews
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('profile/',user_views.profile,name='profile'),
    path('',views.index,name='homepage'),

    path('shop/',views.shop,name='shop'),
    path('contact/',views.contact,name='contact'),
    path('blog/',views.blog,name='blog'),
    path('addCart/<int:pk>/',views.addCart,name='addCart'),
    path('cart/',views.cartPage,name='cart')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)