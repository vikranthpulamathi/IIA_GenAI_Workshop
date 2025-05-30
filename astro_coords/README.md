# Astronomical Coordinate System Converter

This project generates random celestial coordinates and converts them between different astronomical coordinate systems using the Astropy library. It demonstrates the transformation between Equatorial (RA/Dec), Galactic, and Ecliptic coordinate systems, and creates visualizations using Mollweide projections.

## Features

- Generates random RA (Right Ascension) and Dec (Declination) coordinates
- Converts coordinates between three astronomical coordinate systems:
  - Equatorial (RA/Dec)
  - Galactic (l/b)
  - Ecliptic (lon/lat)
- Creates Mollweide projection plots for all three coordinate systems
- Saves coordinate data in CSV format
- Generates high-quality visualization plots

## Requirements

- Python 3.8+
- Required Python packages:
  - astropy
  - matplotlib
  - numpy
  - pandas

## Installation

1. Clone or download this repository
2. Install the required packages:

```bash
pip install astropy matplotlib numpy pandas
```

## Project Structure

```
astro_coords/
├── data/                  # Directory for CSV files
├── plots/                # Directory for generated plots
├── generate_coords.py    # Main Python script
└── README.md            # This file
```

## Usage

1. Run the main script:

```bash
python generate_coords.py
```

This will:
- Generate 100 random RA/Dec coordinates
- Save the initial coordinates to `data/initial_coordinates.csv`
- Convert the coordinates to Galactic and Ecliptic systems
- Save all coordinates to `data/all_coordinates.csv`
- Create Mollweide projection plots in `plots/coordinate_systems.png`

## Output Files

- `data/initial_coordinates.csv`: Original RA/Dec coordinates
- `data/all_coordinates.csv`: All coordinate systems (Equatorial, Galactic, Ecliptic)
- `plots/coordinate_systems.png`: Mollweide projection visualizations

## Development Notes

The code is organized in a modular way with separate functions for:
- Coordinate generation
- Coordinate system conversion
- Data saving
- Visualization creation

Error handling is implemented throughout the code to ensure robust execution.

## License

This project is open source and available under the MIT License.
