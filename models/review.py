#!/usr/bin/python3
"""Module to create the review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Class for managing review objects"""

    place_id = ""
    user_id = ""
    text = ""