from django.contrib.gis.db import models


class Inmueble(models.Model):
    build_status = models.IntegerField(blank=False)
    is_active = models.BooleanField(blank=False)
    start_month = models.IntegerField(blank=False)
    construction_type = models.IntegerField(blank=False)
    date_diff = models.TextField(blank=False)
    description = models.TextField(blank=True)
    date_in = models.DateTimeField(blank=False)
    property_type = models.IntegerField(blank=False)
    end_week = models.IntegerField(blank=False)
    typology_type = models.IntegerField(blank=False)
    coordinates = models.PointField(blank=False)
    boundary_id = models.IntegerField(blank=False)
    id_uda = models.TextField(blank=False)
    title = models.TextField(blank=True)
    listing_type = models.IntegerField(blank=False)
    date_out = models.DateTimeField(blank=False)
    start_week = models.IntegerField(blank=False)
    end_quarter = models.IntegerField(blank=False)
    last_activity = models.IntegerField(blank=False)
    start_quarter = models.IntegerField(blank=False)
    end_month = models.IntegerField(blank=False)


