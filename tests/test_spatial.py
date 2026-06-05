import pytest

from geo2zip.spatial import KDTree


def test_kdtree_query_returns_nearest_point_index_and_distance():
    points = [(0.0, 0.0), (3.0, 4.0), (10.0, 10.0)]
    tree = KDTree(points)

    distance, index = tree.query((2.0, 3.0))

    assert index == 1
    assert distance == pytest.approx(1.4142135624)


def test_kdtree_query_checks_far_branch_when_needed():
    points = [(0.0, 0.0), (10.0, 10.0), (6.0, 3.0), (6.0, 5.0)]
    tree = KDTree(points)

    distance, index = tree.query((5.9, 5.0))

    assert index == 3
    assert distance == pytest.approx(0.1)


def test_kdtree_rejects_empty_data():
    with pytest.raises(ValueError, match="requires at least one point"):
        KDTree([])
