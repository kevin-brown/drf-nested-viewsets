from rest_framework import serializers
from rest_nested_viewsets import fields

__all__ = ["NestedHyperlinkedModelSerializer"]


NestedHyperlinkedModelSerializer(serializers.HyperlinkedModelSerializer):
    _hyperlink_field_class = fields.NestedHyperlinkedRelatedField
    _hyperlink_identity_field_class = fields.NestedHyperlinkedIdentityField
