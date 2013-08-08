from django.test import TestCase
from rest_nested_viewsets.fields import NestedRelatedField
from ..models import FakeModel
from ..serializers import FakeSerializer


class RelatedFieldTests(TestCase):

    def test_no_extra_args(self):
        field = NestedRelatedField(view_name="test_view")

        self.assertEqual(field.map, {})

    def test_maps_set(self):
        field = NestedRelatedField(view_name="test_view", map={"pk": "abc"})

        self.assertEqual(field.map, {"pk": "abc"})

    def test_get_url_no_map(self):
        field = NestedRelatedField(view_name="test_view")
        field.parent = FakeSerializer()

        url = field.get_url(FakeModel(1), "test_view", None, None)

        self.assertEqual(url, "/1/")

    def test_get_url_with_map_match(self):
        field = NestedRelatedField(view_name="test_nested_view", map={
            "something": "pk",
        })
        field.parent = FakeSerializer()
        field.parent.context["view"].kwargs["pk"] = "123"

        url = field.get_url(FakeModel(1), "test_nested_view", None, None)

        self.assertEqual(url, "/123/1/")
