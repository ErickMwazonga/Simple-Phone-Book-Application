from phonebook.models import Contact
from .serializers import (
    ContactCreateSerializer,
    ContactDetailSerializer,
    ContactListSerializer,
)
from .pagination import ContactLimitOffsetPagination
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView
)
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)
from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
)


class ContactCreteAPIView(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactCreateSerializer


class ContactListAPIView(ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['first_name', 'last_name', 'email', 'location']
    # pagination_class = LimitOffsetPagination
    pagination_class = ContactLimitOffsetPagination


class ContactRetrieveAPIView(RetrieveAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactDetailSerializer


class ContactDeleteAPIView(DestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactListSerializer


class ContactUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactListSerializer
