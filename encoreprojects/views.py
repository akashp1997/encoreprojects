from django.contrib.auth import views


def login(request, *args, **kwargs):
    """Override login to include remember me option"""
    if request.method == 'POST':
        if not request.POST.get('rememberMe', False):
            request.session.set_expiry(0)
    return views.LoginView.as_view()(
        request, *args, **kwargs,
        redirect_authenticated_user=True
    )
