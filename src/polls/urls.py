from django.urls import path
from debug_toolbar.toolbar import debug_toolbar_urls
from . import views

# Se usa para poder diferenciar los nombres de las urls, se recomienda con proyectos muy grandes.
app_name = "polls"

urlpatterns = [
    # Las urls para las vistas genericas debido a que las vistas ya creadas (index, detail y results),
    # son pequeñas y se pueden usar vistas genericas de Django.
    # Se cambia de question_id a pk.
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
