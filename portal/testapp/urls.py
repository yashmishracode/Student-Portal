from django.urls import path
from testapp import views

urlpatterns = [
    path('test/',views.test),
]
