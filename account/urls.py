from django.urls    import path
from .views         import SignUpView, SignInView, CheckAccessView

urlpatterns = [
    path('/sign-up', SignUpView.as_view()),
    path('/sign-in', SignInView.as_view()),
    path('/check-user', CheckAccessView.as_view())    
]