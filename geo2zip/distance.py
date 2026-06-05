from math import asin, cos, radians, sin, sqrt
from typing import Tuple


def haversine_distance(point_a: Tuple[float, float], point_b: Tuple[float, float]) -> float:
    """
    Return the great-circle distance between two latitude/longitude points in kilometers.
    """
    earth_radius_km = 6371.0088
    lat_a, lon_a = point_a
    lat_b, lon_b = point_b

    lat_delta = radians(lat_b - lat_a)
    lon_delta = radians(lon_b - lon_a)
    lat_a = radians(lat_a)
    lat_b = radians(lat_b)

    angle = (
        sin(lat_delta / 2) ** 2
        + cos(lat_a) * cos(lat_b) * sin(lon_delta / 2) ** 2
    )

    return 2 * earth_radius_km * asin(sqrt(angle))
