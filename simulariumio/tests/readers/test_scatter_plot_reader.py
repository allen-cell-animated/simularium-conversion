#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Dict, Any

import pytest
import numpy as np

from simulariumio import Converter, exceptions
from simulariumio.tests.conftest import three_default_agents


def test_scatter_plot() -> Dict[str, Any]:
    return {
        "title": "Test Scatterplot 1",
        "xaxis_title": "time (ns)",
        "yaxis_title": "concentration (uM)",
        "xtrace": np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]),
        "ytraces": {
            "agent1": np.array(
                [
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
                ]
            ),
            "agent2": np.array(
                [
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
                ]
            ),
            "agent3": np.array(
                [
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
                ]
            ),
        },
        "render_mode": "lines",
    }


@pytest.mark.parametrize(
    "trajectory, plot_data, expected_data",
    [
        # scatter plot with multiple y-traces
        (
            three_default_agents(),
            test_scatter_plot(),
            {
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
                                "x": [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0],
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
                                "x": [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0],
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
                                "x": [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0],
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
                    }
                ],
            },
        ),
        pytest.param(
            three_default_agents(),
            {
                "title": "Test Scatterplot 2",
                "xaxis_title": "time (ns)",
                "yaxis_title": "concentration (uM)",
                "ytraces": {
                    "agent1": [
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
                    ]
                },
                "render_mode": "lines",
            },
            {},
            marks=pytest.mark.raises(
                exception=KeyError
            ),  # input data is missing key 'xtrace'
        ),
        pytest.param(
            three_default_agents(),
            {
                "title": "Test Scatterplot 2",
                "xaxis_title": "time (ns)",
                "yaxis_title": "concentration (uM)",
                "xtrace": np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]),
                "ytraces": {
                    "agent1": np.array(
                        [
                            74.0190301,
                            40.35983437,
                            21.29691538,
                            93.67690109,
                            24.54807229,
                            58.38854845,
                            11.19286985,
                            27.28811308,
                            18.89378287,
                        ]
                    )
                },
                "render_mode": "lines",
            },
            {},
            marks=pytest.mark.raises(
                exception=exceptions.DataError
            ),  # length of y-trace (9) != length of x-trace (10)
        ),
    ],
)
def test_add_one_scatter_plot(trajectory, plot_data, expected_data):
    converter = Converter(trajectory)
    converter.add_plot(plot_data, "scatter")
    assert expected_data == converter._data["plotData"]


@pytest.mark.parametrize(
    "trajectory, plot_data1, plot_data2, expected_data",
    [
        (
            three_default_agents(),
            test_scatter_plot(),
            {
                "title": "Test Scatterplot 2",
                "xaxis_title": "time (ns)",
                "yaxis_title": "concentration (uM)",
                "xtrace": np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]),
                "ytraces": {
                    "agent20": np.array(
                        [
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
                        ]
                    )
                },
            },
            {
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
                                "x": [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0],
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
                                "x": [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0],
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
                                "x": [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0],
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
                    {
                        "layout": {
                            "title": "Test Scatterplot 2",
                            "xaxis": {"title": "time (ns)"},
                            "yaxis": {"title": "concentration (uM)"},
                        },
                        "data": [
                            {
                                "name": "agent20",
                                "type": "scatter",
                                "x": [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0],
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
                                "mode": "markers",
                            }
                        ],
                    },
                ],
            },
        ),
    ],
)
def test_add_two_scatter_plots(trajectory, plot_data1, plot_data2, expected_data):
    converter = Converter(trajectory)
    converter.add_plot(plot_data1, "scatter")
    converter.add_plot(plot_data2)  # default to scatter
    assert expected_data == converter._data["plotData"]