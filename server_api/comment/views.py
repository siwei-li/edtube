from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .models import Comment, CommentSerializer


@method_decorator(name="list", decorator=swagger_auto_schema(tags=["comments"]))
@method_decorator(name="create", decorator=swagger_auto_schema(tags=["comments"]))
@method_decorator(name="retrieve", decorator=swagger_auto_schema(tags=["comments"]))
@method_decorator(name="destroy", decorator=swagger_auto_schema(tags=["comments"]))
class CommentsOp(viewsets.ModelViewSet):
    '''

retrieve:
    Return a comment instance.

list:
    Return all comments, ordered by most recently added.

create:
    Add a new comment or reply.

- Less than 5000 characters.

delete:
    Remove an existing comment or reply.

    '''

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticatedOrReadOnly]
    http_method_names = ['get', 'post', 'head', 'delete']


    def list(self, request, video_id):
        serializer = CommentSerializer(Comment.objects.filter(video_id=video_id,parent=None),many=True)
        return Response(serializer.data)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
