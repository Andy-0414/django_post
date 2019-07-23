from .serializers import PostSerializer,LoginUserSerializer,UserSerializer
from posts.models import Post
from rest_framework import viewsets, permissions, generics
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from knox.models import AuthToken

class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class LoginView(generics.GenericAPIView):
    serializer_class = LoginUserSerializer
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response(
            {
                "user": UserSerializer(user, context=self.get_serializer_context()).data,
                "token": AuthToken.objects.create(user)[1],
            }
        )

class UserView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user