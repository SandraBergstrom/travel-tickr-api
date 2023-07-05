from rest_framework.decorators import api_view
from rest_framework.response import Response
from .settings import (
    JWT_AUTH_COOKIE, JWT_AUTH_REFRESH_COOKIE, JWT_AUTH_SAMESITE,
    JWT_AUTH_SECURE,
)


@api_view()
# Route for API root. Responds with a welcome message
def root_route(request):
    return Response({
        "message": "Welcome to my Travel Ticker API!"
    })


# dj-rest-auth logout view fix
@api_view(['POST'])
def logout_route(request):
    # Custom logout route. Deletes JWT_AUTH_COOKIE and
    # JWT_AUTH_REFRESH_COOKIE from client.
    response = Response()

    # Set JWT_AUTH_COOKIE to an expired date,
    # effectively removing it from client.
    response.set_cookie(
        key=JWT_AUTH_COOKIE,
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )

    # Set JWT_AUTH_REFRESH_COOKIE to an expired date,
    # effectively removing it from client.
    response.set_cookie(
        key=JWT_AUTH_REFRESH_COOKIE,
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    return response
