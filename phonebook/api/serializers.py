from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField,
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
    full_name = SerializerMethodField()
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
            'full_name',
            'phone_number',
            'email',
            'location',
            'emergency_contact',
            # 'delete_url',
        ]

    def get_full_name(self, object):
        return '{} {}'.format(object.first_name, object.last_name)


class ContactDetailSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = [
            'first_name',
            'last_name',
            'phone_number',
            'email',
        ]
