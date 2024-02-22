#!/usr/bin/env python3
""" doc doc doc """

import bcrypt


def _hash_password(password: str) -> bytes:
    """doc doc doc"""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
