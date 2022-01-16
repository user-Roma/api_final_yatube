from rest_framework import viewsets

from .permissions import AuthorOrIsAuthenticatedAndReadOnly, ReadOnly


class YatubeApiV1BaseViewSet(viewsets.ModelViewSet):
    """Base viewset for Posts, Commetns, Follow."""
    permission_classes = [AuthorOrIsAuthenticatedAndReadOnly]

    def perform_create(self, serializer):
        """Set a new value to the field author."""
        serializer.save(author=self.request.user)

    def get_permissions(self):
        """Set ReadOnly permissions for safe methods."""
        if self.action == 'retrieve' or self.action == 'list':
            return(ReadOnly(),)
        return super().get_permissions()
