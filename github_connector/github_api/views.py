from django.shortcuts import render


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .services.github_service import get_user_repos, get_repo_issues, create_issue


@api_view(['GET'])
def fetch_repositories(request, username):
    data = get_user_repos(username)
    if "error" in data:
        return Response(data,status=status.HTTP_400_BAD_REQUEST)
    
    return Response(data,status=status.HTTP_200_OK)



@api_view(['GET'])
def fetch_repo_issues(request, owner, repo):
    data = get_repo_issues(owner, repo)

    if "error" in data:
        return Response(data,status=status.HTTP_400_BAD_REQUEST)
    
    return Response(data,status=status.HTTP_200_OK)



@api_view(['POST'])
def create_github_issue(request, owner, repo):
    title = request.data.get("title")
    body = request.data.get("body")

    if not title:
        return Response(
            {"error": "Title is required"},
            status=status.HTTP_400_BAD_REQUEST
        )
    

    if len(title) < 3:
        return Response(
            {"error": "Title must be at least 3 characters"},
            status=status.HTTP_400_BAD_REQUEST
        )

    result = create_issue(owner, repo, title, body)

    if "error" in result:
        return Response(result, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(result, status=status.HTTP_201_CREATED)