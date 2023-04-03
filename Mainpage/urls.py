from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('',views.Homepage,name="Homepage"),
    path('about/',views.AboutPage,name="AboutPage"),
    path('designs/',views.DesignPage,name="DesignPage"),
    path('profile/',views.ProfilePage,name="ProfilePage"),
    path('add-design/',views.AddDesignPage,name="AddDesignPage"),
    path('mydesign/<id>/',views.MyDesignPage,name="MyDesignPage"),
    path('user-info/<id>/',views.UserInformation,name="UserInformation"),
    path('all-user/',views.All_User,name="All_User"),
    path('appointments/',views.Appointments,name="Appointments"),
    path('pending-app/',views.PendingAppointment,name="PendingAppointment"),
    path('edit-profile/',views.Edit_Profile,name='Edit_Profile'),
    path('contact/',views.ContactPage,name="ContactPage"),
    path('main-user-info/<id>',views.MainUserInfo,name="MainUserInfo"),
    path('checkout/',views.Checkout,name='Checkout'), # type: ignore
    path('success/',views.success_page,name="success_page"),
    path('cancle/',views.cancle_page,name="cancle_page"),
    path('logout/',views.Logout,name="Logout"),
    path('contract-status/',views.Contract_Status,name="Contract_Status"), # type: ignore
    path('add-payment/',views.PaymentManager,name="PaymentManager"), # type: ignore
    path('paymentsuccess/',views.Paymentsuccess,name="Paymentsuccess"),
    path('payment-checkout/',views.PaymentCheckout,name="PaymentCheckout"), # type: ignore
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATICFILES_DIRS)
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)