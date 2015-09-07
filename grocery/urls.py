from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from app.customer import views as customer_views
from app.merchant import views as merchant_views

urlpatterns = patterns('',
    ('^index/$', customer_views.index),
    ('^login/$', customer_views.loginUser),
    ('^logout/$', customer_views.logoutUser),
    ('^create/$', customer_views.newAccount),
    ('^main/$', customer_views.main),
    ('^getCategories/$', customer_views.getCategories),
    ('^myInfo/$',customer_views.myInfo),
    ('^user/update/([\w]+)$',customer_views.updateUser),
                # cid/     p/     query
    ('^search/([\d\w]+)/([\d]+)/([\w\W]*)$',customer_views.search),
    ('^product/([\d\w]+)$', customer_views.getProduct),
    ('^getCart/$',customer_views.viewCart),
    ('^cart/add/([\d\w]+)/([\d]+)$',customer_views.addToCart),
    ('^cart/delete/([\d\w]+)$', customer_views.deleteFromCart),
    ('^cart/update/([\d\w]+)/([\d]+)$', customer_views.updateCart),
    #('^cart/checkout/$', customer_views.checkoutCart),
    ('^cart/checkout/shippinginfo$', customer_views.shippinginfo),
    ('^cart/checkout/shippingoption$', customer_views.shippingoption),
    ('^cart/checkout/submitOrder$', customer_views.submitOrder),
    ('^orderInfo/([\d\w]+)/$', customer_views.getOrderDetails),
    ('^merchant/index/$', merchant_views.merchantIndex),
    ('^merchant/login/$', merchant_views.merchantLoginUser),
    ('^merchant/logout/$', merchant_views.merchantLogoutUser),
    ('^merchant/create/$', merchant_views.merchantNewAccount),
    ('^merchant/main/$', merchant_views.merchantMain),
    ('^merchant/mCreate/$', merchant_views.createManufacturer),
    ('^merchant/pCreate/$', merchant_views.createProduct),
    ('^merchant/viewAll/$', merchant_views.viewProducts),
    ('^merchant/update/product/([\w]+)/([\d\w]+)$', merchant_views.updateProduct),
    ('^merchant/product/delete/([\d\w]+)$', merchant_views.deleteProduct),
    ('^merchant/upload/product/icon/([\d\w]+)$', merchant_views.uploadIcon),
    ('^product/icon/([\d\w]+)$', merchant_views.getIcon),
)
