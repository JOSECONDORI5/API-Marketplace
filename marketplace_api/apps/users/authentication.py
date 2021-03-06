from datetime import timedelta

from django.utils import timezone
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed

from django.conf import settings


class ExpiringTokenAuthentication(TokenAuthentication):

    # expired = False

    # Calculate token expired time
    def expires_in(self, token):
        time_elapsed = timezone.now() - token.created
        left_time = timedelta(seconds=settings.TOKEN_EXPIRED_AFTER_SECONDS) - time_elapsed
        return left_time

    # ¿Expired token?
    def is_token_expired(self, token):
        return self.expires_in(token) < timedelta(seconds=0)

    # Get time expired token
    def token_expire_handler(self, token):
        is_expire = self.is_token_expired(token)
        if is_expire:
            # self.expired = True
            # print('TOKEN EXPIRADO')
            user = token.user
            token.delete()
            token = self.get_model().objects.create(user=token.user)
        return token

    # Get credentials of token
    def authenticate_credentials(self, key):
        token, user = None, None
        try:
            token = self.get_model().objects.select_related('user').get(key=key)
            user = token.user
            token = self.token_expire_handler(token)
        except self.get_model().DoesNotExist:
            pass
        #     message = 'Token inválido.'
        #     self.expired = True
        #     # return message
        #     # raise AuthenticationFailed('Token inválido.')
        # if token is not None:
        #     if not token.user.is_active:
        #         message = 'Usuario no activo o eliminado.'
        #         # return message
        #         # raise AuthenticationFailed('Usuario no activo o eliminado.')
        #
        #     is_expired = self.token_expire_handler(token)
        #
        #     if is_expired:
        #         message = 'Su token ha expirado.'
        #         # return message
        #         # raise AuthenticationFailed('Su token ha expirado.')
        #
        # # return token.user, token
        return user
