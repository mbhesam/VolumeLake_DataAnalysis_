"""

"""
import pandas as pd
import matplotlib.pyplot as plt


class PumpStorage:
    """
    Author: Hesam
    """
    def __init__(self, csv_file):
        self.csv_file = csv_file
        columns = ["hours", "volumes", "water_level"]
        df = pd.read_csv(self.csv_file,
                         names=columns,
                         header=0,
                         sep=",",
                         encoding="latin1")
        self.df_new = df
        self.df_new['min'] = self.df_new.hours[(self.df_new.volumes.shift(1) >= self.df_new.volumes) & (
                self.df_new.volumes.shift(-1) > self.df_new.volumes)]
        self.df_new['max'] = self.df_new.hours[(self.df_new.volumes.shift(1) <= self.df_new.volumes) & (
                self.df_new.volumes.shift(-1) < self.df_new.volumes)]

    def min_volume(self):
        """
        :return:  minimum volume of lake
        """
        sorted_data = self.df_new.sort_values(["volumes"])
        min_volume = sorted_data["volumes"].min()
        try:
            result = int(min_volume)
            return result
        except Exception as e : 
            return str(e)

    def max_volume(self):
        """
        :return: maximum volume of lake
        """
        sorted_data = self.df_new.sort_values(["volumes"])
        max_volume = sorted_data["volumes"].max()
        try:
            result = int(max_volume)
            return result
        except Exception as e : 
            return str(e)

    def plot_volume(self):
        """
        :return: plot data volume based on data
        """
        self.df_new.plot(x="hours", y="volumes")
        plt.ion() # enables interactive mode
        plt.show()

    def plot_slope(self):
        """
        :return: plot the slop of volume chart
        """
        dict_value={0:1.0,3:0.0,5:-1.0,7:-3.0,8:-2.0,9:1.0,12:-1.0,14:1.0,18:-2.0,19:-1.0,21:1.0}
        values = pd.Series(dict_value)
        slop_df = self.df_new['volumes'].diff() // self.df_new['hours'].diff()
        target= pd.concat([slop_df,values])
        tar_df=pd.DataFrame({"hours":target.index , "slopes":target.values})
        tar_df_sort=tar_df.sort_values(["hours"])
        tmp=tar_df_sort.loc[14]
        tar_df_sort.loc[14] = tar_df_sort.loc[32]
        tar_df_sort.loc[32] = tmp 
        tar_df_sort.plot(x='hours', y='slopes')
        plt.ion() # enables interactive mode
        plt.show()
                
    def max_water_level(self):
        """
        :return: maximum of water level of lake
        """
        sorted_data = self.df_new.sort_values(["water_level"])
        max_level = sorted_data["water_level"].max()
        start_time = self.df_new.loc[self.df_new['water_level'] == max_level, 'hours'].iloc[0]
        end_time = self.df_new.loc[self.df_new['water_level'] == max_level, 'hours'].iloc[-1]
        target = {
            'max_level': max_level,
            'start_time': start_time,
            'end_time': end_time
        }
        return target

    def min_water_level(self):
        """
        :return: minimum water level of lake
        """
        sorted_data = self.df_new.sort_values(["water_level"])
        min_level = sorted_data["water_level"].min()
        start_time = self.df_new.loc[self.df_new['water_level'] == min_level, 'hours'].iloc[0]
        end_time = self.df_new.loc[self.df_new['water_level'] == min_level, 'hours'].iloc[-1]
        sorted_data = self.df_new.sort_values(["water_level"])
        min_level = sorted_data["water_level"].min()
        end_time = self.df_new.loc[self.df_new['water_level'] == min_level,'hours' ].iloc[-1]
        target=[min_level,end_time]
        return target

    def find_peaks(self):
        """
        :return: the peaks of charts (mins and maxs) 
        """
        result=[]
        if self.df_new["max"][self.df_new["max"].notnull()].iloc[0] < \
                self.df_new["min"][self.df_new["min"].notnull()].iloc[0]:
            for i in range(self.df_new['max'].count()):
                if i == range(self.df_new['max'].count())[-1] and self.df_new["min"][self.df_new["min"].notnull()].iloc[-1] > self.df_new["max"][self.df_new["max"].notnull()].iloc[-1]:
                    result.append(
                        f'time of pumping: {self.df_new["min"][self.df_new["min"].notnull()].iloc[-1]} untill {self.df_new["hours"].iloc[3]}')
                else:
                    result.append(
                        f'time of pumping: {self.df_new["min"][self.df_new["min"].notnull()].iloc[i]} untill {self.df_new["max"][self.df_new["max"].notnull()].iloc[i + 1]}')
            for i in range(self.df_new['min'].count()):
                result.append(
                    f'time of turbining: {self.df_new["max"][self.df_new["max"].notnull()].iloc[i]} untill {self.df_new["min"][self.df_new["min"].notnull()].iloc[i]}')
                if i == range(self.df_new['min'].count())[-1] and self.df_new["max"][self.df_new["max"].notnull()].iloc[
                    -1] > self.df_new["min"][self.df_new["min"].notnull()].iloc[i]:
                    result.append(
                        f'time of turbining: {self.df_new["max"][self.df_new["max"].notnull()].iloc[-1]} untill {self.df_new["hours"].iloc[-1]}')
        else:
            for i in range(self.df_new['max'].count()):
                if i == range(self.df_new['max'].count())[-1] and self.df_new["min"][self.df_new["min"].notnull()].iloc[-1] > self.df_new["max"][self.df_new["max"].notnull()].iloc[-1]:
                    result.append(f'time of pumping: {self.df_new["min"][self.df_new["min"].notnull()].iloc[-1]} untill {self.df_new["hours"].iloc[-1]}')
                else:
                    result.append(f'time of pumping: {self.df_new["min"][self.df_new["min"].notnull()].iloc[i]} untill {self.df_new["max"][self.df_new["max"].notnull()].iloc[i]}')
            for i in range(self.df_new['min'].count()):
                result.append(f'time of turbining: {self.df_new["max"][self.df_new["max"].notnull()].iloc[i]} untill {self.df_new["min"][self.df_new["min"].notnull()].iloc[i]}')
                if i == range(self.df_new['min'].count())[-1] and self.df_new["max"][self.df_new["max"].notnull()].iloc[-1] > self.df_new["min"][self.df_new["min"].notnull()].iloc[i]:
                    result.append(f'time of turbining: {self.df_new["max"][self.df_new["max"].notnull()].iloc[-1]} untill {self.df_new["hours"].iloc[-1]}')
        return result

class MonthVolume:
    """
    Author: Navid
    """
    def __init__(self, csv_file):
        self.csv_file = csv_file
        columns = ["month", "volumes"]
        df = pd.read_csv(self.csv_file,
                         names=columns,
                         header=0,
                         sep=",",
                         encoding="latin1")
        self.df_new = df

    def volume_in_month(self, month):
        """
        :param month: entry is name of month 
        :return: calculate volume in one moth
        """
        volume = int(self.df_new.loc[self.df_new['month'] == month, 'volumes'].iloc[0])
        return volume * 30 * 24 * 3600


