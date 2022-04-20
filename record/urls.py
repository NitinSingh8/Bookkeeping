from django.urls import path
from . import views


urlpatterns = [
    path('',views.bookeeping,name="book"),
    path('home/',views.home,name="home"),
    path('learn/',views.learn_func,name="learn"),
    path('explore/',views.explore_func,name="explore"),
    path('about/',views.about_func,name="about"),
    path('login/',views.signin_func,name="signin"),
    path('signup/',views.signup_func,name="signup"),
    path('logout/',views.logout_func,name="logout"),
    path('set_amount/',views.set_amount_func,name="set_amount"),
    path('modify_amount/<int:my_id>',views.modify_amount_func,name="modify_amount"),

]
