from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Place, Large_class, Small_class, Item
from .serializers import PlaceSerializer, LclassSerializer, SclassSerializer, ItemSerializer


class PlaceListAPIView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()

class LclassListAPIView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = LclassSerializer
    queryset = Large_class.objects.all()

class SclassListAPIView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = SclassSerializer
    queryset = Small_class.objects.all()

class ItemListAPIView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

class SetItemAPIView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ItemSerializer
    def get_queryset(self):
        return Item.objects.filter(is_set = True)
    def list(self, request):
        Lis = []
        queryset = self.get_queryset()
        set_name_list = set([dic["set_name"] for dic in queryset.values("set_name")])
        set_Dic = {}
        for setnm in set_name_list:
            set_Dic[setnm] = []
        for itm in ItemSerializer(queryset, many=True).data:
            belonged_set = set_Dic[itm["set_name"]]
            belonged_set.append(itm)
        for st in set_Dic.keys():
            dic = {"name":st, "items":set_Dic[st]}
            Lis.append(dic)
        return Response(Lis)

class ItemTabelListAPIView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = LclassSerializer
    def get_queryset(self):
        return Large_class.objects.all()
    def list(self, request):
        l_class_lis = [{"name": "All"}]
        s_class_dic = {}
        item_lis = []
        queryset = self.get_queryset()
        for lcls in LclassSerializer(queryset, many=True).data:
            l_class_lis.append( {"name": lcls["name"]} )
            s_class_dic[ lcls["name"] ] = lcls["small_class_set"]
            item_lis.extend(lcls["item_set"])
        s_class_dic["All"] = [{"name": "All"}]
        Lis = [{
            "large_classes": l_class_lis,
            "small_classes": s_class_dic,
            "items":item_lis
        }]
        return Response(Lis)

