from django.shortcuts import render
from django.http import Http404
from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

from .models import Chemical, Commodity, ChemicalComposition
from .serializers import ChemicalSerializer, CommoditySerializer, \
    ChemicalCompositionSerializer

from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view




class CustomPagination(PageNumberPagination):
    page_size = 1


# Class based views

# class ChemicalList(APIView):
#     """
#     class based view for chemical list
#     """
#
#     def get(self, request):
#         chemicals = Chemical.objects.all()
#         serializer = ChemicalSerializer(chemicals, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = ChemicalSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class ChemicalDetail(APIView):
#     """
#     class based view for chemical details
#     """
#
#     def get_object(self, pk):
#         try:
#             return Chemical.objects.get(pk=pk)
#         except Chemical.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk):
#         university = self.get_object(pk)
#         serializer = ChemicalSerializer(university)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         chemical = self.get_object(pk)
#         serializer = ChemicalSerializer(chemical, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         chemical = self.get_object(pk)
#         chemical.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class CommodityList(APIView):
#       """
#         class based view for commodity list
#      """
# #     def get(self, request):
#         commodity = Commodity.objects.all()
#         serializer = CommoditySerializer(commodity, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = CommoditySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class CommodityDetail(APIView):
#     """
#     class based view for commodity details
#     """
#
#     def get_object(self, pk):
#         try:
#             return Commodity.objects.get(pk=pk)
#         except Commodity.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk):
#         university = self.get_object(pk)
#         serializer = CommoditySerializer(university)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         commodity = self.get_object(pk)
#         serializer = CommoditySerializer(commodity, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         commodity = self.get_object(pk)
#         commodity.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# Viewsets
# NOTE: I done with class based views first. Then I optimize with viewsets.

class ChemicalViewSet(viewsets.ModelViewSet):
    """
        viewset for chemical
    """

    queryset = Chemical.objects.all()
    serializer_class = ChemicalSerializer
    pagination_class = LimitOffsetPagination
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]


class CommodityViewSet(viewsets.ModelViewSet):
    """
    viewset for commodity
    """
    queryset = Commodity.objects.all()
    serializer_class = CommoditySerializer
    pagination_class = LimitOffsetPagination
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]


class ChemicalCompositionViewSet(viewsets.ModelViewSet):
    """
    viewset for chemical composition
    """
    queryset = ChemicalComposition.objects.all()
    serializer_class = ChemicalCompositionSerializer
    # pagination_class = CustomPagination
    pagination_class = LimitOffsetPagination
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
