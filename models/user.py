#!/usr/bin/python3
""" Module for User
"""


from models.base_model import BaseModel


class User(BaseModel):
    """BaseModel User
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
