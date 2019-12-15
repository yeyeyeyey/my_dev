from rest_framework import serializers
from demo_learn.models import DoubandbMovies
from demo_learn.models import Person

class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DoubandbMovies
        fields = ('title','score','info','movie_site','pic_site',
                  'director',
                 'actor','create_time','update_time')
class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoubandbMovies
        fields = ('id','title')

class ListPicSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoubandbMovies
        fields = "__all__"

class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        person = Person
        fields = "__all__"