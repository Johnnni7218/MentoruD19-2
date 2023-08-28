from django.urls import path
from .views import PostList, post_create, feedback_create, PostDetail, FeedbackList, PostUpdate, PostDelete, \
   FeedbackDelete, filter_posts, PostDetailUser, FeedbackListUser, FeedbackDetail, feed_accept

urlpatterns = [
   path('', PostList.as_view(), name='posts'),
   path('create/', post_create, name='post_create'),
   path('create_feed/', feedback_create, name='feedback_create'),
   path('<int:pk>/', PostDetail.as_view(), name='post'),
   path('feedback/<int:pk>/', FeedbackDetail.as_view(), name='feedback'),
   path('post_user/<int:pk>/', PostDetailUser.as_view(), name='post_user'),
   path('feedbacks/<int:post_id>/', FeedbackList.as_view(), name='feedbacks'),
   path('feedbacks_user/<int:post_id>/', FeedbackListUser.as_view(), name='feedbacks_user'),
   path('update/<int:pk>', PostUpdate.as_view(), name='post_update'),
   path('delete/<int:pk>', PostDelete.as_view(), name='post_delete'),
   path('delete_feed/<int:pk>', FeedbackDelete.as_view(), name='feedback_delete'),
   path('user_posts/', filter_posts, name='user_posts'),
   path('accept/', feed_accept, name='feed_accept'),
]
