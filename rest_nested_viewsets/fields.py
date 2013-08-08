from rest_framework.serializers import HyperlinkedIdentityField, \
HyperlinkedRelatedField


class NestedHyperlinkedField(object):
    
    base_obj = None
    
    def __init__(self, *args, **kwargs):
        self.map = kwargs.pop("map", {})
        
        super(NestedHyperlinkedField, self).__init__(*args, **kwargs)
    
    def field_to_native(self, obj, field_name):
        self.base_obj = obj
        
        return super(NestedHyperlinkedField, self).field_to_native(obj,
                                                                   field_name)
    
    def get_url(self, obj, view_name, request, format):
        from django.core.urlresolvers import NoReverseMatch
        from rest_framework.reverse import reverse
        
        try:
            return super(NestedHyperlinkedField, self).get_url(obj,
                view_name, request, format)
        except NoReverseMatch:
            pass
        
        kwargs = {
            "pk": obj.pk,
        }
        
        serializer = self.parent
        view = serializer.context["view"]
        
        for key, kwkey in self.map.iteritems():
            base_obj = self.base_obj.pk if self.base_obj else 0
            kwargs[key] = view.kwargs.get(kwkey, base_obj)
        
        url = reverse(view_name, kwargs=kwargs, request=request, format=format)
        
        return url


class NestedIdentityField(NestedHyperlinkedField,
                               HyperlinkedIdentityField):
    pass


class NestedRelatedField(NestedHyperlinkedField, HyperlinkedRelatedField):
    pass
