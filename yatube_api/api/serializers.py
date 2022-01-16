from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework import validators

from posts.models import Comment, Follow, Group, Post, User


class PostSerializer(serializers.ModelSerializer):
    """Serializer for model Post."""
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class GroupSerializer(serializers.ModelSerializer):
    """Serializer for model Group."""

    class Meta:
        fields = '__all__'
        model = Group


class CommentSerializer(serializers.ModelSerializer):
    """Serializer for model Comment."""
    author = SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        fields = '__all__'
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    """Serializer for model Follow."""
    user = SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault())
    following = SlugRelatedField(
        queryset=User.objects.all(), slug_field='username')

    class Meta:
        fields = '__all__'
        model = Follow
        # Validate that only unique pairs of user and following exits:
        validators = [
            validators.UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following')
            )
        ]

    def validate(self, data):
        if self.context.get('request').user == data['following']:
            raise validators.ValidationError('LOL')
        return data
