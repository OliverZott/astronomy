from dataclasses import dataclass
import math


@dataclass
class celestial_object:
    """
    Base class for celestial objects

    - name
    - radius [m]
    - mass [kg]
    - density [g/cm³]
    """
    name: str
    radius: float
    mass: float
    density: float


sun = celestial_object(
    name="sun",
    mass=1.99*math.pow(10, 30),
    radius=695*math.pow(10, 6),
    density=1.41
)

earth = celestial_object(
    name="earth",
    mass=5.97*math.pow(10, 24),
    radius=6.378*math.pow(10, 6),
    density=5.52
)

moon = celestial_object(
    name="moon",
    mass=7.342*math.pow(10, 22),
    radius=1.7381*math.pow(10, 6),
    density=3.344
)
