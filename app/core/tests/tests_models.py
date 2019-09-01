from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTest(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = "viron@viron.com"
        password= "Testpass123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_user_with_normailzed_email_success(self):
        """Test creating a new user with normalized email is successful"""
        email = 'viron@VIRON.com'
        password = "Pass"
        #get_user_model() will return the currently active user model
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test123")

    def test_create_super_user(self):
        """Test creating super user"""
        user = get_user_model().objects.create_superuser(
        "viron@viron.com",
        "vishyverny"
        )
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
