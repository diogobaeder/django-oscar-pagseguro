# -*- coding: utf-8 -*-
from django.urls import *

from .views import SuccessResponseView

urlpatterns = [
    path('preview/<int:basket_id>/',
         SuccessResponseView.as_view(preview=True),
         name='pagseguro-success-response'),
    path('checkout/payment-details/',
         SuccessResponseView.as_view(preview=True),
         name='pagseguro-success-response'),
    path('checkout/preview/',
         SuccessResponseView.as_view(preview=True),
         name='pagseguro-success-response'),
    path('retorno/pagseguro/', include('pagseguro.urls')),
]
