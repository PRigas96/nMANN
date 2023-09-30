# Practical methods for Approximate Nearest Neighbor Search on non-Manhattan squares

Minas Dioletis, Ioannis Z. Emiris, George Ioannakis, Panagiotis Repouskos, Panagiotis Rigas, Charalampos Tzamos and Andreas Zamanos

![header](/dev/other/images/pipelinecgta.png)

Figure: Illustration of the pipeline of our approach.


## Table of Contents

- [Method](#Method)
- [Installation](#Installation)
- [Code Structure](#CD)
- [Getting Started](#getting_started)
- [License](#license)

<a id="Method"></a>

## Method

Key points of our method are:
- Use of simple L<sub>&infin;</sub><sup>*</sup> for performance gain
- Unsupervised Learning to reduce error variability
- Plug-and-Play into any data structure
- Great scaling and higly parallelizable

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

### Input Data
To construct a square an initial point is required, serving as root (minimum x and y values before rotation), with specific length. Then, it is rotated by rotation angle (degrees).
```
[[x_0:double, y_0:double, length:double, rotation_in_degrees:double] ... ]
```

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
    online.inference(clustered_data, querry_points,'None')
    ```

<a id="license"></a>

## License

This project is licensed under the MIT License - see the LICENSE file for details.
