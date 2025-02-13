from rest_framework.views import APIView
from .serializers import UserRegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status


class UserRegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        tokens = RefreshToken.for_user(user)
        tokens = {
            "access": str(tokens.access_token),
            "refresh": str(tokens),
        }
        return Response(
            tokens,
            status=status.HTTP_201_CREATED,
        )

