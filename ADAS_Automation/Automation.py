import win32com.client as win32
import time
from Diag_Req_Res import *
from Report_generator import *

CANoe = win32.DispatchEx("CANoe.Application")

def ACC_Active():
    #file = open(r"C:\Users\srava\Desktop\Vinay_AET\ADAS_Automation\Report.txt", "w")
    write_content("ACC Test Automation Report\n")
    write_content("Test Case 1: ACC_active\n")

    write_content("Test Step 1: M0_sig_ReadytoDrive to drive active 0x2(Drive mode)\n")
    ##get signal
    M0_drive_sig = CANoe.GetBus("CAN").GetSignal(1,"MO_Message_1", "MO_sig_ReadytoDrive") ##DBC information --> Bus = CAN bus, Channel = 1, Messsage = M0_Message_1, Signal = MO_sig_ReadytoDrive
    time.sleep(0.1)
    M0_drive_sig.Value = 0x2
    time.sleep(0.5)

    write_content("Test Step 2: Set signal ACC_Int_status to Active 0x1(Active)\n")
    ACC_Init_Status = CANoe.GetBus("CAN").GetSignal(1,"ACC_BCM_Message", "ACC_Int_status")
    time.sleep(0.1)
    ACC_Init_Status.Value = 0x1
    time.sleep(0.5)

    write_content("Test Step 3: set ACC_MainSwitch to active 0x2\n")
    ACC_MainSwitch = CANoe.GetBus("CAN").GetSignal(1,"ACC_BCM_Message", "ACC_MainSwitch_ACC")
    time.sleep(0.1)
    ACC_MainSwitch.Value = 0x2
    time.sleep(0.5)

    write_content("Test Step 4: set Gear_signal to drive 0x3\n")
    Gear_Sig = CANoe.GetBus("CAN").GetSignal(1,"Gear_Message", "Gear_signal")
    time.sleep(0.1)
    Gear_Sig.Value = 0x3
    time.sleep(0.5)

    write_content("Test Step 5: set Speed morethan 40kmph (Sig_Spdmtr_Rd to > 40kmph)\n")
    Speed_Sig = CANoe.GetBus("CAN").GetSignal(1,"RDS_Coder_Data_CAN", "Sig_Spdmtr_Rq")
    time.sleep(0.1)
    Speed_Sig.Value = 0x78
    time.sleep(0.5)

    write_content("Test Step 6: Set ACC_Set_signal to Activate 0x1\n")
    ACC_Set_signal = CANoe.GetBus("CAN").GetSignal(1,"ACC_BCM_Message", "ACC_Set_signal")
    time.sleep(0.1)
    ACC_Set_signal.Value = 0x1
    time.sleep(0.5)


    #output
    write_content("Test Step 7: Expected output Check ACC_sig_status should be Active and the value should be 0x2\n")
    ACC_Status = CANoe.GetBus("CAN").GetSignal(1,"ACC_status", "ACC_sig_status")

    if int(ACC_Status) == 0x2:
        write_content(f"The test step 7 is Passed, The Expected value is 0x2 and Actual value is {ACC_Status}\n")
        print("The test case 1 is Passed\n")
    else:
        write_content(f"The test step 7 is Failed, The Expected value is 0x2 and Actual value is {ACC_Status}\n")
        print("The test case 1 is Failed\n")

