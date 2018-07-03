from market.customize import cust_vals

import os
import sys

def customization(request):
    """
    Adds the customization variables to the request.
    """

    # Check that if a logo has been specified, the file exists.
    if cust_vals['c_logo'] and not os.path.isfile(cust_vals['c_logo_path']):
        sys.stderr('Error: File for logo does not exist at ' + cust_vals['c_logo_path'] + '\nUsing text logo instead.')
        cust_vals['c_logo'] = False
    return cust_vals

def user_profile(request):
    """
    Adds the UserProfile (or a Falsy value for anonymous users) to context.
    See: UserProfileMiddleware
    """
    return {
        'profile': request.profile
    }
