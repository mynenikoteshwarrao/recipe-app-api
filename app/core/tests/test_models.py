"""
Tests for models
"""

from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test Models."""

    def test_user_created_with_email_successful(self):
        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalize(self):
        """Test email is normalize for new users."""
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['test2@Example.com', 'test2@example.com'],
            ['Test3@EXAMPLE.com', 'Test3@example.com'],
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, "sample123")
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """Test that creating a user without an email raises a ValeuError"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('','test123')

    def test_create_super_user(self):
        """Test creating super user"""
        user = get_user_model().objects.create_superuser(
            'test@example.com',
            'pass@123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)