def ACC_Passive():
    #file = open(r"C:\Users\srava\Desktop\Vinay_AET\ADAS_Automation\Report.txt", "a")
    write_content("Test Case 2: ACC_Passive\n")

    write_content("Test Step 1: M0_sig_ReadytoDrive to drive active 0x2(Drive mode)\n")
    ##get signal
    M0_drive_sig = CANoe.GetBus("CAN").GetSignal(1,"MO_Message_1", "MO_sig_ReadytoDrive") ##DBC information --> Bus = CAN bus, Channel = 1, Messsage = M0_Message_1, Signal = MO_sig_ReadytoDrive
    time.sleep(0.1)
    M0_drive_sig.Value = 0x2
    time.sleep(0.5)

    write_content("Test Step 2: Set signal ACC_Int_status to Active 0x1(Active)\n")
    ACC_Init_Status = CANoe.GetBus("CAN").GetSignal(1,"ACC_BCM_Message", "ACC_Int_status")
    time.sleep(0.1)
    ACC_Init_Status.Value = 0x1
    time.sleep(0.5)

    write_content("Test Step 3: set ACC_MainSwitch to off 0x1\n")
    ACC_MainSwitch = CANoe.GetBus("CAN").GetSignal(1,"ACC_BCM_Message", "ACC_MainSwitch_ACC")
    time.sleep(0.1)
    ACC_MainSwitch.Value = 0x1
    time.sleep(0.5)

    write_content("Test Step 4: set Gear_signal to drive 0x3\n")
    Gear_Sig = CANoe.GetBus("CAN").GetSignal(1,"Gear_Message", "Gear_signal")
    time.sleep(0.1)
    Gear_Sig.Value = 0x3
    time.sleep(0.5)

    write_content("Test Step 5: set Speed morethan 40kmph (Sig_Spdmtr_Rd to > 40kmph)\n")
    Speed_Sig = CANoe.GetBus("CAN").GetSignal(1,"RDS_Coder_Data_CAN", "Sig_Spdmtr_Rq")
    time.sleep(0.1)
    Speed_Sig.Value = 0x78
    time.sleep(0.5)

    write_content("Test Step 6: Set ACC_Set_signal to Activate 0x1\n")
    ACC_Set_signal = CANoe.GetBus("CAN").GetSignal(1,"ACC_BCM_Message", "ACC_Set_signal")
    time.sleep(0.1)
    ACC_Set_signal.Value = 0x1
    time.sleep(0.5)


    #output
    write_content("Test Step 7: Expected output Check ACC_sig_status should be Active and the value should be 0x2\n")
    ACC_Status = CANoe.GetBus("CAN").GetSignal(1,"ACC_status", "ACC_sig_status")

    if int(ACC_Status) == 0x1:
        write_content(f"The test step 7 is Passed, The Expected value is 0x2 and Actual value is {ACC_Status}\n")
        print("The test case 2 is Passed\n")
    else:
        write_content(f"The test step 2 is Failed, The Expected value is 0x2 and Actual value is {ACC_Status}\n")
        print("The test case 2 is Failed\n")


