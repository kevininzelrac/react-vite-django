from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
import json

from .models import Post

def posts_view(request, post_id=None):
    if request.method == 'GET':
        # Get all posts or get a post by ID
        if post_id is None:
            queryset = Post.objects.all()
            data = {"posts": list(queryset.values())}
        else:
            try:
                post = Post.objects.get(id=post_id)
                data = {"post": {"id": post.id, "title": post.title, "content": post.content}}
            except Post.DoesNotExist:
                return HttpResponse(status=404)

        content = json.dumps(data, cls=DjangoJSONEncoder)
        return HttpResponse(content, content_type='application/json', status=200)

    elif request.method == 'POST':
        # Add a new post
        body = json.loads(request.body.decode('utf-8'))
        id = body.get("id")
        title = body.get("title")
        content = body.get("content")
        post = Post.objects.create(id=id, title=title, content=content)
        post.save()
        return HttpResponse(status=201)

    elif request.method == 'PUT':
        # Update an existing post
        if post_id is not None:
            try:
                post = Post.objects.get(id=post_id)
                body = json.loads(request.body.decode('utf-8'))
                post.title = body.get("title", post.title)
                post.content = body.get("content", post.content)
                post.save()
                return HttpResponse(status=200)
            except Post.DoesNotExist:
                return HttpResponse(status=404)
        else:
            return HttpResponse(status=400)

    elif request.method == 'DELETE':
        # Delete an existing post
        if post_id is not None:
            try:
                post = Post.objects.get(id=post_id)
                post.delete()
                return HttpResponse(status=200)
            except Post.DoesNotExist:
                return HttpResponse(status=404)
        else:
            return HttpResponse(status=400)

    else:
        return HttpResponse(status=405)