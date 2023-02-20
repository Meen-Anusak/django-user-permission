from django.urls import path
from .views import GetPermission
urlpatterns = [
   path('', GetPermission.as_view()),

]