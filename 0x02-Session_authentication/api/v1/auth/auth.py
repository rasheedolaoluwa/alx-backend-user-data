#!/usr/bin/env python3
""" Authentication Module """
from flask import request
from typing import List, TypeVar
from os import getenv


class Auth:
    """ Manages the API authentication """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Checks if the endpoint requires authentication """
        if path is None or excluded_paths is None or excluded_paths == []:
            return True

        l_path = len(path)
        if l_path == 0:
            return True

        slash_path = path.endswith('/')

        tmp_path = path
        if not slash_path:
            tmp_path += '/'

        for exc in excluded_paths:
            l_exc = len(exc)
            if l_exc == 0:
                continue

            if exc[l_exc - 1] != '*':
                if tmp_path == exc:
                    return False
            else:
                if exc[:-1] == path[:l_exc - 1]:
                    return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Retrieves the authorization header from the request """
        if request is None:
            return None

        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar('User'):
        """ Returns the current user (to be implemented in subclasses) """
        return None

    def session_cookie(self, request=None):
        """ Extracts the session cookie value from the request """

        if request is None:
            return None

        SESSION_NAME = getenv("SESSION_NAME")

        if SESSION_NAME is None:
            return None

        session_id = request.cookies.get(SESSION_NAME)

        return session_id