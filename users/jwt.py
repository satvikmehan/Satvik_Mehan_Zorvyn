from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.exceptions import AuthenticationFailed


class CustomTokenSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)

        # ✅ Check AFTER authentication
        if not self.user.is_active:
            raise AuthenticationFailed("User account is inactive")

        # ✅ Add role to response
        data['role'] = self.user.role

        return data

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # ✅ Add role inside token
        token['role'] = user.role

        return token


class CustomTokenView(TokenObtainPairView):
    serializer_class = CustomTokenSerializer