#!/usr/bin/env python3
"""
Astronomical Coordinate System Converter and Visualizer

This script generates random celestial coordinates and converts them between
different coordinate systems (Equatorial, Galactic, and Ecliptic) using astropy.
It also creates visualization plots using matplotlib.
"""

import numpy as np
import pandas as pd
from astropy.coordinates import SkyCoord
import astropy.units as u
import matplotlib.pyplot as plt
from pathlib import Path

def generate_random_coordinates(n=100):
    """Generate n random RA/Dec coordinates."""
    ra = np.random.uniform(0, 360, n)  # RA between 0 and 360 degrees
    dec = np.random.uniform(-90, 90, n)  # Dec between -90 and +90 degrees
    return ra, dec

def convert_coordinates(ra, dec):
    """Convert RA/Dec coordinates to Galactic and Ecliptic."""
    # Create SkyCoord object with RA/Dec (ICRS frame is the default)
    coords = SkyCoord(ra=ra*u.degree, dec=dec*u.degree)
    
    # Convert to Galactic coordinates
    galactic = coords.galactic
    
    # Convert to Ecliptic coordinates
    ecliptic = coords.barycentrictrueecliptic
    
    return coords, galactic, ecliptic

def save_coordinates(coords, galactic, ecliptic, filename):
    """Save all coordinate systems to a CSV file."""
    data = {
        'RA_deg': coords.ra.deg,
        'Dec_deg': coords.dec.deg,
        'Galactic_l_deg': galactic.l.deg,
        'Galactic_b_deg': galactic.b.deg,
        'Ecliptic_lon_deg': ecliptic.lon.deg,
        'Ecliptic_lat_deg': ecliptic.lat.deg
    }
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    return df

def create_mollweide_plot(coords, galactic, ecliptic, output_file):
    """Create a Mollweide projection plot for all three coordinate systems."""
    fig = plt.figure(figsize=(15, 10))
    
    # Convert all longitudes to range [-180, 180] for Mollweide projection
    ra_plot = coords.ra.wrap_at(180*u.deg).radian
    dec_plot = coords.dec.radian
    
    gal_l_plot = galactic.l.wrap_at(180*u.deg).radian
    gal_b_plot = galactic.b.radian
    
    ecl_lon_plot = ecliptic.lon.wrap_at(180*u.deg).radian
    ecl_lat_plot = ecliptic.lat.radian
    
    # Create three subplots
    plt.subplot(311, projection='mollweide')
    plt.grid(True)
    plt.scatter(ra_plot, dec_plot, alpha=0.5, label='Equatorial')
    plt.title('Equatorial Coordinates (RA/Dec)')
    plt.legend()
    
    plt.subplot(312, projection='mollweide')
    plt.grid(True)
    plt.scatter(gal_l_plot, gal_b_plot, alpha=0.5, color='red', label='Galactic')
    plt.title('Galactic Coordinates (l/b)')
    plt.legend()
    
    plt.subplot(313, projection='mollweide')
    plt.grid(True)
    plt.scatter(ecl_lon_plot, ecl_lat_plot, alpha=0.5, color='green', label='Ecliptic')
    plt.title('Ecliptic Coordinates (lon/lat)')
    plt.legend()
    
    plt.tight_layout()
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.close()

def main():
    """Main function to execute the coordinate generation and conversion workflow."""
    # Create directories if they don't exist
    data_dir = Path('data')
    plots_dir = Path('plots')
    data_dir.mkdir(exist_ok=True)
    plots_dir.mkdir(exist_ok=True)
    
    try:
        # Generate random coordinates
        print("Generating random coordinates...")
        ra, dec = generate_random_coordinates(100)
        
        # Save initial coordinates
        pd.DataFrame({'RA': ra, 'Dec': dec}).to_csv(
            data_dir / 'initial_coordinates.csv', 
            index=False
        )
        
        # Convert coordinates
        print("Converting coordinates between systems...")
        coords, galactic, ecliptic = convert_coordinates(ra, dec)
        
        # Save all coordinates
        print("Saving coordinates to CSV...")
        save_coordinates(
            coords, galactic, ecliptic,
            data_dir / 'all_coordinates.csv'
        )
        
        # Create visualization
        print("Creating Mollweide projection plots...")
        create_mollweide_plot(
            coords, galactic, ecliptic,
            plots_dir / 'coordinate_systems.png'
        )
        
        print("Process completed successfully!")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        raise

if __name__ == '__main__':
    main()
