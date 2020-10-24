from django.db.models import Sum
from rest_framework import serializers
from .models import Chemical, Commodity, ChemicalComposition


class ChemicalSerializer(serializers.ModelSerializer):
    """
    serializer for chemical
    """
    class Meta:
        model = Chemical
        fields = ('id', 'name')


class ChemicalCompositionSerializer(serializers.ModelSerializer):
    """
    serializer for chemical composition
    """
    element = ChemicalSerializer()

    # cal_percentage = serializers.SerializerMethodField()

    class Meta:
        model = ChemicalComposition
        fields = ('element', 'percentage')

    # def get_cal_percentage(self, obj):
    #     calculated_percentage = dict()
    #     result = ChemicalComposition.objects.filter(commodities__id=obj.id).aggregate(
    #         total_percentage=Sum('percentage'))
    #     if result.get('total_percentage'):
    #         if result.get('total_percentage') <= 100:
    #             default_chemical = {"id": "9999"+"_"+str(obj.id), "name": "Unknown"}
    #             percentage = 100 - result['total_percentage']
    #             chemical = Chemical.objects.create(**default_chemical)
    #             chemical_composition = ChemicalComposition.objects.create(chemical, percentage)
    #             #commodity = Commodity.objects.create(chemical_composition)
    #             # calculated_percentage['element'] = {"id": 9999, "name": "Unknown"}
    #             # calculated_percentage['percentage'] = 100 - result['total_percentage']
    #     # cal = Commodity.chemical_composition.add(calculated_percentage)
    #     #print(calculated_percentage)
    #     if result.get('total_percentage'):
    #         print(result['total_percentage'])
    #     return obj.percentage


class CommoditySerializer(serializers.ModelSerializer):
    """
    serializer for commodity
    """
    chemical_composition = ChemicalCompositionSerializer(many=True)

    class Meta:
        model = Commodity
        fields = (
            'id',
            'name',
            'inventory',
            'price',
            'chemical_composition'
        )
