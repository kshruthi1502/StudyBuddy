from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
   path('', views.redirecthome, name='home'),
    path('home/', views.home, name='home'),
    path('login/',views.loginpage,name='login'),
    path('register/',views.register,name='register'),
    path('redirecthome/',views.redirecthome,name='availablecourse'),
    path('logout/', views.logoutUser, name="logout"), 
    path('javacourse/',views.javacourseview,name="javacourse"),
    path('about/',views.aboutview,name="about"),
    path('pythoncourse/',views.pythoncourseview,name="pythoncourse"),
    path('quizjava/',views.quizjavaview,name="quizjava"),
    path('quizpython',views.quizpythonview,name="quizpython"),
    path('profile',views.profileview,name="profile"),
    path('availcourse/',views.availcourseview,name="availcourse"),
    path('viewbook/',views.viewbookspage,name="viewbook"),
    path('viewjavabook/',views.javabookview,name="viewjavabook"),
    path('viewpythonbook/',views.pythonbookview,name="viewpythonbook"),
    path('enrollc/',views.viewenrollpage,name="enrollc"),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()