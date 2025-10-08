from django.urls import path
from .views import PostListAPIView, PostDetailAPIView
from .views import CommentListCreateAPIView
from .views import login_view, logout_view
from .views import signup_view
from django.conf import settings
from django.conf.urls.static import static
from .views import test_image
from .views import get_user_info, admin_delete_comment
from rest_framework.routers import DefaultRouter

from django.urls import path, include
from .views import PostListAPIView, PostDetailAPIView

urlpatterns = [
    path('api/posts/', PostListAPIView.as_view(), name='api_post_list'),
    path('api/posts/<int:pk>/', PostDetailAPIView.as_view(), name='api_post_detail'),
    path('api/posts/<int:post_id>/comments/', CommentListCreateAPIView.as_view(), name='api_post_comments'),
    path('api/login/', login_view, name='api_login'),
    path('api/logout/', logout_view, name='api_logout'),
    path('api/signup/', signup_view, name='api_signup'),
    path('test-image/', test_image),
    path('api/user/', get_user_info),
    path('posts/', PostListAPIView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailAPIView.as_view(), name='post-detail'),

    # Admin endpoint to delete comment
    path('api/comments/<int:comment_id>/delete/', admin_delete_comment, name='admin_delete_comment'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





