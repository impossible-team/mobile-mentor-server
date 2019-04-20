from django.contrib import admin
from django.conf.urls import url, include
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from profile import api_views
from topic import views as topic_views

urlpatterns = [
    url('admin/', admin.site.urls),
]

router = routers.DefaultRouter()
router.register(r'profiles', api_views.ProfileViewSet)
router.register(r'topics', topic_views.TopicViewSet)

# Логин
urlpatterns += [
    url(r'login/', api_views.LoginAPIView.as_view(), name='login')
]

urlpatterns += [
    url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'docs/', get_swagger_view('Swagger')),
    url(r'', include(router.urls))
]
