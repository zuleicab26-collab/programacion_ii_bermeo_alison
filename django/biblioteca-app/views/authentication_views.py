from django.contrib.auth.views import LoginView, LogoutView

class BibliotecaLoginView(LoginView):
    template_name = 'authentication/login.html'
    redirect_authenticated_user = True

class BibliotecaLogoutView(LogoutView):
    template_name = 'authentication/logout.html'
    next_page = 'home'