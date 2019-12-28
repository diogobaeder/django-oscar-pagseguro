# -*- coding: utf-8 -*-
from django.urls import *

from .views import SuccessResponseView

urlpatterns = [
    path(r'^preview/(?P<basket_id>\d+)/$',
         SuccessResponseView.as_view(preview=True),
         name='pagseguro-success-response'),
    path(r'^checkout/payment-details/$',
         SuccessResponseView.as_view(preview=True),
         name='pagseguro-success-response'),
    path(r'^checkout/preview/$',
         SuccessResponseView.as_view(preview=True),
         name='pagseguro-success-response'),
    path(r'^retorno/pagseguro/', include('pagseguro.urls')),
]
