from .models import Link

def ctx_dict(request):
    ctx = {link.key: link.url for link in Link.objects.all()}
    return ctx