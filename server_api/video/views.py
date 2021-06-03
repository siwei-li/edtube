from collections import OrderedDict

# from drf_yasg.inspectors import PaginatorInspector
from rest_framework import status, viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly

from video.models import Video
from video.serializers import VideoSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


# class LimitOffsetPaginatorInspectorClass(PaginatorInspector):
#
#     def get_paginated_response(self, paginator, response_schema):
#         """
#         :param BasePagination paginator: the paginator
#         :param openapi.Schema response_schema: the response schema that must be paged.
#         :rtype: openapi.Schema
#         """
#
#         return openapi.Schema(
#             type=openapi.TYPE_OBJECT,
#             properties=OrderedDict((
#                 ('count', openapi.Schema(type=openapi.TYPE_INTEGER)),
#                 ('next', openapi.Schema(
#                     type=openapi.TYPE_OBJECT,
#                     properties=OrderedDict((
#                         ('offset', openapi.Schema(type=openapi.TYPE_INTEGER)),
#                         ('limit', openapi.Schema(type=openapi.TYPE_INTEGER))
#                     ))
#                 )),
#                 ('results', response_schema),
#             )),
#             required=['results']
#         )
#
#     def get_paginator_parameters(self, paginator):
#         """
#         Get the pagination parameters for a single paginator **instance**.
#
#         Should return :data:`.NotHandled` if this inspector does not know how to handle the given `paginator`.
#
#         :param BasePagination paginator: the paginator
#         :rtype: list[openapi.Parameter]
#         """
#
#         return [
#             openapi.Parameter('offset', openapi.IN_QUERY, "Offset for Pagination", False, None, openapi.TYPE_INTEGER),
#             openapi.Parameter('limit', openapi.IN_QUERY, "Page Size", False, None, openapi.TYPE_INTEGER)
#         ]

# def method_permission_classes(classes):
#     def decorator(func):
#         def decorated_func(self, *args, **kwargs):
#             self.permission_classes = classes
#             # this call is needed for request permissions
#             self.check_permissions(self.request)
#             return func(self, *args, **kwargs)
#         return decorated_func
#     return decorator

class VideosOp(viewsets.ModelViewSet):
    '''

retrieve:
    Return a video instance.

list:
    Return all videos, ordered by most recently added.

### Pagination

| Query     | Description                  |
| --------- | ---------------------------- |
| ?page=1   | The page number              |
| ?limit=10 | The number of items per page |

### Search, Select and Sort in Collections

| Query              | Description                                                                                        |
| ------------------ | -------------------------------------------------------------------------------------------------- |
| ?search=hello       | Search the collection where title contains hello (title and the value can be anything in the collection) |                                                                        |
| ?ordering=-title       | Get data in descending order using that field                                                      |
| ?ordering=title        | Get data in ascending order using that field

create:
    Upload a new video.

- Video must be less than 5mb
- Must be a format of mp4

delete:
    Remove an existing video.

partial_update:
    Update one or more fields on an existing video.

update:
    Update a video.

    '''
    queryset = videos = Video.objects.all()
    serializer_class = VideoSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticatedOrReadOnly]
    http_method_names = ['get', 'post', 'head', 'put','delete']

    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['title']

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        if not request.user:
            return self.list(request, *args, **kwargs)
        else:
            # return self.request.user.accounts.all()
            return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.perform_update(request, VideoSerializer)

    # @action(detail=True, methods=['post'],name="Search videos")
    # def search(self, request, *args, **kwargs):

# @swagger_auto_schema(method='GET', pagination_class=PageNumberPagination, \
#                      paginator_inspectors=[LimitOffsetPaginatorInspectorClass],\
#                      manual_parameters=[openapi.Parameter('page', openapi.IN_QUERY, type="openapi.TYPE_INTEGER")], \
#                      # responses={200: openapi.Response("Success:", VideoSerializer(many=True))},
#                      )
# @swagger_auto_schema(method='POST', \
#                      request_body=openapi.Schema(
#                          type=openapi.TYPE_OBJECT,
#                          required=['title', 'description', 'category_id'],
#                          properties={
#                              'source': openapi.Schema(type=openapi.TYPE_STRING),
#                              'platform_id': openapi.Schema(type=openapi.TYPE_STRING),
#                              'title': openapi.Schema(type=openapi.TYPE_STRING),
#                              'description': openapi.Schema(type=openapi.TYPE_STRING),
#                              'category_id': openapi.Schema(type=openapi.TYPE_INTEGER),
#                          },
#                      ), \
#                      responses={200: openapi.Response("Success:", VideoSerializer(many=True))}, )
# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticatedOrReadOnly])
# def get_post_videos(request):
#     # TODO generate user specific list
#     if request.method == 'GET':
#         # if logged in:
#         if 1:
#             videos = Video.objects.all()
#             paginator = LimitOffsetPaginatorInspectorClass()
#             # paginator = PageNumberPagination()
#             paginator.page = int(request.GET.get('page', 1))
#             p = paginator.paginate_queryset(videos, request)
#             videoSerializer = VideoSerializer(p, many=True)
#
#             # print("===========", videoSerializer.data)
#             # return Response(videoSerializer.data)
#             return paginator.get_paginated_response(videoSerializer.data)
#     elif request.method == 'POST':
#         # TODO
#         return Response({})
#
#
# @swagger_auto_schema(methods=['GET', 'PUT'], \
#                      responses={
#                          200: openapi.Response("Success:", VideoSerializer),
#                      }, )
# @swagger_auto_schema(method='DELETE', \
#                      responses={
#                          200: openapi.Response("Deleted successfully:", VideoSerializer),
#                      }, )
# @api_view(['GET', 'DELETE', 'PUT'])
# @permission_classes([IsAuthenticatedOrReadOnly])
# def get_delete_update_video(request, id):
#     try:
#         video = Video.objects.get(id=id)
#     except Video.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         videoSerializer = VideoSerializer(video)
#         return Response(videoSerializer.data)
#     elif request.method == 'DELETE':
#         videoSerializer = VideoSerializer(video)
#         video.delete()
#         return Response({"Deleted successfully:": videoSerializer.data},status=status.HTTP_200_OK)
#     elif request.method == 'PUT':
#         # TODO
#         return Response({})
