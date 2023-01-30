from rest_framework import serializers

from commercial_network.models import Provider


class ProviderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = '__all__'


class ProviderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = '__all__'

    def is_valid(self, *, raise_exception=False):
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        provider = Provider.objects.create(**validated_data)
        provider.save()
        return provider


class ProviderUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Provider
        fields = ['name', 'level_in_hierarchy']

    def is_valid(self, *, raise_exception=False):
        return super().is_valid(raise_exception=raise_exception)

    def save(self):
        ads = super().save()

        return ads


class AdsDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        field = ['id']