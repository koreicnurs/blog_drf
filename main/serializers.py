from rest_framework import serializers

from main.models import Post, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    author = serializers.EmailField(source='author.email')

    class Meta:
        model = Post
        fields = ('id', 'text', 'category', 'author', 'create_at', 'image')

    def __get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image:
            url = obj.image.url
            if request is not None:
                url = request.build_absolute_uri(url)
        else:
            url = ''
        return url

    def to_representation(self, instance):
        representation = super(PostSerializer, self).to_representation(instance)
        representation['image'] = self.__get_image_url(instance)
        return representation
