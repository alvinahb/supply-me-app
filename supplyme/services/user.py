from supplyme.models import User


def create_user(username, password, first_name, last_name, email):
    user = User(username=username, password=password, first_name=first_name,
                last_name=last_name, email=email)
    user.save()

    return user


def retrieve_user(user_id):
    return User.objects.get(pk=user_id)


def update_user(user_id, username=None, password=None, email=None):
    user = User.objects.get(pk=user_id)

    if username:
        user.username = username
    if password:
        user.password = password
    if email:
        user.email = email
    
    user.save()


def delete_user(user_id):
    user = User.objects.get(pk=user_id)
    user.delete()
