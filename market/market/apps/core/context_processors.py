
def user_profile(request):
    """
    Adds the UserProfile (or a Falsy value for anonymous users) to context.
    See: UserProfileMiddleware
    """
    return {
        'profile': request.profile
    }
