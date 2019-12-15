from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from demo_learn.models import DoubandbMovies
from demo_learn.Movieserializers import MovieSerializer
from rest_framework.response import Response
from rest_framework import status
from demo_learn.models import Person
from rest_framework.views import APIView
from django.http import Http404,HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
    return HttpResponse('hello world')

def create(request):
    # Person.objects.create(name ='xiaoliss',age = 18)
    # s = Person.objects.get(name='xiaoliss')
    person = Person.objects.all()
    serializer =MovieSerializer(person)
    return HttpResponse(serializer.data)
# @csrf_exempt
# @api_view(['GET','POST'])
# def get_list(request,format= None):
#     if request.method =='GET':
#         movie = DoubandbMovies.objects.all()
#         serializer = MovieSerializer(movie,many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class MovieList(APIView):
    def get(self,request,format =None):
        movie = DoubandbMovies.objects.all()
        serializer = MovieSerializer(movie,many=True)
        return Response(serializer.data)
    def post(self,request,format =None):
        serializer = MovieSerializer(data=request.data )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class MovieDetail(APIView):
    def get_object(self,pk):
        try:
            return DoubandbMovies.objects.get(pk = pk)
        except:
            return Http404
    def get(self,request,pk,format = None):
        movie = self.get_object(pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    def put(self,request,pk,format=None):
        movie = self.get_object(pk)
        serializer =MovieSerializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk,format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
