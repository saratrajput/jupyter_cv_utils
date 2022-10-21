# Jupyter CV Utils

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://img.shields.io/badge/License-MIT-blue.svg)

This package contains utility functions to make life easier when using Jupyter notebooks.

## Installation

* With pip:
[Under construction]

* Editable mode:

    ```
    # Clone the repository.
    git clone https://github.com/saratrajput/jupyter_cv_utils.git

    cd jupyter_cv_utils/
    pip install -e .
    ```

## Usage

* Import package.

    ```
    import jupyter_cv_utils as jutils
    ```

* Install package.

    ```
    jutils.install("numpy")
    ```

* Show image in matplotlib fashion.

    ```
    jutils.imshow("numpy")
    ```

* Show image in OpenCV window.

    ```
    jutils.imshow_opencv("numpy")
    ```

* Reload a module.

    ```
    jutils.reload(<module_name>)
    ```
