from django.http import Http404

class RestrictUserMixin:
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.user != self.request.user:
            raise Http404("Acesso negado!")
        return obj