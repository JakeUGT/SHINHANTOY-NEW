from django.urls import path
from . import views
# .(점) = 현재폴더 안에(있는 VIEWS)


urlpatterns = [
    path("", views.OrderListView.as_view()),
]

