import json
from pathlib import Path

from django.core.management.base import BaseCommand
from ...models import Place, Large_class, Small_class, Item

asset_dir = Path(r"C:\Users\naoto\Documents\作業箱\python\projects\gd_my_stash\src\assets")

class Command(BaseCommand):	
	
	#コマンド実行時に呼ばれるメソッド
	def handle(self, *args, **options):
		assets_fle = Path(asset_dir, "gd_list.json")
		classifi_dic = {
    "Helm":"Armors", "Shoulders":"Armors", "Armor":"Armors", "Pants":"Armors", "Gloves":"Armors",
    "Boots":"Armors", "Belt":"Armors", "Ring":"Accessories", "Amulet":"Accessories", "Medal":"Accessories",
    "One-gun":"One-Weapons", "Two-gun":"Two-Weapons", "One-sword":"One-Weapons", "Two-sword":"Two-Weapons",
    "One-mace":"One-Weapons", "Two-mace":"Two-Weapons", "One-ax":"One-Weapons", "Two-ax":"Two-Weapons",
    "One-mace":"One-Weapons", "Two-mace":"Two-Weapons", "One-scepter":"One-Weapons","One-dagger":"One-Weapons",
    "Shield":"One-Weapons", "Off-hand":"One-Weapons"
}
		with assets_fle.open("r", encoding="utf-8") as f:
			jso_data = json.load(f)

			for pla in jso_data.keys():
				#場所モデルの作成と設定
				place_model = Place.objects.get_or_create(name=pla)[0]
				place_model.save()

				for itm in jso_data[pla]:
					kind = itm["kind"]
					#小分類モデルの作成と設定
					S_class_model = Small_class.objects.get_or_create(name=kind)[0]
					S_class_model.save()

					#大分類モデルの作成と設定
					large_kind = classifi_dic[kind]
					L_class_model = Large_class.objects.get_or_create(name=large_kind)[0]
					L_class_model.save()

					#アイテムモデルの作成と設定
					item_model = Item.objects.get_or_create(name=itm["name"])[0]
					item_model.is_set = itm["is_set"]
					item_model.save()

					#外部キーの紐づけ
					place_model.item_set.add(item_model)
					S_class_model.item_set.add(item_model)
					L_class_model.item_set.add(item_model)

					print(f"creation of {item_model.name} ends")