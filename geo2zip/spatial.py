from math import inf, sqrt
from typing import List, Sequence, Tuple


Point = Tuple[float, float]


class KDTree:
    """Small 2D KD-tree compatible with the subset of scipy.spatial.KDTree used here."""

    def __init__(self, data: Sequence[Point]):
        if not data:
            raise ValueError("KDTree requires at least one point.")

        self.data: List[Point] = list(data)
        self._nodes: List[Tuple[int, int, int, int]] = []
        self._root = self._build(list(range(len(self.data))), 0)

    def _build(self, indices: List[int], depth: int) -> int:
        if not indices:
            return -1

        axis = depth % 2
        indices.sort(key=lambda index: self.data[index][axis])
        median = len(indices) // 2

        node_index = len(self._nodes)
        self._nodes.append((indices[median], axis, -1, -1))

        left = self._build(indices[:median], depth + 1)
        right = self._build(indices[median + 1:], depth + 1)
        self._nodes[node_index] = (indices[median], axis, left, right)
        return node_index

    def query(self, point: Point) -> Tuple[float, int]:
        """
        Return the Euclidean distance and index of the nearest stored point.

        This mirrors scipy.spatial.KDTree.query for the single-point, k=1 case
        used by Geo2Zip.
        """
        query_lat, query_lon = point
        best_distance_squared = inf
        best_index = -1

        def visit(node_index: int) -> None:
            nonlocal best_distance_squared, best_index

            if node_index == -1:
                return

            point_index, axis, left, right = self._nodes[node_index]
            lat, lon = self.data[point_index]
            lat_delta = query_lat - lat
            lon_delta = query_lon - lon
            distance_squared = lat_delta * lat_delta + lon_delta * lon_delta

            if distance_squared < best_distance_squared:
                best_distance_squared = distance_squared
                best_index = point_index

            axis_delta = point[axis] - self.data[point_index][axis]
            near, far = (left, right) if axis_delta < 0 else (right, left)

            visit(near)
            if axis_delta * axis_delta < best_distance_squared:
                visit(far)

        visit(self._root)
        return sqrt(best_distance_squared), best_index
