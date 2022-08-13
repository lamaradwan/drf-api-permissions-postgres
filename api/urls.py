from django.urls import path

from .views import QuoteListView, QuoteDetailView, PostListView, PostDetailView

urlpatterns = [
    path('', QuoteListView.as_view(), name = 'things_list'),
    path('<int:pk>/', QuoteDetailView.as_view(), name = 'things_detail'),
    path('post/', PostListView.as_view(), name='things_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='things_detail'),
]