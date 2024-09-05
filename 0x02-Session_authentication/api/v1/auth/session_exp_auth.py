#!/usr/bin/env python3
""" Module for Session Authentication with Expiration """
from api.v1.auth.session_auth import SessionAuth
from datetime import datetime, timedelta
from models.user import User
from os import getenv


class SessionExpAuth(SessionAuth):
    """ Session Expiration class for managing session timeouts """

    def __init__(self):
        """ Initializes session duration from environment variable """
        SESSION_DURATION = getenv('SESSION_DURATION')

        try:
            session_duration = int(SESSION_DURATION)
        except Exception:
            session_duration = 0

        self.session_duration = session_duration

    def create_session(self, user_id=None):
        """ Creates a session with an expiration time """

        session_id = super().create_session(user_id)

        if session_id is None:
            return None

        session_dictionary = {
            "user_id": user_id,
            "created_at": datetime.now()
        }

        self.user_id_by_session_id[session_id] = session_dictionary

        return session_id

    def user_id_for_session_id(self, session_id=None):
        """ Retrieves the user ID based on the session ID and checks if
        the session is still valid """

        if session_id is None:
            return None

        if session_id not in self.user_id_by_session_id:
            return None

        session_dictionary = self.user_id_by_session_id.get(session_id)

        if session_dictionary is None:
            return None

        if self.session_duration <= 0:
            return session_dictionary.get('user_id')

        created_at = session_dictionary.get('created_at')

        if created_at is None:
            return None

        expired_time = created_at + timedelta(seconds=self.session_duration)

        if expired_time < datetime.now():
            return None

        return session_dictionary.get('user_id')
