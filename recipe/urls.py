from django.urls import path
from recipe.views import PageListView, PageDetailView, PageCreateView


urlpatterns = [
    path('', PageListView.as_view(), name='recipe-list-page'),
    path('create/', PageCreateView.as_view(), name='new-page'),
    path('<str:slug>/', PageDetailView.as_view(), name='recipe-details-page'),
]
