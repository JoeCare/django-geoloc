# from abc import ABC
from abc import ABC

from rest_framework import serializers
from .models import Locator


class LocatorSerializer(serializers.ModelSerializer):
    # url = serializers.SerializerMethodField()

    def __init__(self, dictionary, **kwargs):
        super().__init__(**kwargs)
        for key, val in dictionary.items():
            setattr(self, key, val)

    data_collected = serializers.StringRelatedField(
        many=True, required=False)

    class Meta:
        model = Locator
        fields = ['request_ipv4', 'data_collected']


    # def validate_title(self, _title):
    #     query = Book.objects.filter(title__iexact=_title)
    #     if self.instance:
    #         query = query.exclude(id=self.instance.id)
    #     if query.exists():
    #         raise serializers.ValidationError(
    #             'Title multiplication. Set unique title.')
    #     return _title


# class OutputSerializer(serializers.BaseSerializer, ABC):
#
#     def to_representation(self, instance):
#         self.context()
#         return
#         pass
#
#     class Meta:
#         model = Locator
#         fields =