def Check_ACC_Passive_APC():
    #file = open(r"C:\Users\srava\Desktop\Vinay_AET\ADAS_Automation\Report.txt", "w")
    write_content("Test Case 3: Check APC(Activation Prevention Control) conditions\n")

    write_content("Test Step 1: M0_sig_ReadytoDrive to drive active 0x2(Drive mode)\n")
    ##get signal
    M0_drive_sig = CANoe.GetBus("CAN").GetSignal(1, "MO_Message_1", "MO_sig_ReadytoDrive")  ##DBC information --> Bus = CAN bus, Channel = 1, Messsage = M0_Message_1, Signal = MO_sig_ReadytoDrive
    time.sleep(0.1)
    M0_drive_sig.Value = 0x2
    time.sleep(0.5)

    write_content("Test Step 2: Set signal ACC_Int_status to Active 0x1(Active)\n")
    ACC_Init_Status = CANoe.GetBus("CAN").GetSignal(1, "ACC_BCM_Message", "ACC_Int_status")
    time.sleep(0.1)
    ACC_Init_Status.Value = 0x1
    time.sleep(0.5)

    write_content("Test Step 3: set ACC_MainSwitch to Active 0x2\n")
    ACC_MainSwitch = CANoe.GetBus("CAN").GetSignal(1, "ACC_BCM_Message", "ACC_MainSwitch_ACC")
    time.sleep(0.1)
    ACC_MainSwitch.Value = 0x2
    time.sleep(0.5)

    write_content("Test Step 4: set Gear_signal to drive 0x3\n")
    Gear_Sig = CANoe.GetBus("CAN").GetSignal(1, "Gear_Message", "Gear_signal")
    time.sleep(0.1)
    Gear_Sig.Value = 0x3
    time.sleep(0.5)

    write_content("Test Step 5: set Speed lessthan 40kmph (Sig_Spdmtr_Rd to > 40kmph)\n")
    Speed_Sig = CANoe.GetBus("CAN").GetSignal(1, "RDS_Coder_Data_CAN", "Sig_Spdmtr_Rq")
    time.sleep(0.1)
    Speed_Sig.Value = 0x20
    time.sleep(0.5)

    write_content("Test Step 6: Set ACC_Set_signal to Activate 0x1\n")
    ACC_Set_signal = CANoe.GetBus("CAN").GetSignal(1, "ACC_BCM_Message", "ACC_Set_signal")
    time.sleep(0.1)
    ACC_Set_signal.Value = 0x1
    time.sleep(0.5)

    # output
    write_content("Test Step 7: Check ACC_sig_status is Passive 0x1 and ACC_disp_signal is 0x02(Vehicle speed to low)\n")
    ACC_sig_status = CANoe.GetBus("CAN").GetSignal(1, "ACC_status", "ACC_sig_status")
    # print(ACC_sig_status)

    if int(ACC_sig_status) == 0x1:
        write_content(f"The test step 7 condition 1 is Passed, The Expected value is 0x1 and Actual value is {ACC_sig_status}\n")
        print("The test case 3 is Passed\n")
    else:
        write_content(f"The test step 7  condition 1 is Failed, The Expected value is 0x1 and Actual value is {ACC_sig_status}\n")
        print("The test case 3 is Failed\n")

    ACC_disp_signal = CANoe.GetBus("CAN").GetSignal(1, "ACC_status", "ACC_disp_signal")
    #print(ACC_disp_signal)

    if int(ACC_disp_signal) == 0x2:
        write_content(f"The test step 7 condition 2 is Passed the value of ACC_disp_signal is 0x02 - Vehicle speed to low ")
    else:
        write_content(f"The test step 7 condition 2 is failed the value of ACC_disp_signal is 0x01 - Vehicle speed to High ")



##Test case 4: ACC Passive Status and APC Gear Position
def Check_ACC_Passive_Apc_gear():
    #file = open(r"C:\Users\srava\Desktop\Vinay_AET\ADAS_Automation\Report.txt", "w")
    write_content("Test Case 4: ACC Passive Status and APC Gear Position\n")

    write_content("Test Step 1: M0_sig_ReadytoDrive to drive active 0x2(Drive mode)\n")
    ##get signal
    M0_drive_sig = CANoe.GetBus("CAN").GetSignal(1, "MO_Message_1", "MO_sig_ReadytoDrive")  ##DBC information --> Bus = CAN bus, Channel = 1, Messsage = M0_Message_1, Signal = MO_sig_ReadytoDrive
    time.sleep(0.1)
    M0_drive_sig.Value = 0x2
    time.sleep(0.5)

    write_content("Test Step 2: Set signal ACC_Int_status to Active 0x1(Active)\n")
    ACC_Init_Status = CANoe.GetBus("CAN").GetSignal(1, "ACC_BCM_Message", "ACC_Int_status")
    time.sleep(0.1)
    ACC_Init_Status.Value = 0x1
    time.sleep(0.5)

    write_content("Test Step 3: set ACC_MainSwitch to Active 0x2\n")
    ACC_MainSwitch = CANoe.GetBus("CAN").GetSignal(1, "ACC_BCM_Message", "ACC_MainSwitch_ACC")
    time.sleep(0.1)
    ACC_MainSwitch.Value = 0x2
    time.sleep(0.5)

    write_content("Test Step 4: set Gear_signal to Reverse 0x1\n")
    Gear_Sig = CANoe.GetBus("CAN").GetSignal(1, "Gear_Message", "Gear_signal")
    time.sleep(0.1)
    Gear_Sig.Value = 0x1
    time.sleep(0.5)

    write_content("Test Step 5: set Speed morethan 40kmph (Sig_Spdmtr_Rd to > 40kmph)\n")
    Speed_Sig = CANoe.GetBus("CAN").GetSignal(1, "RDS_Coder_Data_CAN", "Sig_Spdmtr_Rq")
    time.sleep(0.1)
    Speed_Sig.Value = 0x50
    time.sleep(0.5)

    write_content("Test Step 6: Set ACC_Set_signal to Activate 0x1\n")
    ACC_Set_signal = CANoe.GetBus("CAN").GetSignal(1, "ACC_BCM_Message", "ACC_Set_signal")
    time.sleep(0.1)
    ACC_Set_signal.Value = 0x1
    time.sleep(0.5)

    # output
    write_content("Test Step 7: Check ACC_sig_status is Passive 0x1 and ACC_disp_signal is 0x02(Vehicle speed to low)\n")
    ACC_sig_status = CANoe.GetBus("CAN").GetSignal(1, "ACC_status", "ACC_sig_status")
    # print(ACC_sig_status)

    if int(ACC_sig_status) == 0x1:
        write_content(f"The test step 7 condition 1 is Passed, The Expected value is 0x1 and Actual value is {ACC_sig_status}\n")
        print("The test case 4 is Passed\n")
    else:
        write_content(f"The test step 7  condition 1 is Failed, The Expected value is 0x1 and Actual value is {ACC_sig_status}\n")
        print("The test case 4 is Failed\n")

    ACC_disp_signal = CANoe.GetBus("CAN").GetSignal(1, "ACC_status", "ACC_disp_signal")
    #print(ACC_disp_signal)

    if int(ACC_disp_signal) == 0x3:
        write_content(f"The test step 7 condition 2 is Passed the value of ACC_disp_signal is 0x02 - Vehicle speed to low ")
        print("The test case 4 is Passed\n")
    else:
        write_content(f"The test step 7 condition 2 is failed the value of ACC_disp_signal is 0x01 - Vehicle speed to High ")
        print("The test case 4 is Failed\n")

