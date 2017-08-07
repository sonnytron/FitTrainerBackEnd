from rest_framework import routers

from .views import CreateView

router = routers.DefaultRouter(trailing_slash=False)
router.register('excercise', CreateView)

urlpatterns = router.urls
