from django.urls import path
from messages_api.views import CreateMessage, PostView
urlpatterns = [
    path('create', CreateMessage.as_view(), name='create_message'),
    path('posts', PostView.as_view(), name='posts_list'),
]
