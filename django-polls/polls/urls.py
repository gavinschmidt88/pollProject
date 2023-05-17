from django.urls import include, path
from django.conf import settings
from django.conf.urls import include

from . import views

app_name = "polls"

urlpatterns = urlpatterns = [
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path("", views.IndexView.as_view(
         template_name='polls/templates/index.html'), name="index"),
]
