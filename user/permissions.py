from rest_framework import permissions
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.exceptions import TokenError


class RequestHelper:
    @classmethod
    def get_user_id_from_request(self, request):
        return request.META['LOGGED_IN_USER_ID']


class AppOnlyUser(permissions.BasePermission):
    def has_permission(self, request, view):
        # Implement token validations here
        # site[https://django-rest-framework-simplejwt.readthedocs.io/en/latest/rest_framework_simplejwt.html#rest_framework_simplejwt.tokens.Token]
        try:
            reqToken = request.META['HTTP_X_AUTHORIZATION'].split("Bearer ")[1]
            token = AccessToken(token=reqToken, verify=False)
            token.verify()
            tokenPayload = token.payload

            request.META['LOGGED_IN_USER_ID'] = tokenPayload['user_id']
            return True
        except TokenError as err:
            return False

    def has_object_permission(self, request, view, obj):
        # Implement object permissions
        return True
