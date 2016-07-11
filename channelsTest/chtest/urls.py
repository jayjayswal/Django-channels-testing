from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from chtest.controllers import user


urlpatterns = [

    url(r'^user/?$',user.user, name='user'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