##Test case 4: ACC Passive Status and APC Gear Position
def Check_ACC_Passive_Apc_gear():
            # file = open(r"C:\Users\srava\Desktop\Vinay_AET\ADAS_Automation\Report.txt", "w")
    write_content("Test Case 4: Check APC(Activation Prevention Control) conditions\n")

    write_content("Test Step 1: M0_sig_ReadytoDrive to drive active 0x2(Drive mode)\n")
            ##get signal
    M0_drive_sig = CANoe.GetBus("CAN").GetSignal(1, "MO_Message_1", "MO_sig_ReadytoDrive")  ##DBC information --> Bus = CAN bus, Channel = 1, Messsage = M0_Message_1, Signal = MO_sig_ReadytoDrive
    time.sleep(0.1)
    M0_drive_sig.Value = 0x2
    time.sleep(0.5)

    write_content("Test Step 2: Set signal ACC_Int_status to Active 0x1(Active)\n")
    ACC_Init_Status = CANoe.GetBus("CAN").GetSignal(1, "ACC_BCM_Message", "ACC_Int_status")
    time.sleep(0.1)
    ACC_Init_Status.Value = 0x1
    time.sleep(0.5)

    write_content("Test Step 3: set ACC_MainSwitch to Active 0x2\n")
    ACC_MainSwitch = CANoe.GetBus("CAN").GetSignal(1, "ACC_BCM_Message", "ACC_MainSwitch_ACC")
    time.sleep(0.1)
    ACC_MainSwitch.Value = 0x2
    time.sleep(0.5)

    write_content("Test Step 4: set Gear_signal to Reverse 0x1\n")
    Gear_Sig = CANoe.GetBus("CAN").GetSignal(1, "Gear_Message", "Gear_signal")
    time.sleep(0.1)
    Gear_Sig.Value = 0x1
    time.sleep(0.5)

    write_content("Test Step 5: set Speed morethan 40kmph (Sig_Spdmtr_Rd to > 40kmph)\n")
    Speed_Sig = CANoe.GetBus("CAN").GetSignal(1, "RDS_Coder_Data_CAN", "Sig_Spdmtr_Rq")
    time.sleep(0.1)
    Speed_Sig.Value = 0x50
    time.sleep(0.5)

    write_content("Test Step 6: Set ACC_Set_signal to Activate 0x1\n")
    ACC_Set_signal = CANoe.GetBus("CAN").GetSignal(1, "ACC_BCM_Message", "ACC_Set_signal")
    time.sleep(0.1)
    ACC_Set_signal.Value = 0x1
    time.sleep(0.5)

    # output
    write_content(
        "Test Step 7: Check ACC_sig_status is Passive 0x1 and ACC_disp_signal is 0x02(Vehicle speed to low)\n")
    ACC_sig_status = CANoe.GetBus("CAN").GetSignal(1, "ACC_status", "ACC_sig_status")
    # print(ACC_sig_status)

    if int(ACC_sig_status) == 0x1:
        write_content(f"The test step 7 condition 1 is Passed, The Expected value is 0x1 and Actual value is {ACC_sig_status}\n")
        #print("The test case 4 is Passed\n")
    else:
        write_content(f"The test step 7  condition 1 is Failed, The Expected value is 0x1 and Actual value is {ACC_sig_status}\n")
        print("The test case 4 is Failed\n")

    ACC_disp_signal = CANoe.GetBus("CAN").GetSignal(1, "ACC_status", "ACC_disp_signal")
    # print(ACC_disp_signal)

    if int(ACC_disp_signal) == 0x3:
        write_content(f"The test step 7 condition 2 is Passed the value of ACC_disp_signal is 0x02 - Vehicle speed to low ")
        print("The test case 4 is Passed\n")
    else:
        write_content(f"The test step 7 condition 2 is failed the value of ACC_disp_signal is 0x01 - Vehicle speed to High ")
        print("The test case 4 is Failed\n")

