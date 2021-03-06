## Simularium repositories
This repository is part of the Simularium project ([simularium.allencell.org](https://simularium.allencell.org)), which includes repositories:
- [simulariumIO](https://github.com/allen-cell-animated/simulariumio) - Python package that converts simulation outputs to the format consumed by the Simularium viewer website
- [simularium-engine](https://github.com/allen-cell-animated/simularium-engine) - C++ backend application that interfaces with biological simulation engines and serves simulation data to the front end website
- [simularium-viewer](https://github.com/allen-cell-animated/simularium-viewer) - NPM package to view Simularium trajectories in 3D
- [simularium-website](https://github.com/allen-cell-animated/simularium-website) - Front end website for the Simularium project, includes the Simularium viewer

---

# SimulariumIO

[![Build Status](https://github.com/allen-cell-animated/simulariumio/workflows/Build%20Master/badge.svg)](https://github.com/allen-cell-animated/simulariumio/actions)
[![Documentation](https://github.com/allen-cell-animated/simulariumio/workflows/Documentation/badge.svg)](https://allen-cell-animated.github.io/simulariumio)
[![Code Coverage](https://codecov.io/gh/allen-cell-animated/simulariumio/branch/master/graph/badge.svg)](https://codecov.io/gh/allen-cell-animated/simulariumio)

Simulariumio converts simulation outputs to the format consumed by the [Simularium viewer](https://simularium.allencell.org/).

---

## Features
* Converts 3D spatiotemporal trajectories to .simularium JSON format
* Accepts spatial trajectories from the following biological simulation engines:
    * CytoSim (https://gitlab.com/f.nedelec/cytosim)
    * ReaDDy (https://readdy.github.io/)
    * PhysiCell (http://physicell.org/)
* Conversions for data from custom engines can be implemented using the TrajectoryConverter class
* Also accepts metrics data for plots to display alongside spatial data

We're working to improve performance for converting large trajectories, and also discussing with the authors of some packages the possibility of adding the ability to export Simularium files directly.

___

## Quick Start

### Convert spatial trajectory from a supported engine
See the Tutorial for the simulation engine you're using for details:
* [Cytosim Tutorial](examples/Tutorial_cytosim.ipynb)
* [ReaDDy Tutorial](examples/Tutorial_readdy.ipynb)
* [PhysiCell Tutorial](examples/Tutorial_physicell.ipynb)

An overview for data from ReaDDy:
```python
from simulariumio.readdy import ReaddyConverter, ReaddyData

# see ReaDDy Tutorial for parameter details
input_data = ReaddyData(
    spatial_unit_factor_meters=1e-9,  # nanometers
    box_size=BOX_SIZE,
    timestep=TIMESTEP,  # seconds
    path_to_readdy_h5=PATH_TO_H5_FILE,
)
ReaddyConverter(input_data).write_JSON("output_file_name")
```

### Convert spatial trajectory from a custom engine
See the [Custom Data Tutorial](examples/Tutorial_custom.ipynb) for details. An overview:
```python
from simulariumio import TrajectoryConverter, TrajectoryData, AgentData

# see Custom Data Tutorial for parameter details
input_data = TrajectoryData(  
    spatial_unit_factor_meters=1e-9,  # nanometers
    box_size=BOX_SIZE,
    agent_data=AgentData(
        times=TIMES,  # seconds
        n_agents=N_AGENTS,
        viz_types=VIZ_TYPES,
        unique_ids=UNIQUE_IDS,
        types=TYPE_IDS,
        positions=POSITIONS,
        radii=RADII,
    )
)
TrajectoryConverter(input_data).write_JSON("output_file_name")
```

### Add metrics data to plot
See the [Plots Tutorial](examples/Tutorial_plots.ipynb) for details. An overview:
```python
from simulariumio import ScatterPlotData

# see Plots Tutorial for parameter details
example_scatter_plot = ScatterPlotData(
    title=TITLE,
    xaxis_title=X_TITLE,
    yaxis_title=Y_TITLE,
    xtrace=X_VALUES,
    ytraces=Y_VALUES,
)
converter = TrajectoryConverter(input_data) # see above to create converter
converter.add_plot(example_scatter_plot, "scatter")
converter.write_JSON("output_file_name")
```
___

## Installation
**Install Requires:** 

* Requires Python 3.7 or 3.8

* If ReaDDy trajectories will be converted, the ReaDDy python package must be installed:
(add conda forge channel if it's not already: `conda config --add channels conda-forge`)
`conda install -c readdy readdy`

**Stable Release:** `pip install simulariumio`

**Development Head:** `pip install git+https://github.com/allen-cell-animated/simulariumio.git`

___

## Documentation
For full package documentation please visit [allen-cell-animated.github.io/simulariumio](https://allen-cell-animated.github.io/simulariumio).

___

## Development
See [CONTRIBUTING.md](CONTRIBUTING.md) for information related to developing the code.

