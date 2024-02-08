#!/usr/bin/env python3
""" doc doc doc """
import bcrypt


def hash_password(password: str) -> bytes:
    """doc doc doc"""
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