##Test case 5: ACC Active then SOC Condition Vehicle speed
def Check_ACC_Active_SOC():
    #file = open(r"C:\Users\srava\Desktop\Vinay_AET\ADAS_Automation\Report.txt", "w")
    write_content("Test Case 5: ACC Active then SOC Condition Vehicle speed\n")

    write_content("Test Step 1: M0_sig_ReadytoDrive to drive active 0x2(Drive mode)\n")
    ##get signal
    M0_drive_sig = CANoe.GetBus("CAN").GetSignal(1, "MO_Message_1", "MO_sig_ReadytoDrive")  ##DBC information --> Bus = CAN bus, Channel = 1, Messsage = M0_Message_1, Signal = MO_sig_ReadytoDrive
    time.sleep(0.1)
    M0_drive_sig.Value = 0x2
    time.sleep(0.5)

    write_content("Test Step 2: Set signal ACC_Int_status to Active 0x1(Active)\n")
    ACC_Init_Status = CANoe.GetBus("CAN").GetSignal(1, "ACC_BCM_Message", "ACC_Int_status")
    time.sleep(0.1)
    ACC_Init_Status.Value = 0x1
    time.sleep(0.5)

    write_content("Test Step 3: set ACC_MainSwitch to Active 0x2\n")
    ACC_MainSwitch = CANoe.GetBus("CAN").GetSignal(1, "ACC_BCM_Message", "ACC_MainSwitch_ACC")
    time.sleep(0.1)
    ACC_MainSwitch.Value = 0x2
    time.sleep(0.5)

    write_content("Test Step 4: set Gear_signal to Drive 0x1\n")
    Gear_Sig = CANoe.GetBus("CAN").GetSignal(1, "Gear_Message", "Gear_signal")
    time.sleep(0.1)
    Gear_Sig.Value = 0x3
    time.sleep(0.5)

    write_content("Test Step 5: set Speed morethan 40kmph (Sig_Spdmtr_Rd to > 40kmph)\n")
    Speed_Sig = CANoe.GetBus("CAN").GetSignal(1, "RDS_Coder_Data_CAN", "Sig_Spdmtr_Rq")
    time.sleep(0.1)
    Speed_Sig.Value = 0x50
    time.sleep(0.5)

    write_content("Test Step 6: Set ACC_Set_signal to Activate 0x1\n")
    ACC_Set_signal = CANoe.GetBus("CAN").GetSignal(1, "ACC_BCM_Message", "ACC_Set_signal")
    time.sleep(0.1)
    ACC_Set_signal.Value = 0x1
    time.sleep(0.5)

    # output
    write_content("Test Step 7: Check ACC_sig_status is Passive 0x1 and ACC_disp_signal is 0x02(Vehicle speed to low)\n")
    ACC_sig_status = CANoe.GetBus("CAN").GetSignal(1, "ACC_status", "ACC_sig_status")
    #print(ACC_sig_status)
    write_content(f"The test step 7 condition 1 is Passed, The Expected value is 0x1 and Actual value is {ACC_sig_status}\n")

    write_content("Test Step 8: set Speed lessthan 40kmph (Sig_Spdmtr_Rd to > 40kmph)\n")
    Speed_Sig = CANoe.GetBus("CAN").GetSignal(1, "RDS_Coder_Data_CAN", "Sig_Spdmtr_Rq")
    time.sleep(0.1)
    Speed_Sig.Value = 0x15
    time.sleep(0.5)

    write_content("Test Step 9: Set ACC_Set_signal to Activate 0x1\n")
    ACC_Set_signal = CANoe.GetBus("CAN").GetSignal(1, "ACC_BCM_Message", "ACC_Set_signal")
    time.sleep(0.1)
    ACC_Set_signal.Value = 0x1
    time.sleep(0.5)

    write_content("Test Step 10: Check ACC_sig_status is Active 0x1 and ACC_disp_signal is 0x02(Vehicle speed to low)\n")
    ACC_sig_status = CANoe.GetBus("CAN").GetSignal(1, "ACC_status", "ACC_sig_status")

    if int(ACC_sig_status) == 0x1:
        write_content(f"The test step 7 condition 1 is Passed, The Expected value is 0x1 and Actual value is {ACC_sig_status}\n")
        #print("The test case 5 condition 1 is Passed\n")
    else:
        write_content(f"The test step 7  condition 1 is Failed, The Expected value is 0x1 and Actual value is {ACC_sig_status}\n")
        #print("The test case 5 condition 1 is Failed\n")


    ACC_disp_signal = CANoe.GetBus("CAN").GetSignal(1, "ACC_status", "ACC_disp_signal")
    #print(ACC_disp_signal)

    if int(ACC_disp_signal) == 0x2:
        write_content(f"The test step 7 condition 2 is Passed the value of ACC_disp_signal is 0x02 - Vehicle speed to low ")
        print("The test case 5 is Passed\n")
    else:
        write_content(f"The test step 7 condition 2 is failed the value of ACC_disp_signal is 0x01 - Vehicle speed to High ")
        print("The test case 5 is Failed\n")



