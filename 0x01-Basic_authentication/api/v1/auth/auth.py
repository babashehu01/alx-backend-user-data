#!/usr/bin/env python3
""" Defines Auth class
"""
from flask import request


class Auth:
    """Auth class
    """
    def __init__(self):
        """
            Constructor

            Args:
                path: path to authenticate
                excluded_paths: list of excluded path to authenticate
        """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
            Require the auth

            Args:
                path: path to authenticate
                excluded_paths: list of excluded path to authenticate

            Return:
                True if is authenticated otherwise false
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
            Look the headers

            Args:
                request: Look the autthorization

            Return:
                The authorization header or None
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
            Look current user

            Args:
                request: Look the reques user

            Return:
                The user
        """
        return None
