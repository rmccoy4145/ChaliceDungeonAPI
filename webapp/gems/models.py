from django.db import models
# Create your models here.

class GemLocation(models.Model):

    dungeon_type_choices = (
        ("Pthumeru Ihyll", "Pthumeru Ihyll"),
        ("Lower Loran", "Lower Loran"),
        ("Isz", "Isz"),
        ("Ailing Loran", "Ailing Loran"),
        ("Pthumerian Defilement", "Pthumerian Defilement")
    )

    shape_choices = (
        ("Radial", "Radial"),
        ("Triangle", "Triangle"),
        ("Waning", "Waning")
    )

    gem_type_choices = (
        ("Tempering", "Tempering"),
        ("Fire", "Fire"),
        ("Fire Abyssal", "Fire Abyssal"),
        ("Nourishing", "Nourishing"),
        ("Nourishing Abyssal", "Nourishing Abyssal"),
        ("Beast/Kin Hunter", "Beast/Kin Hunter"),
        ("Heavy Abyssal", "Heavy Abyssal"),
        ("Cold Abyssal", "Cold Abyssal"),
        ("Tempering/Fire/Bolt", "Tempering/Fire/Bolt"),
        ("Physical/Fire/Bolt/Arcane", "Physical/Fire/Bolt/Arcane"),
        ("Adept (Blunt/Thrust)", "Adept (Blunt/Thrust)"),
        ("Arcane", "Arcane"),
        ("Odd Arcane", "Odd Arcane"),
        ("Arcane Abyssal", "Arcane Abyssal"),
        ("Bolt", "Bolt"),
        ("Fire", "Fire"),
        ("Odd Bolt", "Odd Bolt"),
        ("Bloodtinge", "Bloodtinge"),
        ("Pulsing", "Pulsing")
    )

    rarity_choices = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10),
        (11, 11),
        (12, 12),
        (13, 13),
        (14, 14),
        (15, 15),
        (16, 16),
        (17, 17),
        (18, 18),
        (19, 19),
        (20, 20)
    )

    layer_choices = (
        (1, 1),
        (2, 2),
        (3, 3)
    )

    glyph = models.CharField(max_length=255)
    dungeon_type = models.CharField(max_length=255, choices=dungeon_type_choices)
    fetid = models.BooleanField()
    rotten = models.BooleanField()
    cursed = models.BooleanField()
    shape = models.CharField(max_length=255, choices=shape_choices)
    gem_type = models.CharField(max_length=255, choices=gem_type_choices)
    first_effect = models.CharField(max_length=255)
    second_effect = models.CharField(max_length=255)
    third_effect = models.CharField(max_length=255)
    rarity = models.IntegerField(choices=rarity_choices)
    layer = models.IntegerField(choices=layer_choices)
    notes = models.CharField(max_length=255)

    def __str__(self):
        return "glyph = {}, dungeon = {}, shape = {}, gem_type = {}, first_effect = {}, second_effect = {}, " \
               "third_effect = {}".format(self.glyph, self.dungeon_type, self.shape, self.gem_type, self.first_effect,
                      self.second_effect, self.third_effect)
