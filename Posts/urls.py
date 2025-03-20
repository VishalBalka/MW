from django.urls import path
from Posts import views

urlpatterns = [
    path('helloworld',views.helloworld)
]