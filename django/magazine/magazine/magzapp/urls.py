from django.urls import path
from .views import *


urlpatterns = [
    path('signup/', signupuser, name='signupuser'),
    path('login/', loginuser, name='loginuser'),
    path('logout/', logoutuser, name='logoutuser'),

    path('home/', homepage, name='homepage'),
    path('list/', magazine_list, name='magazine_list'),
    path('profile/', view_profile, name='view_profile'),
    path('profile/edit', edit_profile, name='edit_profile'),
    path('profile/change_password', change_password, name='change_password'),
    path('sublist/', subscription_list, name='subscription_list'),
    path('cart/', cart, name='cart'),
    path('search/',SearchBook.as_view(),name='search'),

    path('emag/', entermagazine, name='entermagazine'),
    path('esup/', entersupplier, name='entersupplier'),
    path('efreq/', enter_reference_frequency, name='enter_reference_frequency'),

    path('cart/<int:mag_id>', status1, name='cart'),
    path('pay/', status2, name='pay'),
    path('unsub/<int:mag_id>', status3, name='unsubscribe'),
    path('magazine/<int:mag_id>', display, name='magazine'),
]
