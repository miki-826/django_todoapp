from django.urls import path
from . import views
from .views import taskcreate,Tasklist , taskdetail,taskupdate,deletetask,tasklistloginview,registertodoapp
from django.contrib.auth.views import LogoutView

urlpatterns=[

    path("" , views.Tasklist.as_view(),name="tasks"),
    path("task/<int:pk>/",taskdetail.as_view(),name="task"),
    path("create_task/",taskcreate.as_view(),name="create_task"),
    path("edit_task/<int:pk>/",taskupdate.as_view(),name="edit_task"),
    path("delete_task/<int:pk>/", deletetask.as_view(),name="delete_task"),
    path("login/", tasklistloginview.as_view(),name="login"),
    path("logout/", LogoutView.as_view(next_page="login"),name="logout"),
    path("register/", registertodoapp.as_view(),name="register")
]
