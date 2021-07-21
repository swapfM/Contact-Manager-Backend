from accounts.models import User, Contact
from accounts.api.serializers import LoginSerializer, RegisterSerializer, UserSerializer, ContactsSerializer
from knox.models import AuthToken
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly


class LoginAPI(generics.GenericAPIView):
	serializer_class = LoginSerializer

	def post(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = serializer.validated_data
		return Response({
			'user': UserSerializer(user).data,
			'token': AuthToken.objects.create(user)[1]
		})


class RegisterAPI(generics.GenericAPIView):
	serializer_class = RegisterSerializer

	def post(self, request, *args, **kwargs):

		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = serializer.save()

		return Response({
			'user': UserSerializer(user).data,
			'token': AuthToken.objects.create(user)[1]
		})


class UserAPI(generics.RetrieveAPIView):
	permission_classes = [
		permissions.IsAuthenticated
	]
	serializer_class = UserSerializer

	def get_object(self):
		self.request.user


class ContactList(generics.ListCreateAPIView):
	queryset = Contact.objects.all()
	serializer_class = ContactsSerializer
	permission_classes = [permissions.IsAuthenticated]

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

	def get_queryset(self):
		owner_queryset = self.queryset.filter(owner=self.request.user)
		return owner_queryset


class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Contact.objects.all()
	serializer_class = ContactsSerializer
	permission_classes = [permissions.IsAuthenticated]


	def get_queryset(self):
		owner_queryset = self.queryset.filter(owner=self.request.user)
		return owner_queryset



