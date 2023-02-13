"""
Views for the user API.
"""

from rest_framework import generics

from user.serializers import UserSerializer

class CreateUserView(generics:createAPIView):
    """Create a new user in a system"""
    serializer_class = UserSerializer