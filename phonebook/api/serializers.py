from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
)
from phonebook.models import Contact


class ContactCreateSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = [
            'first_name',
            'last_name',
            'phone_number',
            'email',
            'location',
            'emergency_contact',
        ]


contacts_detail_url = HyperlinkedIdentityField(
    view_name='api:detail',
    lookup_field='pk',
    )


class ContactListSerializer(ModelSerializer):
    url = contacts_detail_url
    # delete_url = HyperlinkedIdentityField(
    #     view_name='api:delete',
    #     lookup_field='pk',
    #     )
    class Meta:
        model = Contact
        fields = [
            'url',
            'first_name',
            'last_name',
            'phone_number',
            'email',
            'location',
            'emergency_contact',
            # 'delete_url',
        ]


class ContactDetailSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = [
            'first_name',
            'last_name',
            'phone_number',
            'email',
        ]
