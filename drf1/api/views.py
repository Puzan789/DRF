from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.


@api_view(["GET"])
def home(request):
    stu = student.objects.all()
    serializer = studentserializer(stu, many=True)

    return Response({"hello": "world", "message": serializer.data})


@api_view(["POST"])
def post_student(request):
    data = request.data
    serializer = studentserializer(data=request.data)
    if not serializer.is_valid():
        return Response(
            {
                "status": 403,
                "errors": serializer.errors,
                "message": "something went wrong",
            }
        )
    serializer.save()
    return Response(
        {"hello": "world", "payload": serializer.data, "message": "your data is save"}
    )


@api_view(["PUT"])
def update_student(request,id):
  
        stu_obj=student.objects.get(id=id)
        serializer = studentserializer(stu_obj,data=request.data,partial=True)  #pailako data j X tei halxa partial ley
        if not serializer.is_valid():
            return Response(
                {
                    "status": 403,
                    "errors": serializer.errors,
                    "message": "something went wrong",
                }
            )
        serializer.save()
        return Response({"hello": "world", "payload": serializer.data, "message": "your data is save"})
  

# @api_view(["DELETE"])
# def delete(request,id)