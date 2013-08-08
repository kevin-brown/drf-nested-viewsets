from .views import FakeView


class FakeSerializer(object):
    context = {
        "view": FakeView()
    }
