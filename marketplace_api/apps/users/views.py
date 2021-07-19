from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.views import Token
from rest_framework.authtoken.views import ObtainAuthToken

from apps.users.api.serializers import UserTokenSerializer

class Login(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        # print(request.user)
        login_serializer = self.serializer_class(data=request.data, context={'request': request})

        if login_serializer.is_valid():
            # print("Pasó validación")
            print(login_serializer.validated_data['user'])
            user = login_serializer.validated_data['user']
            if user.is_active:
                token, created = Token.objects.get_or_create(user=user)
                user_serializer = UserTokenSerializer(user)
                if created:
                    return Response({
                        'token': token.key,
                        'user': user_serializer.data,
                        'message': 'Inicio de sesión exitoso,'
                    }, status=status.HTTP_201_CREATED)
                else:
                    token.delete()
                    token = Token.objects.create(user=user)
                    return Response({
                        'token': token.key,
                        'user': user_serializer.data,
                        'message': 'Inicio de sesión exitoso,'
                    }, status=status.HTTP_201_CREATED)
            else:
                return Response({'mensaje': 'Este usuario no puede iniciar sesión'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error': 'Nombre de usuario o contraseña incorrectos.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'mensaje': 'Hola desde authtoken'}, status=status.HTTP_200_OK)
