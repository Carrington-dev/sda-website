from django.contrib.auth import get_user_model
from django.test import TestCase

User = get_user_model()

class CustomUserTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="testuser@example.com",
            username="testuser@example.com",
            password="strongpassword123",
            first_name="John",
            last_name="Doe"
        )
        self.superuser = User.objects.create_superuser(
            email="admin@example.com",
            username="admin@example.com",
            password="adminpassword123",
            first_name="Admin",
            last_name="User"
        )
    
    def test_user_creation(self):
        """Test if a regular user is created properly"""
        self.assertEqual(self.user.email, "testuser@example.com")
        self.assertTrue(self.user.check_password("strongpassword123"))
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)
    
    def test_superuser_creation(self):
        """Test if a superuser is created properly"""
        self.assertEqual(self.superuser.email, "admin@example.com")
        self.assertTrue(self.superuser.check_password("adminpassword123"))
        self.assertTrue(self.superuser.is_staff)
        self.assertTrue(self.superuser.is_superuser)
    
    def test_user_str_representation(self):
        """Test user string representation"""
        self.assertEqual(str(self.user), "testuser@example.com")
    
    def test_duplicate_email(self):
        """Test that users cannot register with duplicate emails"""
        with self.assertRaises(Exception):
            User.objects.create_user(email="testuser@example.com", password="newpass123")
    
    # def test_authentication(self):
    #     """Test user authentication"""
    #     self.assertTrue(self.client.login(email="testuser@example.com", password="strongpassword123"))
    
    # def test_invalid_authentication(self):
    #     """Test authentication with invalid credentials"""
    #     self.assertFalse(self.client.login(email="testuser@example.com", password="wrongpassword"))
