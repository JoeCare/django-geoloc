from rest_framework import serializers
from .models import Locator


class LocatorSerializer(serializers.ModelSerializer):
    # url = serializers.SerializerMethodField()

    class Meta:
        model = Locator
        fields = '__all__'
        ready_only_fields = ['id']

    # def validate_title(self, _title):
    #     query = Book.objects.filter(title__iexact=_title)
    #     if self.instance:
    #         query = query.exclude(id=self.instance.id)
    #     if query.exists():
    #         raise serializers.ValidationError(
    #             'Title multiplication. Set unique title.')
    #     return _title
