from django.db import models

class Place(models.Model):
    name = models.CharField("アイテム配置場所", max_length=20, null=False)
    def __str__(self):
    	return f"{self.name}"

class Large_class(models.Model):
	Lc_choices = (("OW",'One-Weapons'), ("AM",'Armors'), ("TW",'Two-Weapons'), ("AC",'Accessories'))
	name = models.CharField(
		"大分類", max_length=20, choices=Lc_choices, default="Armors", null=False
	)
	def __str__(self):
		return f"{self.name}"

class Small_class(models.Model):
	Sc_choices = (
		('Helm','Helm'), ('Shoulders','Shoulders'), ('Armor','Armor'), ('Pants','Pants'), ('Gloves','Gloves'), ('Boots','Boots'), ('Belt','Belt'), ('Ring','Ring'), ('Amulet','Amulet'), ('Medal','Medal'), ('One-gun','One-gun'), ('Two-gun','Two-gun'), ('One-sword','One-sword'), ('Two-sword','Two-sword'), ('One-mace','One-mace'), ('Two-mace','Two-mace'), ('One-ax','One-ax'), ('Two-ax','Two-ax'), ('One-scepter','One-scepter'), ('One-dagger','One-dagger'), ('Shield','Shield'), ('Off-hand','Off-hand')
	)
	name = models.CharField(
		"小分類", max_length=20, choices=Sc_choices, default="Helm", null=False
	)
	parent_class = models.ForeignKey(
		Large_class, on_delete=models.SET_NULL, null=True
	)
	def __str__(self):
		return f"{self.name}"

class Itemset(models.Model):
	name = models.CharField("セット名", max_length=128, default="")
	is_lv94 = models.BooleanField("要求レベル94", default=True)
	contained_parts = models.CharField("含まれる部位", max_length=128, default="")
	def __str__(self):
		return f"{self.name}"

class Item(models.Model):
	item_place = models.ForeignKey(
		Place, on_delete=models.SET_NULL, null=True
	)
	name = models.CharField("アイテム名", max_length=128, default="")
	item_small_class = models.ForeignKey(
		Small_class, on_delete=models.SET_NULL, null=True
	)
	item_large_class = models.ForeignKey(
		Large_class, on_delete=models.SET_NULL, null=True
	)
	is_set = models.BooleanField("セット装備", default=False)
	set_name = models.CharField("セット名", max_length=128, default="", blank=True)
	belonged_set = models.ForeignKey(
		Itemset, related_name = "owned_parts_ITEMLIST",
		on_delete=models.SET_NULL, null=True, blank=True
	)
	def __str__(self):
		return f"{self.name} ({self.item_small_class}) at {self.item_place}"