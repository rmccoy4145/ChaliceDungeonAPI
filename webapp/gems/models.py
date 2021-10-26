from django.db import models


# Create your models here.
class GemLocation(models.Model):
    glyph = models.CharField(max_length=255)
    dungeon_type = models.CharField(max_length=255)
    shape = models.CharField(max_length=255)
    fetid = models.BooleanField()
    rotten = models.BooleanField()
    cursed = models.BooleanField()
    shape = models.CharField(max_length=255)
    gem_type = models.CharField(max_length=255)
    first_effect = models.CharField(max_length=255)
    second_effect = models.CharField(max_length=255)
    third_effect = models.CharField(max_length=255)
    rarity = models.IntegerField()
    layer = models.IntegerField()
    notes = models.CharField(max_length=255)

    def __str__(self):
        return "glyph = {}, dungeon = {}, shape = {}, gem_type = {}, first_effect = {}, second_effect = {}, " \
               "third_effect = {}".format(self.glyph, self.dungeon_type, self.shape, self.gem_type, self.first_effect,
                      self.second_effect, self.third_effect)
