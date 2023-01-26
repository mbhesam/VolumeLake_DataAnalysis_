"""

"""
from reservoir.pump_storage import PumpStorage, MonthVolume
from reservoir.water_level import WaterLevel
from config import CSV_PATH, CONSTANT
from graphics import *


win = GraphWin("Graphic Result",1850,800)
win.setBackground("gray")

if __name__ == '__main__':

    # read data from data directory
    pump_storage = PumpStorage(CSV_PATH['reservoir'])
    water_level = WaterLevel(CSV_PATH['water_level'])
    month_volume = MonthVolume(CSV_PATH['inflow_alpha_creek'])
    with open("result.txt" , "w") as writer:
        
        # the pump storage volume in the Pool Beta
        try:
            pump_volume = pump_storage.max_volume() - pump_storage.min_volume()
            result1=f"*** Solution 1 ***\nvolume of pool Beta is: {pump_volume} Mio.m³"
            Text(Point(920,100),result1).draw(win)
            writer.write(result1)
        except Exception as e : 
            writer.write(str(e)+"\n")

        # UHPP pumping and turbining time
        writer.write(f"\n*** Solution 2 ***\ntime of pumping and turbining in UHPP & plot volumes")
        Text(Point(920,140),f"\n*** Solution 2 ***\ntime of pumping and turbining in UHPP & plot volumes").draw(win)

        # plot volume chart
        pump_storage.plot_volume()

        peaks = pump_storage.find_peaks()
        try:
            distance=[30,60,90,120,150,180]
            for i in range(len(peaks)):
                Text(Point(920,160+distance[i]),peaks[i]+"\n").draw(win)
                writer.write(peaks[i]+"\n")
        except Exception as e : 
            writer.write(str(e)+"\n")
            
        # plot inflow/outflow of Pool Beta
        writer.write(f"\n*** Solution 3 ***\ninflow/outflow of Pool Beta")
        pump_storage.plot_slope()

        # pump storage volume in the Lake Alpha is same as pool Beta
        try:
            pump_storage_volume_lake = pump_volume
            result3=f"\n*** Solution 4 ***\npump storage volume in lake is {pump_storage_volume_lake} Mio.m³"
            Text(Point(920,370),result3).draw(win)
            writer.write(result3)
        except Exception as e : 
            writer.write(str(e)+"\n")

        # maximum operational water level Zs of the Lake Alpha
        try:
            max_height = water_level.max_water_alpha_lake()
            result4=f"\n*** Solution 5 ***\nmaximum operational water level in reservoir is {max_height} m.a.s.l"
            Text(Point(920,420),result4).draw(win)
            writer.write(result4)
        except Exception as e : 
            writer.write(str(e)+"\n")

        # elevation which maximum operational water level Zs of the Lake Alpha
        try:
            water_level_outlet = water_level.bottom_outlet()
            result5=f"\n*** Solution 6 ***\nbottom outlet is located at {water_level_outlet} m.a.s.l"
            Text(Point(920,470),result5).draw(win)
            writer.write(result5)
        except Exception as e : 
            writer.write(str(e)+"\n")

        # annual storage volume of the Lake Alpha
        try:
            msg_annual_storage_volume = 'annual storage volume of reservoir is volume of reservoir without ' \
                                        'dead volume and pump storage: '
            min_height = water_level.min_water_alpha_lake()
            volume_annual_alpha = water_level.annual_storage_volume(pump_volume)
            result6=f"\n*** Solution 7 ***\n{msg_annual_storage_volume} {volume_annual_alpha} Mio.m³"
            Text(Point(920,530),result6).draw(win)
            writer.write(result6)
        except Exception as e : 
            writer.write(str(e)+"\n")

        # is the maximum head and what is the minimum head for the UHPP (Omega II)
        try:
            msg_uhpp_electricity_power_plant = 'Maximum Fall Head for UHPP happens when Upper Reservoir in its maximum ' \
                                                'level AND Lake Alpha in its minimum level. This happens at the end of August'
            start_time_max = pump_storage.max_water_level()['start_time']
            end_time_max = pump_storage.max_water_level()['end_time']
            result7=f"\n*** Solution 8 ***\n{msg_uhpp_electricity_power_plant}, {start_time_max} - {end_time_max} o`clock"
            Text(Point(920,580),result7).draw(win)
            writer.write(result7)
        except Exception as e : 
            writer.write(str(e)+"\n")

        try:
            msg_delta_h = 'Delta h:'
            max_level = float(pump_storage.max_water_level()['max_level'])
            result8=f"{msg_delta_h} {max_level - int(min_height)} m"
            Text(Point(920,630),result8).draw(win)
            writer.write(result8)
        except Exception as e : 
            writer.write(str(e)+"\n")

        try:
            msg_max_height_upper_alpha = 'Minimum Fall Head for UHPP happens when Upper Reservoir in its minimum level AND ' \
                                         'Lake Alpha in its maximum level. This happens at the end of April,'
            end_time_min = pump_storage.min_water_level()[-1]
            result9=f"{msg_max_height_upper_alpha} {end_time_min} o´clock"
            Text(Point(920,660),result9).draw(win)
            writer.write(result9)
        except Exception as e : 
            writer.write(str(e)+"\n")

        try:
            min_level = float(pump_storage.min_water_level()[0])
            result10=f"{msg_delta_h} {min_level - int(max_height)} m"
            Text(Point(920,690),result10).draw(win)
            writer.write(result10)
        except Exception as e : 
            writer.write(str(e)+"\n")

        # How high is the turbine discharge in the LHPP (Omega I) between end of April and end of August

        try:
            inflow_volume_alpha_lack_may_till_aug = round(
                (month_volume.volume_in_month('May') +
                month_volume.volume_in_month('Jun') +
                month_volume.volume_in_month('Jul') +
                month_volume.volume_in_month('Aug')
                ) / 1000000, 1
            )
            outflow_volume_alpha_lack_may_till_aug = inflow_volume_alpha_lack_may_till_aug + volume_annual_alpha
            q_out_alpha_may_aug = round((outflow_volume_alpha_lack_may_till_aug / (4 * 30 * 24 * 3600) * 1000000), 1)
            q_lhpp_electricity_power_plant = round(q_out_alpha_may_aug - (CONSTANT['flow_in_tropical_creek'] / 1000), 1)
            msg_lhpp_electricity_power_plant = 'Between the start of May and the end of August, Lake Alpha Volume goes from ' \
                                            'Maximum Operational Volume to Minimum Operational Volume,And since there ' \
                                            'are 2 outflow (to LHPP and to Alphabeta Creek), we can say turbine discharge ' \
                                            'in the LHPP has'

            result11=f"\n*** Solution 9 ***\n{msg_lhpp_electricity_power_plant} {q_lhpp_electricity_power_plant} m³/s"
            Text(Point(920,720),result11).draw(win)
            writer.write(result11)
            month_volume.plot_All()
        except Exception as e : 
            writer.write(str(e)+"\n")


        try:
            win.getMouse()
        except:
            pass