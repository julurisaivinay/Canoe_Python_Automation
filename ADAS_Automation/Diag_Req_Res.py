from py_canoe import CANoe
import time


def diag_open():
    diag = CANoe()
    #Opening the Diag Panel
    diag.open(r"C:\Users\srava\Desktop\Vinay_AET\ADAS_Automation\RBS\RBS_Python_v0.2\RBS_Python.cfg")
    #Start the Diagnostic
    diag.start_measurement()
    time.sleep(3)

    #Running the Services
    def_session = diag.send_diag_request(diag_ecu_qualifier_name= "Door", request= "10 01") # Service for Default Session
    time.sleep(1)
    Ext_session = diag.send_diag_request(diag_ecu_qualifier_name= "Door", request= "10 03") # Service for Extended Session
    time.sleep(2)
    ACC_Var_Code = diag.send_diag_request(diag_ecu_qualifier_name= "Door", request= "2E DE 02 01 02") # Service for Activate the Variant coding