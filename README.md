# Practical methods for Approximate Nearest Neighbor Search on non-Manhattan squares

Minas Dioletis, Ioannis Z. Emiris, George Ioannakis, Panagiotis Repouskos, Panagiotis Rigas, Charalampos Tzamos and Andreas Zamanos

## Table of Contents

- [Method](#Method)
- [Installation](#Installation)
- [Code Structure](#CD)
- [Getting Started](#getting_started)
- [License](#license)

<a id="Installation"></a>

## Installation

Clone the repository and install the requirements by running the following in your terminal:

```[BASH]
git clone https://github.com/PRigas96/nMANN
cd nMANN
conda env create -f environment.yml
source activate nmannv1
```

<a id="CD"></a>

## Code Structure

```
├─── data                          # directory for data used in experiments
│    ├── data_v1                   #   contains small sized data
│    ├── data_v2                   #   large sized data
│    └── ...                       #   helper functions
├─── dev                           # prototype src used for developement
├─── utils                         # main package
│    ├── data.py                   #   data creation functions
│    ├── geometry.py               #   geometric package
│    ├── kde.py                    #   kernel density estimation function
│    ├── metrics.py                #   L_{\infty} metric
│    ├── res.py                    #   result plot functions
│    ├── results.py                #   results related functions
│    └─── visualization.py         #   data for visualization
├─── demo.ipynb                    # demo notebook
└─── environment.yml               # enviroment of variables
```

<a id="getting_started"></a>

## Getting Started

### Demo

Use [demo](demo.ipynb) to experiment with the method

### Application

1. load a dataset and some querry points using:

    ```[Python]
    dataset = np.load('./your_path/your_data.npy')
    querry_points = np.load('./your_path/your_querry_points.npy')
    ```

2. Cluster the data:

    ```[Python]
    clustered_data, optimal_bandwidth, _ = kde.optimal_clustering(data)
    ```

3. Infere:

    ```[Python]
    nearest_neighbors = inference(clustered_data, querry_points)
    ```

<a id="license"></a>

## License

This project is licensed under the MIT License - see the LICENSE file for details.
