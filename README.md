# Practical methods for Approximate Nearest Neighbor Search on non-Manhattan squares

Minas Dioletis, Ioannis Z. Emiris, George Ioannakis, Panagiotis Rigas, Charalampos Tzamos and Andreas Zamanos

## Installation

Clone the repository and install the requirements:

```
git clone https://github.com/PRigas96/NMANNv1
cd NMANNv1
conda env create -f environment.yml
source activate deep3d_pytorch
```

## Usage

go to demo folder and infer with the code

## Files

- `demo/`: contains the code for the demo

```
nmannv1
│
└─── data
    │
    └─── data_v1 (contains the data)
    │
    └─── data_v2 (contains the data)
    │
    └─── ...
│
└─── jup_not (contains prototype jupyter notebooks)
│
└─── other (contains other files)
│
└─── utils (contains utility functions)
     │
     └─── data.py (contains functions for data creation)
     │
     └─── geometry.py (contains functions for geometry)
     │
     └───  kde.py (contains functions for kernel density estimation)
     │
     └─── metrics.py (contains functions for metrics)
     │
     └─── res.py (contains result plot functions)
     │
     └─── results.py (contains functions for results)
     │
     └─── visualization.py (contains functions for visualization)
```
