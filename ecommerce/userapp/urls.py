from django.urls import path,include
from . import views

app_name='userss'

urlpatterns = [
    path('',views.basePage,name='base-page' ),
    path('login/',views.log_in,name='login-url' ),
    path('logout/',views.log_out,name='logout-url' ),
    path('signup/',views.Signup,name='signup-url' ),

    path('c_prod_list/',views.customerProdList,name='customer-prod-list-url'),
    path('c_prod_list/jackets/',views.jacketsPage,name='jackets-url'),
    path('c_prod_list/shirts/',views.shirtsPage,name='shirts-url'),
    path('c_prod_list/tshirts/',views.tshirtsPage,name='tshirts-url'),
    path('c_prod_list/jeans/',views.jeansPage,name='jeans-url'),
    path('c_prod_list/shorts/',views.shortsPage,name='shorts-url'),
    path('c_prod_list/tights/',views.tightsPage,name='tights-url'),
    path('c_prod_list/trousers/',views.trousersPage,name='trousers-url'),
    path('c_prod_list/joggers/',views.joggersPage,name='joggers-url'),
    path('c_prod_list/sneakers/',views.sneakersPage,name='sneakers-url'),
    path('c_prod_list/pumps/',views.pumpsPage,name='pumps-url'),
    path('c_prod_list/heels/',views.heelsPage,name='heels-url'),

    path('c_prod_list/women/',views.womenPage,name='women-url'),
    path('c_prod_list/women/jackets/',views.womenJacketsPage,name='women-jackets-url'),
    path('c_prod_list/women/shirts/',views.womenShirtsPage,name='women-shirts-url'),
    path('c_prod_list/women/tshirts/',views.womenTshirtsPage,name='women-tshirts-url'),
    path('c_prod_list/women/jeans/',views.womenJeansPage,name='women-jeans-url'),
    path('c_prod_list/women/shorts/',views.womenShortsPage,name='women-shorts-url'),
    path('c_prod_list/women/tights/',views.womenTightsPage,name='women-tights-url'),
    path('c_prod_list/women/trousers/',views.womenTrousersPage,name='women-trousers-url'),
    path('c_prod_list/women/joggers/',views.womenJoggersPage,name='women-joggers-url'),
    path('c_prod_list/women/sneakers/',views.womenSneakersPage,name='women-sneakers-url'),
    path('c_prod_list/women/pumps/',views.womenPumpsPage,name='women-pumps-url'),
    path('c_prod_list/women/heels/',views.womenHeelsPage,name='women-heels-url'),

    path('c_prod_list/men/',views.menPage,name='men-url'),
    path('c_prod_list/men/jackets/',views.menJacketsPage,name='men-jackets-url'),
    path('c_prod_list/men/shirts/',views.menShirtsPage,name='men-shirts-url'),
    path('c_prod_list/men/tshirts/',views.menTshirtsPage,name='men-tshirts-url'),
    path('c_prod_list/men/jeans/',views.menJeansPage,name='men-jeans-url'),
    path('c_prod_list/men/shorts/',views.menShortsPage,name='men-shorts-url'),
    path('c_prod_list/men/tights/',views.menTightsPage,name='men-tights-url'),
    path('c_prod_list/men/trousers/',views.menTrousersPage,name='men-trousers-url'),
    path('c_prod_list/men/joggers/',views.menJoggersPage,name='men-joggers-url'),
    path('c_prod_list/men/sneakers/',views.menSneakersPage,name='men-sneakers-url'),
    path('c_prod_list/men/pumps/',views.menPumpsPage,name='men-pumps-url'),
    path('c_prod_list/men/heels/',views.menHeelsPage,name='men-heels-url'),

    path('c_prod_list/kids/',views.kidsPage,name='kids-url'),
    path('c_prod_list/kids/jackets/',views.kidsJacketsPage,name='kids-jackets-url'),
    path('c_prod_list/kids/shirts/',views.kidsShirtsPage,name='kids-shirts-url'),
    path('c_prod_list/kids/tshirts/',views.kidsTshirtsPage,name='kids-tshirts-url'),
    path('c_prod_list/kids/jeans/',views.kidsJeansPage,name='kids-jeans-url'),
    path('c_prod_list/kids/shorts/',views.kidsShortsPage,name='kids-shorts-url'),
    path('c_prod_list/kids/tights/',views.kidsTightsPage,name='kids-tights-url'),
    path('c_prod_list/kids/trousers/',views.kidsTrousersPage,name='kids-trousers-url'),
    path('c_prod_list/kids/joggers/',views.kidsJoggersPage,name='kids-joggers-url'),
    path('c_prod_list/kids/sneakers/',views.kidsSneakersPage,name='kids-sneakers-url'),
    path('c_prod_list/kids/pumps/',views.kidsPumpsPage,name='kids-pumps-url'),
    path('c_prod_list/kids/heels/',views.kidsHeelsPage,name='kids-heels-url'),

    path('vendor_home/',views.vendorHome,name='vendor-home-url' ),
    path('v_prod_list/',views.vendorProdList,name='vendor-prod-list-url'),
    path('v_prod_add/',views.vendorProdAdd,name='vendor-prod-add-url'),
    path('v_prod_list/v_update/<int:id>/',views.vendorProdUpdate,name='vendor-prod-update-url'),
    path('v_prod_list/v_delete/<int:id>/',views.vendorProdDelete,name='vendor-prod-delete-url'),
    path('v_orders/',views.vendorOrders,name='vendor-all-orders-url'),
    path('v_orders_by_customer/',views.vendorOrdersByCustomer,name='vendor-orders-by-customer-url'),

    path('cart/',views.cartView,name='cart-url'),
    path('checkout/',views.checkoutView,name='checkout-url'),
    path('pay/',views.payView,name='pay-url'),

    path('update_order/',views.updateOrderView,name='update-order-url'),

]
