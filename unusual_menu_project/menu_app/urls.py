from django.urls import path
from menu_app.views import main_view, empty

urlpatterns = [
    path('', empty, name='empty'),
    path('<path:path>', main_view, name='main'),
]