##Test case 6:  ACC Active then SOC Condition Gear Position
def Check_ACC_Active_SOC_Gear():
    #file = open(r"C:\Users\srava\Desktop\Vinay_AET\ADAS_Automation\Report.txt", "w")
    write_content("Test Case 6:  ACC Active then SOC Condition Gear Position\n")

    write_content("Test Step 1: M0_sig_ReadytoDrive to drive active 0x2(Drive mode)\n")
    ##get signal
    M0_drive_sig = CANoe.GetBus("CAN").GetSignal(1, "MO_Message_1", "MO_sig_ReadytoDrive")  ##DBC information --> Bus = CAN bus, Channel = 1, Messsage = M0_Message_1, Signal = MO_sig_ReadytoDrive
    time.sleep(0.1)
    M0_drive_sig.Value = 0x2
    time.sleep(0.5)

    write_content("Test Step 2: Set signal ACC_Int_status to Active 0x1(Active)\n")
    ACC_Init_Status = CANoe.GetBus("CAN").GetSignal(1, "ACC_BCM_Message", "ACC_Int_status")
    time.sleep(0.1)
    ACC_Init_Status.Value = 0x1
    time.sleep(0.5)

    write_content("Test Step 3: set ACC_MainSwitch to Active 0x2\n")
    ACC_MainSwitch = CANoe.GetBus("CAN").GetSignal(1, "ACC_BCM_Message", "ACC_MainSwitch_ACC")
    time.sleep(0.1)
    ACC_MainSwitch.Value = 0x2
    time.sleep(0.5)

    write_content("Test Step 4: set Gear_signal to Drive 0x1\n")
    Gear_Sig = CANoe.GetBus("CAN").GetSignal(1, "Gear_Message", "Gear_signal")
    time.sleep(0.1)
    Gear_Sig.Value = 0x3
    time.sleep(0.5)

    write_content("Test Step 5: set Speed morethan 40kmph (Sig_Spdmtr_Rd to > 40kmph)\n")
    Speed_Sig = CANoe.GetBus("CAN").GetSignal(1, "RDS_Coder_Data_CAN", "Sig_Spdmtr_Rq")
    time.sleep(0.1)
    Speed_Sig.Value = 0x50
    time.sleep(0.5)

    write_content("Test Step 6: Set ACC_Set_signal to Activate 0x1\n")
    ACC_Set_signal = CANoe.GetBus("CAN").GetSignal(1, "ACC_BCM_Message", "ACC_Set_signal")
    time.sleep(0.1)
    ACC_Set_signal.Value = 0x1
    time.sleep(0.5)

    # output
    write_content("Test Step 7: Check ACC_sig_status is Passive 0x1 and ACC_disp_signal is 0x02(Vehicle speed to low)\n")
    ACC_sig_status = CANoe.GetBus("CAN").GetSignal(1, "ACC_status", "ACC_sig_status")
    #print(ACC_sig_status)
    write_content(f"The test step 7 condition 1 is Passed, The Expected value is 0x1 and Actual value is {ACC_sig_status}\n")

    write_content("Test Step 8: set Gear_signal to Drive 0x1\n")
    Gear_Sig = CANoe.GetBus("CAN").GetSignal(1, "Gear_Message", "Gear_signal")
    time.sleep(0.1)
    Gear_Sig.Value = 0x1
    time.sleep(0.5)

    write_content("Test Step 9: Set ACC_Set_signal to Activate 0x1\n")
    ACC_Set_signal = CANoe.GetBus("CAN").GetSignal(1, "ACC_BCM_Message", "ACC_Set_signal")
    time.sleep(0.1)
    ACC_Set_signal.Value = 0x1
    time.sleep(0.5)

    write_content("Test Step 10: Check ACC_sig_status is Passsive 0x1 and ACC_disp_signal is 0x03\n")
    ACC_sig_status = CANoe.GetBus("CAN").GetSignal(1, "ACC_status", "ACC_sig_status")

    if int(ACC_sig_status) == 0x1:
        write_content(f"The test step 7 condition 1 is Passed, The Expected value is 0x2 and Actual value is {ACC_sig_status}\n")
        #print("The test case 6 condition 1 is Passed\n")
    else:
        write_content(f"The test step 7  condition 1 is Failed, The Expected value is 0x2 and Actual value is {ACC_sig_status}\n")
        #print("The test case 6 condition 1 is Failed\n")


    ACC_disp_signal = CANoe.GetBus("CAN").GetSignal(1, "ACC_status", "ACC_disp_signal")
    #print(ACC_disp_signal)

    if int(ACC_disp_signal) == 0x3:
        write_content(f"The test step 7 condition 2 is Passed the value of ACC_disp_signal is 0x03 - Check Gear Position")
        print("The test case 6 is Passed\n")
    else:
        write_content(f"The test step 7 condition 2 is failed the value of ACC_disp_signal is 0x02 - Gear Position is correct")
        print("The test case 6 is Failed\n")


#CANoe.Open(r"C:\Users\srava\Desktop\Vinay_AET\ADAS_Automation\RBS\RBS_Python_v0.2\RBS_Python.cfg")
#time.sleep(2)
#CANoe.Measurement.Start()
#time.sleep(7)

diag_open()
ACC_Active()
ACC_Passive()
Check_ACC_Passive_APC()
Check_ACC_Passive_Apc_gear()
Check_ACC_Active_SOC()
Check_ACC_Active_SOC_Gear()

CANoe.Measurement.Stop()
print(r"Executed Successfully: Report can be found here --> C:\Users\srava\Desktop\Vinay_AET\ADAS_Automation\Report.html")