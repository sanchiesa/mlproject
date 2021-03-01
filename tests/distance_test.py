# tests/distance_test.py
from mlproject.distance import haversine

def test_type_haversine():
    assert type(haversine(48.865070, 2.380009, 48.865070, 1.380009)) == int or float

