from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CRUD_api
from .serializers import CRUD_apiSerializer

# Create your views here.



class CRUD_apiView(APIView):
    def get(self, request):
        CRUD_objects = CRUD_api.objects.all()
        serializer = CRUD_apiSerializer(CRUD_objects, many=True)
        return Response({"Object": serializer.data})

    def post(self, request):
        CRUD_objects = request.data.get('CRUD_api')
        # Create an article from the above data
        serializer = CRUD_apiSerializer(data=CRUD_objects)
        if serializer.is_valid(raise_exception=True):
            CRUD_saved = serializer.save()
        return Response({"success": " cell '{}','{}' created successfully".format(CRUD_saved.name, CRUD_saved.surname)})

    def put(self, request, pk):
        saved_cell = get_object_or_404(CRUD_api.objects.all(), pk=pk)
        data = request.data.get('CRUD_api')
        serializer = CRUD_apiSerializer(instance=saved_cell, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            cell_saved = serializer.save()
        return Response({
            "success": "cell '{}' updated successfully".format(cell_saved.name)
        })

    def delete(self, request, pk):
        # Get object with this pk
        cell = get_object_or_404(CRUD_api.objects.all(), pk=pk)
        cell.delete()
        return Response({
            "message": "Article with id `{}` has been deleted.".format(pk)
        }, status=204)