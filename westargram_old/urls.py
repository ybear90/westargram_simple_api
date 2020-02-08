from django.urls import path
from .views import LoginView, CommentView

urlpatterns = [
    path('', LoginView.as_view()),
    path('/main', CommentView.as_view())
]
