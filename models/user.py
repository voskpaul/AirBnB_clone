#!/usr/bin/python3
"""
This module defines a User class
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    This class is responsible for managing user entities.
    """

    def __init__(self):
        """
        Initialize a new user instance.
        """
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
