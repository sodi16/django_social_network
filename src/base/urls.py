from django.urls import path, include
from django.contrib.auth.decorators import login_required
from base.views import index, UserList, UserDetail, blog_and_photo_upload, profil_page, connections, messages, \
    post_page, feed, add_profil_picture, search_user
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('', feed, name='feed'),
    path('profil-<int:pk>/', UserDetail.as_view(), name='profil'),
    path('upload_post/', blog_and_photo_upload, name='upload_post'),
    path('connections/', connections, name='connections'),
    path('messages/', messages, name='messages'),
    path('post-<int:pk>', post_page, name='post_page'),
    path('logout/', LogoutView.as_view(template_name='base/home.html'), name='logout'),
    path('change_profilpic/', add_profil_picture, name='change_profilpic'),
    path('search_user', search_user, name='search_user'),
    path('account/', include('django.contrib.auth.urls'))
]