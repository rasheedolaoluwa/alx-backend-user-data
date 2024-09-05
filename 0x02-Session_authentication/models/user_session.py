#!/usr/bin/env python3
""" User session management module """
from models.base import Base


class UserSession(Base):
    """ Manages user sessions """

    def __init__(self, *args: list, **kwargs: dict):
        """ Initializes user session attributes """
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
