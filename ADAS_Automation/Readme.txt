Acc Status
Active - Acc is fully active
Passive - Acc is Partially active, still more conditions has not matched


Apc --> Activation prevention conditions
it comes into picture before we activate the ACC

Not Pluged the seat bet --> Doors Opened

Vehicle speed is not > 40kmph

P R N D -->  Vehicle is not in drive mode
SOC --> Switch off Conditions


ACC is Activated
Removing seat belt
Door Opened

Vehicle speed is not > 40 kmph



Variant coding or EOL Proxy:


Test case 1: ACC Active status

M0_sig_ReadytoDrive to drive active 0x2
ACC_Int_status to Active 0x1
ACC_MainSwitch_ACC to active 0x2
Gear_signal to drive 0x3
Sig_Spdmtr_Rd to > 40kmph
ACC_Set_signal to Activated --> 0x1
Check ACC_sig_status is Active 0x2 --> Passed
Acc_sig_status is not active !0x2 -->  Failed

Test case 2: ACC Passive status

M0_sig_ReadytoDrive to drive active 0x2
ACC_Int_status to Active 0x1
ACC_MainSwitch_ACC to off 0x1
Gear_signal to drive 0x3
Sig_Spdmtr_Rd to > 40kmph
ACC_Set_signal to Activated --> 0x1
Check ACC_sig_status is Passive 0x1 --> Passed
Acc_sig_status is not active !0x1 -->   Failed



Test Case 3: Check APC(Activation Prevention Control) conditions

M0_sig_ReadytoDrive to drive active 0x2
ACC_Int_status to Active 0x1
ACC_MainSwitch_ACC to active 0x2
Gear_signal to drive 0x3
Sig_Spdmtr_Rd to <40kmph
ACC_Set_signal to Activated --> 0x1
Check ACC_sig_status is Passive 0x1  and ACC_disp_signal is 0x02 = Vehicle speed too low --> Passed
Acc_sig_status is not active !0x1 and ACC_disp_signal is !0x02 = Not Vehicle speed too low --> Failed

Test Case 4: Check APC(Activation Prevention Control) keeping Reverse gare position

M0_sig_ReadytoDrive to drive active 0x2
ACC_Int_status to Active 0x1
ACC_MainSwitch_ACC to active 0x2
Gear_signal to Reverse 0x1
Sig_Spdmtr_Rd to <40kmph
ACC_Set_signal to Activated --> 0x1
Check ACC_sig_status is Passive 0x1  and ACC_disp_signal is 0x03 = Check Gear Position --> Passed
Acc_sig_status is not active !0x1 and ACC_disp_signal is !0x03 = not Check Gear Position  --> Failed