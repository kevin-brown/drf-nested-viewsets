try:
    from django.conf.urls import include, patterns, url
except ImportError:
    from django.conf.urls.defaults import include, patterns, url


def test_view(request):
    pass


def test_nested_view(request):
    pass


urlpatterns = patterns('',
    url(r"(?P<something>\w+)/(?P<pk>\w+)/$", test_nested_view,
        name="test_nested_view"),
    url(r"(?P<pk>\w+)/$", test_view, name="test_view"),
)
