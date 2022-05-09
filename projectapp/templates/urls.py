from django.urls import path

from projectapp.views import ProjectListView, ProjectCreateView, ProjectDetailView


app_name = 'projectapp'

urlpatterns = {
    path('list/', ProjectListView.as_view(), name = 'list'),

    path('create/', ProjectCReateView.as_view(), name = 'create'),
    path('detail/<int:pk>', ProjectDetail.as_view(), name = 'detail'),
}