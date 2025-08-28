from .models import Post, Comment
from rest_framework import serializers

class CommentSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['author', 'post','created_at']

    def get_replies(self, obj):
        replies = obj.replies.all().order_by('created_at')
        return CommentSerializer(replies, many=True).data

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'

    def validate(self, data):
        document = data.get('document')
        subcategory = data.get('subcategory')
        if document and subcategory != 'files':
            raise serializers.ValidationError('Documents can only be uploaded for Files subcategory.')
        return data