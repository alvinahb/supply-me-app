from django.test import TestCase

from supplyme.models import User
from supplyme.services.user import (create_user,
                                    delete_user,
                                    retrieve_user,
                                    update_user)


class UserTests(TestCase):
    def test_user_crud(self):
        username = 'TestUser'
        password = 'TestPassword'
        email = 'test@email.com'

        # Check that no user in DB
        self.assertEqual(User.objects.all().count(), 0)

        # Create user
        user = create_user(username=username, password=password, email=email)
        self.assertEqual(User.objects.all().count(), 1)
        self.assertEqual(User.objects.get(pk=user.id).username, username)
        self.assertEqual(User.objects.get(pk=user.id).password, password)
        self.assertEqual(User.objects.get(pk=user.id).email, email)

        # Retrieve user
        retrieved_user = retrieve_user(user_id=user.id)
        self.assertEqual(retrieved_user.username, username)
        self.assertEqual(retrieved_user.password, password)
        self.assertEqual(retrieved_user.email, email)

        # Update user
        new_username = 'NewUser'
        new_password = 'NewPassword'
        new_email = 'new@email.com'

        update_user(user_id=user.id, username=new_username, password=new_password,
                    email=new_email)
        self.assertEqual(User.objects.all().count(), 1)
        self.assertEqual(User.objects.get(pk=user.id).username, new_username)
        self.assertEqual(User.objects.get(pk=user.id).password, new_password)
        self.assertEqual(User.objects.get(pk=user.id).email, new_email)

        # Delete user
        delete_user(user_id=user.id)
        self.assertEqual(User.objects.all().count(), 0)
