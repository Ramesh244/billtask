from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .services.twitter import fetch_twitter_data
from .services.facebook import fetch_facebook_data
from posts.models import Post,Comment

class SocialMediaDataView(APIView):
    def get(self, request):
        user = request.user
        twitter_data = fetch_twitter_data(user.twitter_token) if user.twitter_token else {}
        facebook_data = fetch_facebook_data(user.facebook_token) if user.facebook_token else {}
        
        return Response({
            "twitter": twitter_data,
            "facebook": facebook_data,
        })

class LikePostView(APIView):
    def post(self, request, post_id):
        try:
            post = Post.objects.get(id=post_id)
            post.likes += 1
            post.save()
            return Response({"message": "Post liked successfully"}, status=200)
        except Post.DoesNotExist:
            return Response({"error": "Post not found"}, status=404)

class LikePostView(APIView):
    def post(self, request, post_id):
        post = Post.objects.get(id=post_id)
        post.likes += 1
        post.save()
        return Response({"message": "Post liked successfully!"})

class CommentOnPostView(APIView):
    def post(self, request, post_id):
        post = Post.objects.get(id=post_id)
        content = request.data.get("content")
        Comment.objects.create(post=post, user=request.user, content=content)
        return Response({"message": "Comment added successfully!"})


from rest_framework.views import APIView

class AnalyticsView(APIView):
    def get(self, request):
        user = request.user
        total_posts = Post.objects.filter(user=user).count()
        total_likes = Post.objects.filter(user=user).aggregate(total=Post.models.Sum('likes'))['total'] or 0
        return Response({"total_posts": total_posts, "total_likes": total_likes})
