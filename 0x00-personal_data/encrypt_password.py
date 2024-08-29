#!/usr/bin/env python3
"""
Module for encrypting passwords.
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """ Hashes a password and returns the salted, hashed version. """
    encoded = password.encode()
    hashed = bcrypt.hashpw(encoded, bcrypt.gensalt())
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Checks if the provided password matches the hashed password. """
    encoded = password.encode()
    return bcrypt.checkpw(encoded, hashed_password)
