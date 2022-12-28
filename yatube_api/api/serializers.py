from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from posts.models import Post, Group, Comment, Follow, User


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'author', 'text', 'pub_date',
                  'image', 'group')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    following = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username')

    user = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault(),
    )

    def validate(self, value):
        if self.context.get("request").user == value.get("following"):
            raise serializers.ValidationError(
                "Нельзя подписаться на себя"
            )
        return value

    class Meta:
        model = Follow
        fields = ('user', 'following')
