import pytest

from geo2zip.distance import haversine_distance


def test_haversine_distance_is_zero_for_identical_points():
    assert haversine_distance((40.7128, -74.0060), (40.7128, -74.0060)) == pytest.approx(0.0)


def test_haversine_distance_returns_kilometers_between_known_cities():
    new_york = (40.7128, -74.0060)
    los_angeles = (34.0522, -118.2437)

    assert haversine_distance(new_york, los_angeles) == pytest.approx(3935.75, abs=0.1)
