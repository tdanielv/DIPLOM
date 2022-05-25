from rest_framework import serializers

from .models import BBooks, Album, Pep


class BBooksSerializers(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    genre = serializers.CharField(max_length=200)
    year = serializers.IntegerField(default=18)

    def create(self, validated_data):
        return BBooks.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.genre = validated_data.get('genre', instance.genre)
        instance.year = validated_data.get('year', instance.year)
        instance.save()
        return instance

# class PeopleSerializer(serializers.ModelSerializer):
#     profession = serializers.SlugRelatedField(read_only=True, many=True, slug_field='title')
#
#     class Meta:
#         model = People
#         fields = '__all__'

# class PeopleSerializer(serializers.ModelSerializer):
#     profession = serializers.SlugRelatedField(read_only=True, many=True, slug_field='title')
#
#     class Meta:
#         model = People
#         fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    tracks = serializers.StringRelatedField(many=True)

    class Meta:
        model = Album
        fields = ['album_name', 'artist', 'tracks']

class PepSerializer(serializers.ModelSerializer):
    pep = serializers.StringRelatedField(many=True)

    class Meta:
        model = Pep
        fields = ['first_name', 'last_name', 'pep']


# Selected_related and prefecture_related
class ProducersSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    productions = serializers.CharField(max_length=200)

class ProductionsSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    producers = serializers.CharField(max_length=200)