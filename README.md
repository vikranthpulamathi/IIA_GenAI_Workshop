# IIA GenAI Workshop Projects

This repository contains two astronomical analysis projects developed during the IIA GenAI Workshop:

## 1. Galaxy Rotation Curve Modeling

Located in `rotation_curves/`, this project implements a comprehensive model for spiral galaxy rotation curves, including:

### Features
- Exponential disk component (Freeman 1970)
- NFW dark matter halo profile
- Combined rotation curve analysis
- Professional visualization of components

### Key Components
- `src/galaxy_rotation.py`: Main modeling script
- Milky Way-like parameters by default
- Proper astropy unit handling
- Publication-quality plots

For detailed information, see [Rotation Curves Project Documentation](rotation_curves/README.md)

## 2. Astronomical Coordinate System Converter

Located in `astro_coords/`, this project provides tools for coordinate system conversion and visualization:

### Features
- Random celestial coordinate generation
- Multiple coordinate system transformations:
  - Equatorial (RA/Dec)
  - Galactic (l/b)
  - Ecliptic (lon/lat)
- Mollweide projection visualizations

### Key Components
- `generate_coords.py`: Main conversion script
- Professional plotting capabilities
- Data export in CSV format
- Comprehensive error handling

For detailed information, see [Astronomical Coordinates Project Documentation](astro_coords/README.md)

## Project Structure
```
IIA_GenAI/
├── rotation_curves/
│   ├── src/
│   │   └── galaxy_rotation.py
│   ├── plots/
│   │   └── rotation_curve.png
│   ├── README.md
│   └── plan.md
├── astro_coords/
│   ├── generate_coords.py
│   ├── data/
│   │   ├── initial_coordinates.csv
│   │   └── all_coordinates.csv
│   ├── plots/
│   │   └── coordinate_systems.png
│   ├── README.md
│   └── plan.md
└── README.md
```

## Dependencies

Both projects use common Python astronomical and scientific libraries:
- numpy
- astropy
- matplotlib
- scipy
- pandas (for coordinate project)

## Installation

```bash
# Clone the repository
git clone https://github.com/vikranthpulamathi/IIA_GenAI_Workshop.git
cd IIA_GenAI_Workshop

# Install required packages
pip install numpy astropy matplotlib scipy pandas
```

## Usage

### Galaxy Rotation Curves
```python
# Navigate to rotation_curves/src
cd rotation_curves/src
python galaxy_rotation.py
```

### Coordinate Conversion
```python
# Navigate to astro_coords
cd astro_coords
python generate_coords.py
```

## Development Plans

Each project has its own detailed development plan in its respective `plan.md` file:
- [Rotation Curves Development Plan](rotation_curves/plan.md)
- [Coordinate Systems Development Plan](astro_coords/plan.md)

## Contributing

Feel free to open issues or submit pull requests for improvements or bug fixes.

## License

These projects are part of the IIA GenAI Workshop. Please check with the workshop organizers for usage permissions.
