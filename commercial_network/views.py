import django_filters
from rest_framework import filters
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from commercial_network.models import Provider
from commercial_network.permissions import ProviderPermission
from commercial_network.serializers import ProviderListSerializer, ProviderCreateSerializer, ProviderUpdateSerializer, \
    AdsDestroySerializer


class ProviderListView(ListAPIView):
    queryset = Provider.objects.order_by('level_in_hierarchy').all()
    serializer_class = ProviderListSerializer
    permission_classes = [ProviderPermission]
    # filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    # filterset_fields = ['name']
    filter_backends = [filters.SearchFilter]
    search_fields = ['contact__country']

    def get(self, request, *args, **kwargs):
        cites = request.GET.get('city')
        if cites:
            self.queryset = self.queryset.filter(contact__city__icontains=cites)
        country = request.GET.get('country')
        if country:
            self.queryset = self.queryset.filter(contact__country__icontains=country)
        return super().get(self, *args, **kwargs)


class ProviderRetrieveView(RetrieveAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderListSerializer
    permission_classes = [ProviderPermission]


class ProviderCreateView(CreateAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderCreateSerializer
    permission_classes = [ProviderPermission]


class ProviderUpdateView(UpdateAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderUpdateSerializer
    permission_classes = [ProviderPermission]


class ProviderDestroyView(DestroyAPIView):
    queryset = Provider.objects.all()
    serializer_class = AdsDestroySerializer
    permission_classes = [ProviderPermission]
