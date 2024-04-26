from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as vs
from . import views

app_name='api'

router=DefaultRouter()
router.register('products',views.ProductViewsets)
router.register('categories',views.CategoryViewsets)
router.register('reviews',views.ReviewViewsets)
router.register('users',views.UserViewsets)

urlpatterns = [
    path('',include(router.urls)),
    path('api-token-auth/', vs.obtain_auth_token)
]