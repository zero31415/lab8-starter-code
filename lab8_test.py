"""test code for TIL Python programming jupyter notebook Lab 8 - AdvancedData Visualization"""
from unittest import result
import pytest
import matplotlib.pyplot as plt
from testbook import testbook


@pytest.fixture(scope='module')
def tb():
    with testbook('lab8_2025.ipynb', execute=True) as tb:
        yield tb

# Q1 test the create_3d_plots function
def test_create_3d_plots(tb):
    result_test_q1 = tb.ref("test_q1")
    assert result_test_q1["num_plots"] == 2, "There should be two subplots."
    assert result_test_q1["ax1_color_map"] == "viridis", "The colormap of the surface plot should be 'viridis'."
    # assert result_test_q1["ax2_color"][0].tolist() == [0., 0., 1., 1.], "The color of the wireframe plot should be 'blue'."


# Q2: test plotly express map
def test_px_map(tb):
    result_test_q2 = tb.ref("test_q2")
    assert result_test_q2["title"] == "2007 Life Expectancy", "Error: Title should be '2007 Life Expectancy'."


