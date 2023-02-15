from django.contrib import admin
from django.urls import path, include
from base.views import logout_user, index, Login, register
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('register/', register, name='register_page'),
    # path('login/', LoginView.as_view(template_name='base/login.html', redirect_authenticated_user=True), name='login_page'),
    path('login/', Login.as_view(), name='login_page'),
    path('user/', include('base.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
