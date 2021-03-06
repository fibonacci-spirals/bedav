from django.contrib.gis.db import models

class Locality(models.Model):
  id = models.IntegerField(primary_key=True)
  name = models.CharField(max_length=200)
  state = models.CharField(max_length=200)
  country = models.CharField(max_length=200, default="India")

  class Meta:
    db_table = "Locality"

class Hospital(models.Model):
  name = models.CharField(max_length=200)
  website = models.CharField(max_length=3000, null=True)
  phone = models.CharField(max_length=20, null=True)
  location = models.PointField(geography=True, srid=4326, null=True, verbose_name="Location")
  city = models.CharField(max_length=200, null=True)
  district = models.CharField(max_length=200, null=True)
  state = models.CharField(max_length=200, null=True)
  country = models.CharField(max_length=200, default="India", null=True)
  postal_code = models.IntegerField(null=True)
  place_id = models.CharField(max_length=1000, null=True)
  address = models.CharField(max_length=1000, null=True)
  category = models.CharField(max_length=200, null=True) #gov hos, gov med, pri hos, pri med, covid
  locality = models.ForeignKey(Locality, on_delete=models.DO_NOTHING, null=True)

  class Meta:
    db_table = "Hospitals"

class Beds(models.Model):
  branch = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='beds')
  available = models.PositiveIntegerField()
  total = models.PositiveIntegerField()
  time = models.FloatField()

  class Meta:
    db_table = "Beds"

class ICU(models.Model):
  branch = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='ICU')
  available = models.PositiveIntegerField()
  total = models.PositiveIntegerField()
  time = models.FloatField()

  class Meta:
    db_table = "ICU"

class Ventilators(models.Model):
  branch = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='ventilators')
  available = models.PositiveIntegerField()
  total = models.PositiveIntegerField()
  time = models.FloatField()

  class Meta:
    db_table = "Ventilators"



class Equipment(models.Model):
  branch = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='equipment')
  category = models.CharField(max_length=200) # gen, HDU, ICU, vent
  available = models.PositiveIntegerField()
  total = models.PositiveIntegerField()
  time = models.FloatField()

  class Meta:
    db_table = "Equipment"
