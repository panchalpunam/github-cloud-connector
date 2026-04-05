from django.urls import path
from .views import fetch_repositories, fetch_repo_issues, create_github_issue


urlpatterns = [
    path('repos/<str:username>/', fetch_repositories),
    path('issues/<str:owner>/<str:repo>/', fetch_repo_issues),
    path('create-issue/<str:owner>/<str:repo>/', create_github_issue),
    
]