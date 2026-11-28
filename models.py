"""Model definitions for MZPets MVC demo."""

from dataclasses import dataclass, field
from base import BaseModel


@dataclass
class Pet(BaseModel):
    """A pet displayed in the gallery or featured section."""
    name: str = ""
    species: str = ""          # Dog, Cat, Bird, Other
    image_url: str = ""
    description: str = ""


@dataclass
class Service(BaseModel):
    """A service offered by the shop."""
    name: str = ""
    description: str = ""
    icon: str = ""             # emoji used as icon


@dataclass
class Testimonial(BaseModel):
    """A customer testimonial."""
    quote: str = ""
    author: str = ""


@dataclass
class TeamMember(BaseModel):
    """A team member displayed on the About page."""
    name: str = ""
    role: str = ""
    emoji: str = ""
