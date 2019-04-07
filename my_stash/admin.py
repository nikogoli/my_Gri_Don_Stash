from django.contrib import admin
from .models import Place, Large_class, Small_class, Item, Itemset

admin.site.register(Place)
admin.site.register(Large_class)
admin.site.register(Small_class)
admin.site.register(Item)
admin.site.register(Itemset)