from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Place, Large_class, Small_class, Item, Itemset
from .serializers import LclassSerializer, SclassSerializer, ItemSerializer, ItemsetSerializer

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

class ItemsetListAPIView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ItemsetSerializer
    #queryset = Itemset.objects.all()
    def get_queryset(self):
        return Itemset.objects.all()
    def list(self, requaet):
        Lis = []
        queryset = self.get_queryset()
        for itmset in ItemsetSerializer(queryset, many=True).data:
            set_dic = {}
            header_dic = {}
            for key in itmset.keys():
                if key == "id":
                    set_dic[key] = itmset[key]
                    header_dic[key] = itmset[key]
                elif key == "owned_parts_ITEMLIST":
                    set_dic["content_items"] = itmset[key]
                else:
                    header_dic[key] = itmset[key]
            set_dic["header_info"] = header_dic
            Lis.append(set_dic)
        return Response(Lis)
            
            
