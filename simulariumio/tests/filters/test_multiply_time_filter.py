#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from simulariumio import FileConverter
from simulariumio.filters import MultiplyTimeFilter
from simulariumio.tests.conftest import test_scatter_plot


@pytest.mark.parametrize(
    "input_path, plot_data, _filter, expected_data",
    [
        (
            "simulariumio/tests/data/cytosim/aster_pull3D_couples_actin_solid_3_frames"
            "/aster_pull3D_couples_actin_solid_3_frames_small.json",
            test_scatter_plot(),
            MultiplyTimeFilter(multiplier=100),
            {
                "trajectoryInfo": {
                    "version": 2,
                    "timeUnits": {
                        "magnitude": 1.0,
                        "name": "s",
                    },
                    "timeStepSize": 5,
                    "totalSteps": 3,
                    "spatialUnits": {
                        "magnitude": 1.0,
                        "name": "µm",
                    },
                    "size": {"x": 200.0, "y": 200.0, "z": 200.0},
                    "typeMapping": {
                        "1": {"name": "microtubule"},
                        "7": {"name": "motor complex"},
                    },
                },
                "spatialData": {
                    "version": 1,
                    "msgType": 1,
                    "bundleStart": 0,
                    "bundleSize": 3,
                    "bundleData": [
                        {
                            "frameNumber": 0,
                            "time": 0.0,
                            "data": [
                                1001.0,
                                1.0,
                                1.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                1.0,
                                15.0,
                                36.93,
                                36.8,
                                16.78,
                                30.55,
                                43.87,
                                19.84,
                                24.169999999999998,
                                50.93,
                                22.900000000000002,
                                17.78,
                                57.99999999999999,
                                25.95,
                                11.4,
                                65.07,
                                29.01,
                                1000.0,
                                12.0,
                                7.0,
                                -73.8,
                                -25.2,
                                -43.89,
                                0.0,
                                0.0,
                                0.0,
                                2.0,
                                0.0,
                            ],
                        },
                        {
                            "frameNumber": 1,
                            "time": 5,
                            "data": [
                                1001.0,
                                1.0,
                                1.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                1.0,
                                18.0,
                                44.55,
                                33.97,
                                8.86,
                                36.63,
                                38.269999999999996,
                                4.51,
                                28.96,
                                43.28,
                                0.5,
                                21.83,
                                49.61,
                                -2.52,
                                16.0,
                                57.66,
                                -3.58,
                                12.85,
                                66.92,
                                -1.47,
                                1000.0,
                                12.0,
                                7.0,
                                -72.52,
                                -21.9,
                                -43.59,
                                0.0,
                                0.0,
                                0.0,
                                2.0,
                                0.0,
                            ],
                        },
                        {
                            "frameNumber": 2,
                            "time": 10,
                            "data": [
                                1001.0,
                                1.0,
                                1.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                1.0,
                                15.0,
                                44.55,
                                33.97,
                                8.86,
                                36.63,
                                38.269999999999996,
                                4.51,
                                28.96,
                                43.28,
                                0.5,
                                21.83,
                                49.61,
                                -2.52,
                                16.0,
                                57.66,
                                -3.58,
                                1000.0,
                                12.0,
                                7.0,
                                -72.52,
                                -21.9,
                                -43.59,
                                0.0,
                                0.0,
                                0.0,
                                2.0,
                                0.0,
                            ],
                        },
                    ],
                },
                "plotData": {
                    "version": 1,
                    "data": [
                        {
                            "layout": {
                                "title": "Test Scatterplot 1",
                                "xaxis": {"title": "time (ns)"},
                                "yaxis": {"title": "concentration (uM)"},
                            },
                            "data": [
                                {
                                    "name": "agent1",
                                    "type": "scatter",
                                    "x": [
                                        0.0,
                                        100.0,
                                        200.0,
                                        300.0,
                                        400.0,
                                        500.0,
                                        600.0,
                                        700.0,
                                        800.0,
                                        900.0,
                                    ],
                                    "y": [
                                        74.0190301,
                                        40.35983437,
                                        21.29691538,
                                        93.67690109,
                                        24.54807229,
                                        58.38854845,
                                        11.19286985,
                                        27.28811308,
                                        18.89378287,
                                        34.53219224,
                                    ],
                                    "mode": "lines",
                                },
                                {
                                    "name": "agent2",
                                    "type": "scatter",
                                    "x": [
                                        0.0,
                                        100.0,
                                        200.0,
                                        300.0,
                                        400.0,
                                        500.0,
                                        600.0,
                                        700.0,
                                        800.0,
                                        900.0,
                                    ],
                                    "y": [
                                        89.85589674,
                                        9.10122431,
                                        40.23560224,
                                        67.5501959,
                                        30.36962677,
                                        13.04011962,
                                        26.98629198,
                                        66.03464652,
                                        66.05164469,
                                        7.00278548,
                                    ],
                                    "mode": "lines",
                                },
                                {
                                    "name": "agent3",
                                    "type": "scatter",
                                    "x": [
                                        0.0,
                                        100.0,
                                        200.0,
                                        300.0,
                                        400.0,
                                        500.0,
                                        600.0,
                                        700.0,
                                        800.0,
                                        900.0,
                                    ],
                                    "y": [
                                        24.60902276,
                                        12.88084466,
                                        52.99450258,
                                        85.68006617,
                                        26.16588002,
                                        36.35818642,
                                        77.19386492,
                                        9.83423903,
                                        23.2876747,
                                        58.56315023,
                                    ],
                                    "mode": "lines",
                                },
                            ],
                        },
                    ],
                },
            },
        ),
    ],
)
def test_multiply_time_filter(input_path, plot_data, _filter, expected_data):
    converter = FileConverter(input_path)
    converter.add_plot(plot_data, "scatter")
    filtered_data = converter.filter_data([_filter])
    buffer_data = converter._read_trajectory_data(filtered_data)
    assert expected_data == buffer_data
