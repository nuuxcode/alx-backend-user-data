#!/usr/bin/env python3
"""doc doc doc """
from typing import List, TypeVar
from flask import request


class Auth:
    """doc doc doc"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """doc doc doc"""
        return False

    def authorization_header(self, request=None) -> str:
        """doc doc doc"""
        return None

    def current_user(self, request=None) -> TypeVar("User"):
        """doc doc doc"""
        return None
