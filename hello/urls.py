from django.urls import path 
from . import views

urlpatterns =[
    path('', views.index, name='index'),
    # path('next', views.next, name="next"),
    # path('form', views.form, name='form'),
    # path('my_name_is_<nickname>.I_am_<int:age>_years_old.', views.index, name='index'), #うらる直書きで設定できる。クエリパラメータよりスマートだね。
    ]

