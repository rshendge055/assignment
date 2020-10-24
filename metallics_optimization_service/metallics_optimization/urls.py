from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('api/v1/public/chemicals',views.ChemicalViewSet)
router.register('api/v1/public/commodities',views.CommodityViewSet)
router.register('api/v1/public/chemical_compositions', views.ChemicalCompositionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# urlpatterns = [
#     path('api/v1/public/chemical', views.ChemicalList.as_view()),
#     path('api/v1/public/chemical/<int:pk>', views.ChemicalDetail.as_view()),
#
#     path('api/v1/public/commodity', views.CommodityList.as_view()),
#     path('api/v1/public/commodity/<int:pk>', views.CommodityDetail.as_view())
#
# ]

