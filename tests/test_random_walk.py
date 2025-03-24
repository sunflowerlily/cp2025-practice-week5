import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.random_walk import random_walk_2d
import pytest

def test_random_walk_length():
    """Test if the random walk has correct number of steps"""
    steps = 1000
    path = random_walk_2d(steps)
    assert len(path) == steps + 1  # +1 because it includes the starting point

def test_random_walk_step_size():
    """Test if each step is a diagonal step (moves 1 unit in both x and y directions)"""
    path = random_walk_2d(100)
    for i in range(1, len(path)):
        dx = abs(path[i][0] - path[i-1][0])
        dy = abs(path[i][1] - path[i-1][1])
        assert dx == 1 and dy == 1

def test_random_walk_start_point():
    """Test if the starting point is (0,0)"""
    path = random_walk_2d(100)
    assert path[0] == (0, 0)