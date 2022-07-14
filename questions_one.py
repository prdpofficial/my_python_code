last_meter_readings = int(input('Please Enter Last Meter Readings...'))
Current_meter_readings = int(input('Please Enter Current Meter Readings...'))

calculated_units = Current_meter_readings - last_meter_readings
surcharge = 100
bpl_qouta_unit = 100
if(calculated_units>100):
    calculated_units-= 100
    print("Your Bill is Rupess")
    print((calculated_units*12) + (bpl_qouta_unit*7)+ surcharge)
        
else:
    print("Your Consumption is below 100 units so "+"Your Bill is Rupess")
    print(calculated_units*7 + 100)
