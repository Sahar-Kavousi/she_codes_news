from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('add-story/', views.AddStoryView.as_view(), name='newStory'),
    path('<int:pk>/update', views.StoryUpdateView.as_view(),name='update'),
    path('<int:pk>/comment', views.AddCommentView.as_view(), name='addComment'),


]