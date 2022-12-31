from knox.views import LoginView as KnoxLoginView
from rest_framework.authentication import BasicAuthentication
class LoginView(KnoxLoginView):
    """ Login view to allow basic authentication"""
    authentication_classes = [BasicAuthentication]
