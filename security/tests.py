from django.test import TestCase
from security.models import User

# Create your tests here.
class UserCreationTest(TestCase):
    def test_user_model(self):
        user = User.objects.create(email="crn96m@gmail.com", username="crn96m", phone="0798005807",)
        assert(user.email, "crn96m@gmail.com")