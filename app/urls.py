from django.urls import path
from .views import *

urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('<int:pk>/', PostDetail.as_view(), name='detail'),
    path('create/', PostCreate.as_view(), name='create'),
    path('update/<int:pk>/', PostUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', PostDelete.as_view(), name='delete'),
    path("comment/<int:post_id>", comment, name="comment"),
]