from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('main',views.main, name= 'main'),
    path('savedrawing', views.saveDrawing, name = "saveDrawing"),
    path('exec_model', views.exec_model, name = "exec_model"),
    path('loaddrawing/<int:drawingID>/', views.loadDrawing, name = "loadDrawing")
]
