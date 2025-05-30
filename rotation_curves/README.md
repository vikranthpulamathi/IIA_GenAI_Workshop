# Galaxy Rotation Curve Modeling

This project provides tools for modeling and visualizing the rotation curves of spiral galaxies, incorporating both the stellar disk and dark matter halo components.

## Physical Background

Galaxy rotation curves show how the circular velocity of stars and gas varies with distance from the galactic center. The observed flat rotation curves of spiral galaxies provided some of the first evidence for dark matter.

### Components Modeled

1. **Exponential Disk**
   - Follows Freeman (1970) disk model
   - Surface density profile: Σ(R) = Σ₀ exp(-R/Rd)
   - Uses modified Bessel functions for exact solution
   - Parameters: Total mass and scale length

2. **Dark Matter Halo**
   - Uses NFW (Navarro-Frenk-White) profile
   - Density profile: ρ(r) = ρ₀ / [(r/rs)(1 + r/rs)²]
   - Parameters: Scale radius, concentration, and virial mass

### Mathematical Models

The total rotation curve is calculated by adding the contributions from each component in quadrature:

V_total² = V_disk² + V_halo²

## Requirements

- Python 3.7+
- NumPy
- Astropy
- Matplotlib
- SciPy

Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

The main script is in `src/galaxy_rotation.py`. It provides a `GalaxyModel` class with methods for calculating and plotting rotation curves.

Basic usage:
```python
from galaxy_rotation import GalaxyModel
from astropy import units as u

# Create a Milky Way-like galaxy model
galaxy = GalaxyModel(
    disk_mass=5e10 * u.Msun,
    disk_scale_length=3 * u.kpc,
    halo_scale_radius=20 * u.kpc,
    halo_concentration=12,
    halo_mass=1e12 * u.Msun
)

# Generate and save rotation curve plot
galaxy.plot_rotation_curve()
```

## Output

The script generates a plot showing:
- Disk component contribution (dashed line)
- Dark matter halo contribution (dotted line)
- Total rotation curve (solid line)

The plot is saved as `plots/rotation_curve.png`.

## References

1. Freeman, K. C. (1970) "On the Disks of Spiral and S0 Galaxies"
2. Navarro, J. F., Frenk, C. S., & White, S. D. M. (1996) "The Structure of Cold Dark Matter Halos"
