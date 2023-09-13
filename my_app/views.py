from django.shortcuts import render
# # from rest_framework import viewsets

# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from my_app.models import Department, Employee, Position
from my_app.serializers import DepartmentSerializer, EmployeeSerializer, PositionSerializer


class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentEmployeesViewSet(ModelViewSet):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        department_id = self.kwargs.get('pk')
        return Employee.objects.filter(department_id=department_id)


class PositionViewSet(ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
#
# @api_view(http_method_names=['GET', 'POST'])
# def department_list_create_view(request):
#     if request.method == 'GET':
#         departments = Department.objects.all()
#         serializer = DepartmentSerializer(departments, many=True)
#     if request.method == 'POST':
#         serializer = DepartmentSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(http_method_names=['GET', 'DELETE', 'PUT'])
# def department_retrieve_update_delete_view(request, pk):
#         department = Department.objects.get(pk=pk)
#         if request.method == 'GET':
#             serializer = DepartmentSerializer(instance=department)
#             return Response(serializer.data)
#         elif request.method == 'DELETE':
#             department.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         elif request.method == 'PUT':
#             serializer = DepartmentSerializer(instance=department, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             else:
#                 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(http_method_names=['GET', 'POST'])
# def employee_list_create_view(request):
#     if request.method == 'GET':
#         employees = Employee.objects.all()
#         serializer = EmployeeSerializer(employees, many=True)
#     if request.method == 'POST':
#         serializer = EmployeeSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(http_method_names=['GET', 'DELETE', 'PUT'])
# def employee_retrieve_update_delete_view(request, pk):
#         employee = Employee.objects.get(pk=pk)
#         if request.method == 'GET':
#             serializer = EmployeeSerializer(instance=employee)
#             return Response(serializer.data)
#         elif request.method == 'DELETE':
#             employee.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         elif request.method == 'PUT':
#             serializer = EmployeeSerializer(instance=employee, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             else:
#                 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(http_method_names=['GET', 'POST'])
# def position_list_create_view(request):
#     if request.method == 'GET':
#         positions = Position.objects.all()
#         serializer = PositionSerializer(positions, many=True)
#     if request.method == 'POST':
#         serializer = PositionSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(http_method_names=['GET', 'DELETE', 'PUT'])
# def position_retrieve_update_delete_view(request, pk):
#         position = Position.objects.get(pk=pk)
#         if request.method == 'GET':
#             serializer = PositionSerializer(instance=position)
#             return Response(serializer.data)
#         elif request.method == 'DELETE':
#             position.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         elif request.method == 'PUT':
#             serializer = PositionSerializer(instance=position, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             else:
#                 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#






