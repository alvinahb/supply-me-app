from django.test import TestCase

from supplyme.models import User
from supplyme.services.user import (create_user,
                                    delete_user,
                                    retrieve_user,
                                    update_user)


class UserTests(TestCase):

    def check_user_data(self, user, username, password, first_name, last_name, email):
        self.assertEqual(User.objects.get(pk=user.id).username, username)
        self.assertEqual(User.objects.get(pk=user.id).password, password)
        self.assertEqual(User.objects.get(pk=user.id).first_name, first_name)
        self.assertEqual(User.objects.get(pk=user.id).last_name, last_name)
        self.assertEqual(User.objects.get(pk=user.id).email, email)
        self.assertIs(User.objects.get(pk=user.id).is_superuser, False)
        self.assertIs(User.objects.get(pk=user.id).is_staff, False)
        self.assertIs(User.objects.get(pk=user.id).is_active, True)

    def test_user_crud(self):
        username = 'TestUser'
        password = 'TestPassword'
        first_name = 'TestFirstname'
        last_name = 'TestLastname'
        email = 'test@email.com'

        # Check that no user in DB
        self.assertEqual(User.objects.all().count(), 0)

        # Create user
        user = create_user(username=username, password=password, first_name=first_name,
                           last_name=last_name, email=email)
        self.assertEqual(User.objects.all().count(), 1)
        self.check_user_data(user=User.objects.get(pk=user.id), username=username,
                             password=password, first_name=first_name,
                             last_name=last_name, email=email)

        # Retrieve user
        retrieved_user = retrieve_user(user_id=user.id)
        self.check_user_data(user=retrieved_user, username=username, password=password,
                             first_name=first_name, last_name=last_name, email=email)

        # Update user
        new_username = 'NewUser'
        new_password = 'NewPassword'
        new_email = 'new@email.com'

        update_user(user_id=user.id, username=new_username, password=new_password,
                    email=new_email)
        self.assertEqual(User.objects.all().count(), 1)
        self.check_user_data(user=retrieved_user, username=new_username,
                             password=new_password, first_name=first_name,
                             last_name=last_name, email=new_email)

        # Delete user
        delete_user(user_id=user.id)
        self.assertEqual(User.objects.all().count(), 0)
