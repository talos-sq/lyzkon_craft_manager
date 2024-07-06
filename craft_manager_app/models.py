from django.db import models

from django.db import models


class LabStation(models.Model):
    name = models.CharField(max_length=64, verbose_name="Nazwa laboratorium")
    flat_flask = models.IntegerField(verbose_name="Kolba okrągła z płaskim dnem", default=0)
    conical_flask = models.IntegerField(verbose_name="Kolba stożkowa", default=0)
    pipette = models.IntegerField(verbose_name="Pipeta", default=0)
    test_tube = models.IntegerField(verbose_name="Próbówka", default=0)
    beaker = models.IntegerField(verbose_name="Zlewka", default=0)
    threaded_bottle = models.IntegerField(verbose_name="Butla z gwintem", default=0)
    cylinder_with_spigot = models.IntegerField(verbose_name="Butla z króćcem", default=0)
    crystalizer = models.IntegerField(verbose_name="Krystalizator", default=0)
    funnel = models.IntegerField(verbose_name="Lejek", default=0)
    petri_dish = models.IntegerField(verbose_name="Szalka Petriego", default=0)
    watch_glass = models.IntegerField(verbose_name="Szkło zegarowe", default=0)
    high_cylinder_with_plug = models.IntegerField(verbose_name="Cylinder wysoki z korkiem", default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Laboratorium"
        verbose_name_plural = "Laboratoria"
