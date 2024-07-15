# Geo Zip

Geo Zip is a Python package that provides a fast and efficient way to find the closest US ZIP code for a given latitude and longitude. It uses a KDTree for quick nearest-neighbor lookup, making it suitable for geospatial queries.

## Features

- Quickly find the closest ZIP code for a given latitude and longitude.
- Efficient spatial indexing using KDTree.
- Easy-to-use command-line interface.

## Installation

### Prerequisites

- Python 3.7 or higher
- pip

### Install the package

1. Clone the repository:
    ```sh
    git clone https://github.com/jlopex/geo-zip.git
    cd geo-zip
    ```

2. Install the package and its dependencies:
    ```sh
    pip install -e .
    ```

3. Install development dependencies (for testing):
    ```sh
    pip install -e .[dev]
    ```

## Usage

### Command Line Interface

You can use the `geo-zip` command to find the closest ZIP code for a given latitude and longitude.

```sh
geo-zip <latitude> <longitude>
```

Example:

```sh
geo-zip 37.7749 -122.4194
```

This command will output the closest ZIP code to the provided coordinates.

### As a Python Library
You can also use the GeoZip class directly in your Python code:

```python
from geo_zip import GeoZip

# Initialize with the path to your data file
geo_zip = GeoZip('path/to/geo_zip/data/geo_zip.csv')

# Find the closest ZIP code
latitude = 37.7749
longitude = -122.4194
closest_zip = geo_zip.find_closest_zip(latitude, longitude)
print(f"The closest ZIP code to ({latitude}, {longitude}) is {closest_zip}")
```

### Data

The dataset used for ZIP codes and their coordinates is extracted from the [2023 US Gazetteer Files](https://www2.census.gov/geo/docs/maps-data/data/gazetteer/2023_Gazetteer/2023_Gaz_zcta_national.zip). The CSV file is included in the package at geo_zip/data/geo_zip.csv.

### Testing

Simple and stupid Tests are written using pytest. To run the tests, execute the following command:

```sh
pytest tests/
```

