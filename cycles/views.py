from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Cycle
from .serializers import CycleSerializer

class CycleApiView(APIView):
    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the Cycle items for given requested user
        '''

        # use filter to restrict to user's filter: e.g filter(user = request.user.id)
        Cycles =Cycle.objects
        serializer = CycleSerializer(Cycles, many=True)
        return Response(serializer.data,  status=status.HTTP_200_OK)
    

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the cycle with given cycle data
        '''
        data = {
            'title': request.data.get('title'), 
        }
        serializer =CycleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CycleDetailApiView(APIView):
    def get_object(self, cycle_id, user_id):
        '''
        Helper method to get the object with given cycle_id, and user_id
        '''
        try:
            return Cycle.objects.get(id=cycle_id, user = user_id)
        except Cycle.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, cycle_id, *args, **kwargs):
        '''
        Retrieves the cycle with given cycle_id
        '''
        cycle_instance = self.get_object(cycle_id, request.user.id)
        if not cycle_instance:
            return Response(
                {"res": "Object with Cycle id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = CycleSerializer(cycle_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, Cycle_id, *args, **kwargs):
        '''
        Updates the cycle item with given cycle_id if exists
        '''
        cycle_instance = self.get_object(Cycle_id, request.user.id)
        if not cycle_instance:
            return Response(
                {"res": "Object with Cycle id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'title': request.data.get('title'), 
            'category': request.data.get('category'),
            'plan_description': request.data.get('plan'), 
            'do_description': request.data.get('plan'), 
            'action_description': request.data.get('plan'), 
            'check_description': request.data.get('plan'), 
        }
        serializer = CycleSerializer(instance = cycle_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, cycle_id, *args, **kwargs):
        '''
        Deletes the cycle item with given cycle_id if exists
        '''
        cycle_instance = self.get_object(cycle_id, request.user.id)
        if not cycle_instance:
            return Response(
                {"res": "Object with cycle id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        cycle_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )