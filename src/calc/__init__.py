"""Tiny calculator package for CI/CD lab."""

from .ops import add, div, mul, sub  # re-export

__all__ = ["add", "sub", "mul", "div"]
