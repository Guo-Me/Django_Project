from django.urls import path
from . import views
urlpatterns = [
    path('category_list/',views.category_list),
    path('category_add/',views.category_add),
]
