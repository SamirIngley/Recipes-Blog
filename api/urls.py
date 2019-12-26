from django.urls import path

from api.views import PageList, PageDetail

urlpatterns = [
    path('recipe/', PageList.as_view(), name='recipe_list'),
    path('recipe/<int:pk>', PageDetail.as_view(), name='recipe_detail')
]
