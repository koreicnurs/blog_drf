from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


from main.models import Post
from main.serializers import PostSerializer


@api_view()
def posts_list(request):
    queryset = Post.objects.all()
    serializer = PostSerializer(queryset, many=True, context={'request': request})
    return Response(data=serializer.data, status=status.HTTP_200_OK)








# TODO FBV
# TODO CBV
# TODO CRUD
# TODO Viewsets
# TODO Pagination
# TODO Search
# TODO Filltering
# TODO Permission
# TODO Get author from request
