import numpy as np
from astropy import units as u
from astropy import constants as const
import matplotlib.pyplot as plt
from scipy.special import i0, i1, k0, k1

class GalaxyModel:
    """
    A class to model the rotation curve of a spiral galaxy with disk and halo components.
    
    Parameters
    ----------
    disk_mass : astropy.units.Quantity
        Total mass of the disk in solar masses
    disk_scale_length : astropy.units.Quantity
        Scale length of the disk in kpc
    halo_scale_radius : astropy.units.Quantity
        Scale radius of the NFW halo in kpc
    halo_concentration : float
        Concentration parameter of the NFW halo
    halo_mass : astropy.units.Quantity
        Virial mass of the dark matter halo in solar masses
    """
    
    def __init__(self, disk_mass=5e10*u.Msun, disk_scale_length=3*u.kpc,
                 halo_scale_radius=20*u.kpc, halo_concentration=12,
                 halo_mass=1e12*u.Msun):
        self.disk_mass = disk_mass
        self.disk_scale_length = disk_scale_length
        self.halo_scale_radius = halo_scale_radius
        self.halo_concentration = halo_concentration
        self.halo_mass = halo_mass
        
        # Derived parameters
        self.G = const.G.to(u.kpc * u.km**2 / u.s**2 / u.Msun)

    def disk_velocity(self, radius):
        """
        Calculate the rotation velocity due to the exponential disk at a given radius.
        Based on Freeman (1970) disk solution.
        
        Parameters
        ----------
        radius : astropy.units.Quantity
            Radial distance from center in kpc
            
        Returns
        -------
        v_disk : astropy.units.Quantity
            Circular velocity contribution from the disk in km/s
        """
        # Convert radius to dimensionless units
        y = (radius / (2 * self.disk_scale_length)).decompose()
        
        try:
            # Freeman (1970) solution
            v_disk_squared = (4 * np.pi * const.G * self.disk_mass * 
                            y**2 * (i0(y) * k0(y) - i1(y) * k1(y)) / 
                            (self.disk_scale_length))
            
            return np.sqrt(v_disk_squared).to(u.km/u.s)
        except ValueError as e:
            print(f"Error in disk velocity calculation: {e}")
            return np.zeros_like(radius) * u.km/u.s

    def nfw_velocity(self, radius):
        """
        Calculate the rotation velocity due to the NFW dark matter halo.
        
        Parameters
        ----------
        radius : astropy.units.Quantity
            Radial distance from center in kpc
            
        Returns
        -------
        v_halo : astropy.units.Quantity
            Circular velocity contribution from the halo in km/s
        """
        x = (radius / self.halo_scale_radius).decompose()
        
        try:
            # NFW circular velocity equation
            v_halo_squared = (const.G * self.halo_mass / self.halo_scale_radius * 
                            (np.log(1 + x) - x/(1 + x)) /
                            (np.log(1 + self.halo_concentration) - 
                             self.halo_concentration/(1 + self.halo_concentration)))
            
            return np.sqrt(v_halo_squared).to(u.km/u.s)
        except ValueError as e:
            print(f"Error in halo velocity calculation: {e}")
            return np.zeros_like(radius) * u.km/u.s

    def total_velocity(self, radius):
        """
        Calculate the total rotation velocity at a given radius.
        
        Parameters
        ----------
        radius : astropy.units.Quantity
            Radial distance from center in kpc
            
        Returns
        -------
        v_total : astropy.units.Quantity
            Total circular velocity in km/s
        """
        v_disk = self.disk_velocity(radius)
        v_halo = self.nfw_velocity(radius)
        
        # Add contributions in quadrature
        return np.sqrt(v_disk**2 + v_halo**2)

    def plot_rotation_curve(self, r_max=30*u.kpc, n_points=100):
        """
        Plot the rotation curve components and total.
        
        Parameters
        ----------
        r_max : astropy.units.Quantity
            Maximum radius for plotting
        n_points : int
            Number of points to calculate
        """
        r = np.linspace(0.1, r_max.value, n_points) * u.kpc
        
        v_disk = self.disk_velocity(r)
        v_halo = self.nfw_velocity(r)
        v_total = self.total_velocity(r)
        
        plt.figure(figsize=(10, 6))
        plt.plot(r.value, v_disk.value, '--', label='Disk')
        plt.plot(r.value, v_halo.value, ':', label='Dark Matter Halo')
        plt.plot(r.value, v_total.value, '-', label='Total')
        
        plt.xlabel('Radius (kpc)')
        plt.ylabel('Rotation Velocity (km/s)')
        plt.title('Galaxy Rotation Curve')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        # Save the plot
        plt.savefig('../plots/rotation_curve.png', dpi=300, bbox_inches='tight')
        plt.close()

def main():
    """
    Main function to demonstrate the galaxy rotation curve model.
    """
    # Create a Milky Way-like galaxy model
    galaxy = GalaxyModel(
        disk_mass=5e10 * u.Msun,
        disk_scale_length=3 * u.kpc,
        halo_scale_radius=20 * u.kpc,
        halo_concentration=12,
        halo_mass=1e12 * u.Msun
    )
    
    # Generate and save the rotation curve plot
    galaxy.plot_rotation_curve()

if __name__ == "__main__":
    main()
