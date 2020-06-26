try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object


class MoviesMiddleware(MiddlewareMixin):
    """

    """

    def process_request(self, request):
        pass

    def process_response(self, request, response):
        return response
