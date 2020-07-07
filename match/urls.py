from django.urls import path
from . import views

urlpatterns = [
    path('before_home',views.before_home,name='before_home'),
    path('home',views.home,name='home'),
    path('message',views.message,name='message'),
    path('profile_create',views.profile_create,name='profile_create'),
    path('profile',views.profile,name='profile'),
    path('other_profile/<int:num>',views.other_profile,name='other_profile'),
    path('profile_edit',views.profile_edit,name='profile_edit'),
    path('recruit_create',views.recruit_create,name='recruit_create'),
    path('recruit',views.recruit,name='recruit'),
    path('recruit_edit/<int:num>',views.recruit_edit,name='recruit_edit'),
    path('recruit_delete/<int:num>',views.recruit_delete,name='recruit_delete'),
    path('skill_delete/<int:num>',views.skill_delete,name='skill_delete'),
    path('other_recruit/<int:num>',views.other_recruit,name='other_recruit'),
    path('search',views.search,name='search'),
    path('term',views.term,name='term'),
    path('privacy',views.privacy,name='privacy'),
    path('inquiry',views.inquiry,name='inquiry'),
    #path('callback/',views.callback,name='callback')
]