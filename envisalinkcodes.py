## Alarm Server
## Supporting Envisalink 2DS/3
## Written by donnyk+envisalink@gmail.com
##
## This code is under the terms of the GPL v3 license.
evl_ResponseTypes = {
    500 : {'name' : 'Command Acknowledge', 'description' : 'A command has been received successfully.' , 'loglevel' : 1},
    501 : {'name' : 'Command Error', 'description' : 'A command has been received with a bad checksum.' , 'loglevel' : 1},
    502 : {'name' : 'System Error {0}', 'description' : 'An error has been detected.' , 'loglevel' : 1, 'parameters' : 1},
    505 : {'name' : 'Login Interaction', 'description' : 'Sent During Session Login Only.' , 'loglevel' : 1, 'handler' : 'login'},
    510 : {'name' : 'Keypad Led State - Partition 1', 'description' : 'Outputted when the TPI has deceted a change of state in the Partition 1 keypad LEDs.' , 'loglevel' : 1},
    511 : {'name' : 'Keypad Led Flash State - Partition 1', 'description' : 'Outputed when the TPI has detected a change of state in the Partition 1 keypad LEDs as to whether to flash or not. Overrides 510. That is, if 511 says the PROGRAM LED is flashing, then it doesn''t matter what 510 says.' , 'loglevel' : 1},
    550 : {'name' : 'Time/Date Broadcast', 'description' : 'Outputs the current security system time.' , 'loglevel' : 1},
    560 : {'name' : 'Ring Detected', 'description' : 'The Panel has detected a ring on the telephone line. Note: This command will only be issued if an ESCORT 5580xx module is present.' , 'loglevel' : 1},
    561 : {'name' : 'Indoor Temperature Broadcast', 'description' : 'If an ESCORT 5580TC is installed, and at least one ENERSTAT thermostat, this command displays the interior temperature and the thermostat number.' , 'loglevel' : 1},
    562 : {'name' : 'Outdoor Temperature Broadcast', 'description' : 'If an ESCORT 5580TC is installed, and at least one ENERSTAT thermostat, this command displays the exterior temperature and the thermostat number.' , 'loglevel' : 1},
    601 : {'name' : 'Partition {0[0]} Zone {0[1]}{0[2]}{0[3]} Alarm', 'description' : 'A zone has gone into alarm.' , 'loglevel' : 1, 'handler' : 'zone_problem', 'parameters' : 1, 'status' : 'alarm', 'status_val' : True},
    602 : {'name' : 'Partition {0[0]} Zone {0[1]}{0[2]}{0[3]} Alarm Restore', 'description' : 'A zone alarm has been restored.' , 'loglevel' : 1, 'handler' : 'zone_problem', 'parameters' : 1, 'status' : 'alarm', 'status_val' : False},
    603 : {'name' : 'Partition {0[0]} Zone {0[1]}{0[2]}{0[3]} Tamper', 'description' : 'A zone has a tamper condition.' , 'loglevel' : 1, 'handler' : 'zone_problem', 'parameters' : 1, 'status' : 'tamper', 'status_val' : True},
    604 : {'name' : 'Partition {0[0]} Zone {0[1]}{0[2]}{0[3]} Tamper Restore', 'description' : 'A zone tamper condition has been restored.' , 'loglevel' : 1, 'handler' : 'zone_problem', 'parameters' : 1, 'status' : 'tamper', 'status_val' : False},
    605 : {'name' : 'Zone {0} Fault', 'description' : 'A zone has a fault condition.' , 'loglevel' : 1, 'parameters' : 1, 'handler' : 'zone', 'status' : 'fault', 'status_val' : True},
    606 : {'name' : 'Zone {0} Fault Restore', 'description' : 'A zone fault condition has been restored.' , 'loglevel' : 1, 'handler' : 'zone', 'parameters' : 1, 'status' : 'fault', 'status_val' : False},
    609 : {'name' : 'Zone {0} Open', 'description' : 'General status of the zone.' , 'loglevel' : 1, 'handler' : 'zone', 'parameters' : 1, 'status' : 'open', 'status_val' : True},
    610 : {'name' : 'Zone {0} Restored', 'description' : 'General status of the zone.' , 'loglevel' : 1, 'handler' : 'zone', 'parameters' : 1, 'status' : 'open', 'status_val' : False},
    615 : {'name' : 'Envisalink Zone Timer Dump', 'description' : 'This command contains the raw zone timers used inside the Envisalink. The dump is a 256 character packed HEX string representing 64 UINT16 (little endian) zone timers. Zone timers count down from 0xFFFF (zone is open) to 0x0000 (zone is closed too long ago to remember). Each ''tick'' of the zone time is actually 5 seconds so a zone timer of 0xFFFE means ''5 seconds ago''. Remember, the zone timers are LITTLE ENDIAN so the above example would be transmitted as FEFF.' , 'loglevel' : 1},
    620 : {'name' : 'Duress Alarm', 'description' : 'A duress code has been entered on a system keypad.' , 'loglevel' : 1},
    621 : {'name' : '[F] Key Alarm', 'description' : 'A Fire key alarm has been detected.' , 'loglevel' : 1},
    622 : {'name' : '[F] Key Alarm', 'description' : 'A Fire key alarm has been restored (sent automatically).' , 'loglevel' : 1},
    623 : {'name' : '[A] Key Alarm', 'description' : 'A Auxillary key alarm has been detected.' , 'loglevel' : 1},
    624 : {'name' : '[A] Key Alarm', 'description' : 'A Auxillary key alarm has been restored (sent automatically).' , 'loglevel' : 1},
    625 : {'name' : '[P] Key Alarm', 'description' : 'A Panic key alarm has been detected.' , 'loglevel' : 1},
    626 : {'name' : '[P] Key Alarm', 'description' : 'A Panic key alarm has been restored (sent automatically).' , 'loglevel' : 1},
    631 : {'name' : '2-Wire Smoke/Aux Alarm', 'description' : 'A 2-wire smoke/Auxiliary alarm has been activated.' , 'loglevel' : 1, 'handler' : 'smoke'},
    632 : {'name' : '2-Wire Smoke/Aux Restore', 'description' : 'A 2-wire smoke/Auxiliary alarm has been restored.' , 'loglevel' : 1, 'handler' : 'smoke'},
    650 : {'name' : 'Partition {0} Ready', 'description' : 'Partition can now be armed (all zones restored, no troubles, etc). Also issued at the end of Bell Timeout if the partition was READY when an alarm occurred.' , 'loglevel' : 1, 'handler' : 'partition', 'parameters' : 1, 'status' : 'alarm', 'status_val' : True},
    651 : {'name' : 'Partition {0} Not Ready', 'description' : 'Partition cannot be armed (zones open, trouble present, etc).' , 'loglevel' : 1, 'handler' : 'partition', 'parameters' : 1, 'status' : 'ready', 'status_val' : False},
    652 : {'name' : 'Partition {0[0]} Armed Mode {0[1]}', 'description' : 'Partition has been armed - sent at the end of exit delay Also sent after an alarm if the Bell Cutoff Timer expires Mode is appended to indicate whether the partition is armed AWAY, STAY, ZERO-ENTRY-AWAY, or ZERO-ENTRY-STAY.' , 'loglevel' : 1, 'handler' : 'partition', 'parameters' : 1, 'status' : 'armed', 'status_val' : True},
    653 : {'name' : 'Partition {0} Ready - Force Arming Enabled', 'description' : 'Partition can now be armed (all zones restored, no troubles, etc). Also issued at the end of Bell Timeout if the partition was READY when an alarm occurred.' , 'loglevel' : 1, 'parameters' : 1},
    654 : {'name' : 'Partition {0} In Alarm', 'description' : 'A partition is in alarm.' , 'loglevel' : 1, 'handler' : 'partition', 'parameters' : 1, 'status' : 'armed', 'status_val' : True},
    655 : {'name' : 'Partition {0} Disarmed', 'description' : 'A partition has been disarmed.' , 'loglevel' : 1, 'handler' : 'partition', 'parameters' : 1, 'status' : 'armed', 'status_val' : False},
    656 : {'name' : 'Partition {0} Exit Delay in Progress', 'description' : 'A partition is in Exit Delay.' , 'loglevel' : 1, 'parameters' : 1},
    657 : {'name' : 'Partition {0} Entry Delay in Progress', 'description' : 'A partition is in Entry Delay.' , 'loglevel' : 1, 'parameters' : 1},
    658 : {'name' : 'Partition {0} Keypad Lock-out', 'description' : 'A partition is in Keypad Lockout due to too many failed user code attempts.' , 'loglevel' : 1, 'handler' : 'partition', 'parameters' : 1, 'status' : 'keypad_lockout'},
    659 : {'name' : 'Partition {0} Failed to Arm', 'description' : 'An attempt to arm the partition has failed.' , 'loglevel' : 1, 'parameters' : 1},
    660 : {'name' : 'Partition {0} PGM Output is in Progress', 'description' : '*71, *72, *73, or *74 has been pressed.' , 'loglevel' : 1, 'parameters' : 1, 'parameters' : 1},
    663 : {'name' : 'Partition {0} Chime Enabled', 'description' : 'The door chime feature has been enabled.' , 'loglevel' : 1, 'handler' : 'partition_chime', 'parameters' : 1},
    664 : {'name' : 'Partition {0} Chime Disabled', 'description' : 'The door chime feature has been disabled.' , 'loglevel' : 1, 'handler' : 'partition_chime', 'parameters' : 1},
    670 : {'name' : 'Partition {0} Invalid Access Code', 'description' : 'Invalid Access Code.' , 'loglevel' : 1, 'parameters' : 1},
    671 : {'name' : 'Partition {0} Function Not Available', 'description' : 'A partition is in Entry delay.' , 'loglevel' : 1, 'parameters' : 1},
    672 : {'name' : 'Partition {0} Failure to Arm', 'description' : 'An attempt was made to arm the partition and it failed.' , 'loglevel' : 1, 'parameters' : 1},
    673 : {'name' : 'Partition {0} is Busy', 'description' : 'The partition is busy (another keypad is programming or an installer is programming).' , 'loglevel' : 1, 'parameters' : 1},
    674 : {'name' : 'Partition {0} System Arming in Progress', 'description' : 'This system is auto-arming and is in arm warning delay.' , 'loglevel' : 1, 'parameters' : 1},
    700 : {'name' : 'Partition {0[0]} User {0[1]}{0[2]}{0[3]}{0[4]} Closing', 'description' : 'A partition has been armed by a user - sent at the end of exit delay.' , 'loglevel' : 1, 'handler' : 'partition', 'parameters' : 1, 'status' : 'armed', 'status_val' : True},
    701 : {'name' : 'Partition {0} Special Closing', 'description' : 'A partition has been armed by one of the following methods: Quick Arm, Auto Arm, Keyswitch, DLS software, Wireless Key.' , 'loglevel' : 1, 'handler' : 'partition', 'parameters' : 1, 'status' : 'armed', 'status_val' : True},
    702 : {'name' : 'Partition {0} Partial Closing', 'description' : 'A partition has been armed but one or more zones have been bypassed.' , 'loglevel' : 1, 'handler' : 'partition', 'parameters' : 1, 'handler' : 'partition', 'parameters' : 1, 'status' : 'armed', 'status_val' : True},
    750 : {'name' : 'Partition {0[0]} User {0[1]}{0[2]}{0[3]}{0[4]} Opening', 'description' : 'A partition has been disarmed by a user.' , 'loglevel' : 1, 'handler' : 'partition', 'parameters' : 1, 'status' : 'armed', 'status_val' : False},
    751 : {'name' : 'Partition {0} Special Opening', 'description' : 'A partition has been disarmed by one of the following methods: Keyswitch, DLS software, Wireless Key.' , 'loglevel' : 1, 'handler' : 'partition', 'parameters' : 1, 'status' : 'armed', 'status_val' : False},
    800 : {'name' : 'Panel Battery Trouble', 'description' : 'The panel has a low battery.' , 'loglevel' : 1},
    801 : {'name' : 'Panel Battery Trouble Restore', 'description' : 'The panel''s low battery has been restored.' , 'loglevel' : 1},
    802 : {'name' : 'Panel AC Trouble', 'description' : 'AC power to the panel has been removed.' , 'loglevel' : 1},
    803 : {'name' : 'Panel AC Restore', 'description' : 'AC power to the panel has been restored.' , 'loglevel' : 1},
    806 : {'name' : 'System Bell Trouble', 'description' : 'An open circuit has been detected across the bell terminals.' , 'loglevel' : 1},
    807 : {'name' : 'System Bell Trouble Restoral', 'description' : 'The bell trouble has been restored.' , 'loglevel' : 1},
    814 : {'name' : 'FTC Trouble', 'description' : 'The panel has failed to communicate successfully to the monitoring.' , 'loglevel' : 1},
    816 : {'name' : 'Battery Near Full', 'description' : 'Sent when the panel''s Event Buffer is 75% full from when it was last uploaded to DLS.' , 'loglevel' : 1},
    829 : {'name' : 'General System Tamper', 'description' : 'A tamper has occurred with one of the following modules: Zone Expander, PC5132, PC5204, PC5208, PC5400, PC59XX, LINKS 2X50, PC5108L, PC5100, PC5200.' , 'loglevel' : 1},
    830 : {'name' : 'General System Tamper Restore', 'description' : 'A general system Tamper has been restored.' , 'loglevel' : 1},
    840 : {'name' : 'Partition {0} Trouble LED ON', 'description' : 'This command shows the general trouble status that the trouble LED on a keypad normally shows. When ON, it means there is a trouble on this partition. This command when the LED transitions from OFF, to ON.' , 'loglevel' : 1, 'handler' : 'partition', 'parameters' : 1, 'status' : 'trouble', 'status_val' : True},
    841 : {'name' : 'Partition {0} Trouble LED OFF', 'description' : 'This command shows the general trouble status that the trouble LED on a keypad normally shows. When the LED is OFF, this usually means there are no troubles present on this partition but certain modes will blank this LED even in the presence of a partition trouble. This command when the LED transitions from ON, to OFF.' , 'loglevel' : 1, 'handler' : 'partition', 'parameters' : 1, 'status' : 'trouble', 'status_val' : False},
    842 : {'name' : 'Fire Trouble Alarm', 'description' : 'Fire Trouble Alarm' , 'loglevel' : 1},
    843 : {'name' : 'Fire Trouble Alarm Restore', 'description' : 'Fire Trouble Alarm Restore' , 'loglevel' : 1},
    849 : {'name' : 'Verbose Trouble Status', 'description' : 'This command is issued when a trouble appears on the system and roughly every 5 minutes until the trouble is cleared. The two characters are a bitfield (similar to 510,511). The meaning of each bit is the same as what you see on an LED keypad (see the user manual).' , 'loglevel' : 1},
    900 : {'name' : 'Code Required', 'description' : 'This command will tell the API to enter an access code. Once entered, the 200 command will be sent to perform the required action. The code should be entered within the window time of the panel.' , 'loglevel' : 1},
    912 : {'name' : 'Command Output Pressed', 'description' : 'This command will tell the API to enter an access code. Once entered, the 200 command will be sent to perform the required action. The code should be entered within the window time of the panel.' , 'loglevel' : 1},
    921 : {'name' : 'Master Code Required', 'description' : 'This command will tell the API to enter a master access code. Once entered, the 200 command will be sent to perform the required action. The code should be entered within the window time of the panel.' , 'loglevel' : 1},
    922 : {'name' : 'Installers Code Required', 'description' : 'This command will tell the API to enter an installers access code. Once entered, the 200 command will be sent to perform the required action. The code should be entered within the window time of the panel.' , 'loglevel' : 1},    
  }