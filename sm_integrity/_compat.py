"""Optional dependency detection."""

from __future__ import annotations


def has_cryptography() -> bool:
    """Check if the cryptography package is available."""
    try:
        import cryptography  # noqa: F401

        return True
    except ImportError:
        return False


def has_sm_bridge() -> bool:
    """Check if the sm_bridge package is available."""
    try:
        import sm_bridge  # type: ignore[import-not-found]  # noqa: F401

        return True
    except ImportError:
        return False
