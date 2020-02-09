from django.urls import path
from . import views

urlpatterns = [
    path('',views.user_login,name='user_login'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('logout/',views.user_logout,name='user_logout'),
    path('createinternalletter/',views.internal_creation_form,name='internal_letter_form'),
    path('createexternalletter/',views.external_creation_form,name='external_letter_form'),
    path('edit_external/<letter_id>',views.edit_external,name='edit_external'),
    path('edit_internal/<letter_id>',views.edit_internal,name='edit_internal'),
]
