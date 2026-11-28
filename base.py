"""Base class for models in MZPets MVC demo"""


class BaseModel:
    """Provides a simple representation and optional serialization for demo models."""

    def __repr__(self) -> str:
        attrs = ", ".join(f"{k}={v!r}" for k, v in self.__dict__.items())
        return f"{self.__class__.__name__}({attrs})"

    def to_dict(self) -> dict:
        return self.__dict__.copy()
