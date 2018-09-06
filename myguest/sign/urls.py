#coding:utf-8

from django.conf.urls import url
from sign import views_if
from sign import views_if_sec

urlpatterns=[
    # sign system interface:
    # ex:/api/add_event/
    #添加发布会
    url(r'^add_event/',views_if.add_event,name='add_event'),
    # ex:/api/add_guest/
    #添加guest
    url(r'^add_guest/',views_if.add_guest,name='add_guest'),
    # ex:/api/get_event_list/
    #查询发布会
    url(r'^get_event_list/',views_if.get_event_list,name='get_event_list'),
    # ex:/api/get_guest_list/
    #查询guest
    url(r'^get_guest_list/',views_if.get_guest_list,name='get_guest_list'),
    # ex:/api/user_sign/
    #发布会签到
    url(r'^user_sign/',views_if.user_sign,name='user_sign'),

    #查询发布会-带用户认证
    url(r'^sec_get_event_list/', views_if_sec.sec_get_event_list, name='sec_get_event_list'),
    #添加发布会-----增加签名+时间戳
    url(r'^sec_add_event/',views_if_sec.sec_add_event,name='sec_add_event'),
]