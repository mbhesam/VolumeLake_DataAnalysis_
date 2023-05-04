"""

"""
import numpy as np


class WaterLevel:
    """
    Author: Navid
    """
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.my_data = np.loadtxt(self.csv_file, dtype=str, delimiter=',', skiprows=0)

    def max_water_alpha_lake(self):
        """
        :return: maximum of water level of alpha lake 
        """
        return self.my_data[self.my_data[:, 0] == 'ZO', :][0][2]

    def min_water_alpha_lake(self):
        """
        :return: minimum of water level of alpha lake
        """
        return self.my_data[self.my_data[:, 0] == 'ZA', :][0][2]

    def bottom_outlet(self):
        """
        :return: level of bottom outlet  
        """
        return self.my_data[self.my_data[:, 0] == 'ZT', :][0][2]

    def annual_storage_volume(self, pump_volume):
        """
        :param pump_volume: entry of pumping volume
        :return: calculate anual storage
        """
        volume_max_height = self.my_data[self.my_data[:, 0] == 'ZO', :][0][3]
        volume_min_height = self.my_data[self.my_data[:, 0] == 'ZA', :][0][3]
        return int(volume_max_height) - int(volume_min_height) - int(pump_volume)
