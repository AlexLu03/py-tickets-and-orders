from django.contrib.auth import get_user_model
from typing import Optional
from django.core.exceptions import ValidationError

from db import models


def create_user(
        username: str,
        password: str,
        email: Optional[str] = None,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
) -> models.Model:
    user_model = get_user_model()

    kwargs = {}
    if email is not None:
        kwargs['email'] = email
    if first_name is not None:
        kwargs['first_name'] = first_name
    if last_name is not None:
        kwargs['last_name'] = last_name

    user = user_model.objects.create_user(
        username=username,
        password=password,
        **kwargs
    )

    return user

def get_user(
        user_id: int
) -> models.Model:
    return get_user_model().objects.get(pk=user_id)

def update_user(
        user_id: int,
        username: Optional[str] = None,
        password: Optional[str] = None,
        email: Optional[str] = None,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
) -> models.Model:
    try:
        user = get_user(user_id)
        if username is not None:
            user.username = username
        if password is not None:
            user.set_password(password)
        if email is not None:
            user.email = email
        if first_name is not None:
            user.first_name = first_name
        if last_name is not None:
            user.last_name = last_name
    except get_user_model().DoesNotExist:
        raise ValueError(f"User with id={user_id} does not exist")

    user.save()
    return user


