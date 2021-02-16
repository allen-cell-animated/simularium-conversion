#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import pytest

from simulariumio.medyan import MedyanConverter, MedyanData, MedyanAgentInfo


@pytest.mark.parametrize(
    "trajectory, expected_data",
    [
        # truncated data from 50filaments_motor_linker example
        (
            MedyanData(
                box_size=np.array([1000.0, 1000.0, 500.0]),
                path_to_snapshot="simulariumio/tests/data/medyan/snapshot.traj",
                filament_agent_info={
                    0 : MedyanAgentInfo(
                        name="Actin",
                        radius=2,
                    ),
                },
                linker_agent_info={
                    1 : MedyanAgentInfo(
                        name="Xlink",
                        radius=0.5,
                    ),
                },
            ),
            {
                "trajectoryInfo": {
                    "version": 1,
                    "timeStepSize": 1.0,
                    "totalSteps": 3,
                    "spatialUnitFactorMeters": 1e-6,
                    "size": {"x": 1000.0, "y": 1000.0, "z": 500.0},
                    "typeMapping": {
                        "0": {"name": "Actin"},
                        "1": {"name": "linker0"},
                        "2": {"name": "Xlink"},
                        "3": {"name": "linker2"},
                        "4": {"name": "motor1"},
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
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                2.0,
                                6.0,
                                454.34,
                                363.44,
                                265.44,
                                519.74,
                                351.57,
                                180.31,
                                1001.0,
                                1.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                2.0,
                                6.0,
                                547.59,
                                280.31,
                                307.413,
                                535.19,
                                173.03,
                                308.94,
                            ],
                        },
                        {
                            "frameNumber": 1,
                            "time": 1.0,
                            "data": [
                                1001.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                2.0,
                                18.0,
                                443.32,
                                369.86,
                                293.15,
                                458.46,
                                366.54,
                                274.44,
                                525.51,
                                351.31,
                                191.16,
                                595.42,
                                336.64,
                                110.17,
                                672.52,
                                322.31,
                                35.94,
                                678.31,
                                321.24,
                                30.38,
                                1001.0,
                                1.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                2.0,
                                15.0,
                                549.76,
                                310.76,
                                302.03,
                                547.77,
                                286.58,
                                303.35,
                                537.95,
                                179.24,
                                309.54,
                                518.82,
                                73.13,
                                314.87,
                                509.99,
                                28.15,
                                317.04,
                                1000.0,
                                2.0,
                                1.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                1.0,
                                6.0,
                                216.80,
                                854.81,
                                302.91,
                                191.27,
                                867.60,
                                281.47,
                                1001.0,
                                3.0,
                                2.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.5,
                                6.0,
                                657.33,
                                421.49,
                                212.73,
                                662.17,
                                436.29,
                                182.61,
                                1001.0,
                                4.0,
                                3.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                1.0,
                                6.0,
                                639.80,
                                430.99,
                                162.56,
                                670.93,
                                411.16,
                                178.07,
                                1001.0,
                                5.0,
                                4.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                1.0,
                                6.0,
                                541.39,
                                216.81,
                                307.37,
                                584.60,
                                412.76,
                                381.26,
                            ],
                        },
                        {
                            "frameNumber": 2,
                            "time": 2.0,
                            "data": [
                                1001.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                2.0,
                                18.0,
                                419.36,
                                381.11,
                                315.85,
                                446.74,
                                375.82,
                                282.85,
                                516.31,
                                361.27,
                                201.54,
                                592.96,
                                344.26,
                                127.40,
                                679.15,
                                328.7,
                                64.23,
                                728.03,
                                320.52,
                                1.49,
                                1001.0,
                                2.0,
                                1.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                1.0,
                                6.0,
                                219.59,
                                861.72,
                                300.84,
                                190.20,
                                868.62,
                                282.81,
                                1001.0,
                                3.0,
                                2.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.5,
                                6.0,
                                655.54,
                                417.83,
                                217.17,
                                669.71,
                                432.94,
                                190.79,
                                1001.0,
                                6.0,
                                1.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                1.0,
                                6.0,
                                748.61,
                                312.05,
                                295.82,
                                713.24,
                                307.88,
                                295.63,
                                1001.0,
                                7.0,
                                3.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                1.0,
                                6.0,
                                543.47,
                                148.88,
                                277.89,
                                529.89,
                                146.61,
                                312.42,
                                1001.0,
                                5.0,
                                4.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                1.0,
                                6.0,
                                610.41,
                                152.61,
                                304.31,
                                433.00,
                                229.76,
                                191.64,
                                1001.0,
                                8.0,
                                4.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                1.0,
                                6.0,
                                668.84,
                                523.90,
                                357.10,
                                721.95,
                                345.97,
                                427.52,
                            ],
                        },
                    ],
                },
                "plotData": {"version": 1, "data": []},
            },
        ),
    ],
)
def test_cytosim_trajectory_reader(trajectory, expected_data):
    converter = MedyanConverter(trajectory)
    assert expected_data == converter._data
    assert converter._check_agent_ids_are_unique_per_frame()