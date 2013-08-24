from rest_framework import routers


class NestedRouter(routers.DefaultRouter):
    """
    Custom router which hides nested URLs as they cannot be reversed.
    """

    def get_api_root_view(self):
        """
        Return a view to use as the API root.

        Ignores any URLs which do not reverse correctly.
        """

        from django.core.urlresolvers import NoReverseMatch
        from rest_framework import views
        from rest_framework.response import Response
        from rest_framework.urlresolvers import reverse

        api_root_dict = {}

        list_name = self.routes[0].name

        for prefix, viewset, basename in self.registry:
            api_root_dict[prefix] = list_name.format(basename=basename)

        class APIRoot(views.APIView):
            _ignore_model_permissions = True

            def get(self, request, format=None):
                ret = {}

                for key, url_name in api_root_dict.items():
                    try:
                        ret[key] = reverse(url_name, request=request,
                                           format=format)
                    except NoReverseMatch:
                        pass

                return Response(ret)

        return APIRoot.as_view()
