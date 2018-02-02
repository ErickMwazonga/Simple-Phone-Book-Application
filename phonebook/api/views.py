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
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

from phonebook.models import Contact
from .serializers import (
    ContactCreateSerializer,
    ContactDetailSerializer,
    ContactListSerializer,
)
from .pagination import ContactLimitOffsetPagination
# from .permissions import IsOwnerOrReadOnly


class ContactCreteAPIView(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactCreateSerializer
    permission_class = [IsAuthenticated]


class ContactListAPIView(ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['first_name', 'last_name', 'email', 'location']
    # pagination_class = LimitOffsetPagination
    pagination_classes = ContactLimitOffsetPagination

    # def get_queryset(self, *args, **kwargs):
        # queryset_list = super(ContactListAPIView, self).get_queryset(*args, **kwargs) 



class ContactRetrieveAPIView(RetrieveAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactDetailSerializer


class ContactDeleteAPIView(DestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactListSerializer


class ContactUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactListSerializer
    # permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

