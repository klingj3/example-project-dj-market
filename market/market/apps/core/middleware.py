class UserProfileMiddleware(object):
    """
    This middleware adds the current UserProfile to the request,
    or a false value for anonymous users.

    This must be above any other middleware that depends on this information.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # Add the current UserProfile to the request
        if request.user.is_anonymous() or request.user.is_superuser:
            request.profile = None
        else:
            request.profile = request.user.profile

        response = self.get_response(request)
        return response