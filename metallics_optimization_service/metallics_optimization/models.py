from django.db import models
from django.urls import reverse


# Create your models here.

class Chemical(models.Model):
    """
    class for chemical
    """

    # DATABASE FIELDS
    name = models.CharField(max_length=128)

    # MANAGERS
    objects = models.Manager()

    # META CLASS
    class Meta:
        verbose_name = 'chemical'
        verbose_name_plural = 'chemicals'

    # TO STRING METHOD
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('chemical_details', kwargs={'pk': self.id})


class ChemicalComposition(models.Model):
    """
    class for chemical compositions
    """
    # DATABASE FIELDS
    element = models.ForeignKey(Chemical, on_delete=models.CASCADE, related_name='chemical_compositions')
    percentage = models.DecimalField(max_digits=19, decimal_places=2)

    # META CLASS
    class Meta:
        verbose_name = 'chemical_composition'
        verbose_name_plural = 'chemical_compositions'

    # TO STRING METHOD
    def __str__(self):
        return "Chemical {} with percentage {}".format(self.element, self.percentage)


class Commodity(models.Model):
    """
    class for commodity
    """
    # DATABASE FIELDS
    name = models.CharField(max_length=128)
    inventory = models.DecimalField(max_digits=19, decimal_places=2)
    price = models.DecimalField(max_digits=19, decimal_places=2)
    chemical_composition = models.ManyToManyField(ChemicalComposition, related_name='commodities')

    # META CLASS
    class Meta:
        verbose_name = 'commodity'
        verbose_name_plural = 'commidities'

    # TO STRING METHOD
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('commodity_details', kwargs={'pk': self.id})
