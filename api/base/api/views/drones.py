from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import action

from drf_spectacular.utils import extend_schema

from dynamic_rest.viewsets import DynamicModelViewSet
from dynamic_rest.filters import DynamicFilterBackend, DynamicSortingFilter

from django.db.models import Q

from base.models import Drone
from base.api.serializers.drones import DroneSerializer, DroneBatterySerializer


class DroneViewSet(DynamicModelViewSet):
    """
    API endpoint that allows drone to be viewed and edited.
    """

    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated, ]

    filter_backends = [
        DynamicFilterBackend, DynamicSortingFilter,
    ]

    model = Drone
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer

    def get_queryset(self):
        """
        Filters and sorts drones.
        """
        queryset = Drone.objects.all()

        return queryset.order_by("serial_number")


    @extend_schema(methods=['get'], responses={200: DroneBatterySerializer()},
                   description="API endpoint allowing to retrieve the battery for a drone.")
    @action(detail=True, methods=['get'])
    def battery(self, request, pk=None):
        drone = self.get_object()
        return Response(DroneBatterySerializer(embed=True, many=False).to_representation(drone))


    @extend_schema(methods=['get'], responses={200: DroneSerializer(many=True)},
                   description="API endpoint allowing to retrieve the available drones for loading.")
    @action(detail=False, methods=['get'])
    def available_for_loading(self, request, pk=None):
        drones = Drone.objects.filter(
            Q(state='IDLE', battery_capacity__gte=25) |
            Q(state='LOADING')
        )

        page = self.paginate_queryset(drones)
        if page is not None:
            return self.get_paginated_response(DroneSerializer(embed=True, many=True).to_representation(drones))
            
        return Response(DroneSerializer(embed=True, many=True).to_representation(drones))