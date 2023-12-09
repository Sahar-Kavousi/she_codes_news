from django.urls import path
from .views import CreateAccountView, profile, edit_profile
from django.conf.urls.static import static
from django.conf import settings

app_name = 'users'

urlpatterns = [
                  path('create-account/', CreateAccountView.as_view(), name='createAccount'),
                  path('profile/<username>/', profile, name='profile'),
                  path('edit-profile/', edit_profile, name='edit_profile'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
