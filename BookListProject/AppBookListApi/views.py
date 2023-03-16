from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework.views import APIView


# Test these inside Insomia 
@api_view(['POST','GET','PUT','PATCH'])
def books(request):
    return Response('list of the books', status=status.HTTP_200_OK)
    #return HttpResponse('List of the books', status=status.HTTP_200_OK)

class BookList(APIView):
    # def get(self, req):
    #     return Response({"Message":"List of the Books"}, status.HTTP_200_OK)

    def post(self, req):
        return Response({"title":req.data.get('title')}, status.HTTP_201_CREATED)

    def get (self, req):
        author = req.GET.get('author')
        if(author):
            return Response({"Message":"Books created by : "+author}, status.HTTP_200_OK)
        
        return Response({"Message": "List of the boooks"}, status.HTTP_200_OK)


class Book(APIView):
    def get(self, req, pk):
        return Response({"Message":"Single book with Id : "+str(pk)}, status.HTTP_200_OK)

    def put(self, req, pk):
        return Response({"Title":req.data.get('title')}, status.HTTP_200_OK)


