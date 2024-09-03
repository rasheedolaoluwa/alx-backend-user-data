#!/usr/bin/env python3
""" Module for handling Authentication.
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ Class to manage API authentication. """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method to check if an endpoint requires authentication. """
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
            if exc.endswith('*'):
                if exc[:-1] == path[:len(exc) - 1]:
                    return False
            elif tmp_path == exc:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Method to retrieve the Authorization header from a request. """
        if request is None:
            return None

        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar('User'):
        """ Method to validate and retrieve the current user. """
        return None
