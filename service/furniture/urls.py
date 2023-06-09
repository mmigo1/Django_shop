from django.urls import path

from furniture.views import *

urlpatterns = [
    path('', index, name='index'),

    path('list/', FurnitureListView.as_view(), name='furn_list'),
    path('<int:furniture_id>', FurnitureDetailView.as_view(), name='furn_info'),
    path('add/', FurnitureCreateView.as_view(), name='furn_add'),
    path('edit/<int:pk>', FurnitureUpdateView.as_view(), name='furn_edit'),
    path('del/<int:pk>', FurnitureDeleteView.as_view(), name='furn_del'),

    path('email/', contact_email, name='contact_email'),
    path('registration/', user_registration, name='regis'),

    path('login/', user_login, name='log in'),
    path('logout/', user_logout, name='log out'),

    path('api/list', furniture_api_list, name='furn_api_list'),
    path('api/detail/<int:pk>', furniture_api_detail, name='furn_api_detail'),
]
