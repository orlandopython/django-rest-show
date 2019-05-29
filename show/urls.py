from django.urls import path
from show import views

urlpatterns = [
    path('<int:pk>', views.ShowIDView.as_view()),
]