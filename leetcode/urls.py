from django.contrib import admin
from django.urls import path , include
from leetcode import views
urlpatterns = [
   path("" , views.index, name="index"),
   path("/leetcode" , views.leetcode, name="leetcode")
]
