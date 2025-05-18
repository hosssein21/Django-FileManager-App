from django.urls import path
from . import views

app_name='dashboard'
urlpatterns=[
    path('home/',views.DashboardHomeView.as_view(),name='home'),
    path('folder-list/',views.DashboadFolderListView.as_view(),name='folder-list'),
    path('folder/<int:pk>/',views.DashboardFolderDetailView.as_view(),name='folder-detail'),
    path('folder/<int:pk>/edit/', views.DashboardFolderEditView.as_view(), name='folder-edit'),
    path('folder/<int:pk>/delete/', views.DashboardFolderDeleteView.as_view(), name='folder-delete'),
    path('file/<int:pk>/edit/', views.DashboardFileUpdateView.as_view(), name='file-edit'),
    path('file/<int:pk>/delete/', views.DashboardFileDeleteView.as_view(), name='file-delete'),
    path('folder/add/', views.DashboardFolderCreateView.as_view(), name='add-root-folder'),
    path('folder/add/<int:parent_id>/', views.DashboardFolderCreateView.as_view(), name='add-subfolder'),
    path('file/add/', views.DashboardFileCreateView.as_view(), name='add-root-file'),  # upload without folder
    path('file/add/<int:folder_id>/', views.DashboardFileCreateView.as_view(), name='add-file'),
]