import time
import datetime
import re
import shutil
import os
import RPi.GPIO as valve_swtch

cmd_sts = 0
cmd_count = 0
cmd_code = 0
cmd_code_tmp = 0
cmd_param = ""

VALVE1_PORT = 18
VALVE2_PORT = 24
VALVE3_PORT = 23
VALVE4_PORT = 17
VALVE5_PORT = 27
VALVE6_PORT = 5
VALVE7_PORT = 6
VALVE8_PORT = 13
VALVE9_PORT = 19
VALVE10_PORT = 26
VALVE11_PORT = 21
VALVE12_PORT = 20
valve_swtch.setmode(valve_swtch.BCM)
valve_swtch.setwarnings(False)
valve_swtch.setup(VALVE1_PORT, valve_swtch.OUT)
valve_swtch.setup(VALVE2_PORT, valve_swtch.OUT)
valve_swtch.setup(VALVE3_PORT, valve_swtch.OUT)
valve_swtch.setup(VALVE4_PORT, valve_swtch.OUT)
valve_swtch.setup(VALVE5_PORT, valve_swtch.OUT)
valve_swtch.setup(VALVE6_PORT, valve_swtch.OUT)
valve_swtch.setup(VALVE7_PORT, valve_swtch.OUT)
valve_swtch.setup(VALVE8_PORT, valve_swtch.OUT)
valve_swtch.setup(VALVE9_PORT, valve_swtch.OUT)
valve_swtch.setup(VALVE10_PORT, valve_swtch.OUT)
valve_swtch.setup(VALVE11_PORT, valve_swtch.OUT)
valve_swtch.setup(VALVE12_PORT, valve_swtch.OUT)
valve1_val = 0
valve2_val = 0
valve3_val = 0
valve4_val = 0
valve5_val = 0
valve6_val = 0
valve7_val = 0
valve8_val = 0
valve9_val = 0
valve10_val = 0
valve11_val = 0
valve12_val = 0
Mode = 0

def cmd_init():
    idle_mode()

def cmd_analyze(cmd, server):
    global cmd_sts
    global cmd_count
    global cmd_code_tmp
    global cmd_param

    ret = 0

    for i in range(len(cmd)):
        c = cmd[i]
        if cmd_sts == 0:
            if c == ord('c'):
                    cmd_sts = 1
            else:
                    cmd_sts = 0
        elif cmd_sts == 1:
            if c == ord('m'):
                    cmd_sts = 2
            else:
                    cmd_sts = 0
        elif cmd_sts == 2:
            cmd_code_tmp = c
            cmd_param = ""
            cmd_sts = 3
        elif cmd_sts == 3:
            cmd_param += chr(c)
            if(c == 0x0a):
                ret = cmd_action(server)
                cmd_sts = 0
    return ret

def cmd_action(server):
    global cmd_count
    global cmd_code
    global cmd_code_tmp
    global cmd_param
    global valve1_val
    global valve2_val
    global valve3_val
    global valve4_val
    global valve5_val
    global valve6_val
    global valve7_val
    global valve8_val
    global valve9_val
    global valve10_val
    global valve11_val
    global valve12_val

    ret = 0
    cmd_count += 1
    if cmd_code_tmp == ord('1'):    ##  Relay1
        s = re.findall(r'\b\d+\b', cmd_param)
        if (len(s) < 1):
            print("Valve1 Parameter Error",cmd_param)
            return 0
        if(int(s[0]) == 1):
            valve1_val = 1
            valve_swtch.output(VALVE1_PORT,1)
        else:
            valve1_val = 0
            valve_swtch.output(VALVE1_PORT,0)
        print("Valve1 Cmd", valve1_val)
    elif cmd_code_tmp == ord('2'):    ##  Relay2
        s = re.findall(r'\b\d+\b', cmd_param)
        if (len(s) < 1):
            print("Valve2 Parameter Error",cmd_param)
            return 0
        if(int(s[0]) == 1):
            valve2_val = 1
            valve_swtch.output(VALVE2_PORT,1)
        else:
            valve2_val = 0
            valve_swtch.output(VALVE2_PORT,0)
        print("Valve2 Cmd", valve2_val)
    elif cmd_code_tmp == ord('3'):    ##  Relay3
        s = re.findall(r'\b\d+\b', cmd_param)
        if (len(s) < 1):
            print("Valve3 Parameter Error",cmd_param)
            return 0
        if(int(s[0]) == 1):
            valve3_val = 1
            valve_swtch.output(VALVE3_PORT,1)
        else:
            valve3_val = 0
            valve_swtch.output(VALVE3_PORT,0)
        print("Valve3 Cmd", valve3_val)
    elif cmd_code_tmp == ord('4'):    ##  Relay4
        s = re.findall(r'\b\d+\b', cmd_param)
        if (len(s) < 1):
            print("Valve4 Parameter Error",cmd_param)
            return 0
        if(int(s[0]) == 1):
            valve4_val = 1
            valve_swtch.output(VALVE4_PORT,1)
        else:
            valve4_val = 0
            valve_swtch.output(VALVE4_PORT,0)
        print("Valve4 Cmd", valve4_val)
    elif cmd_code_tmp == ord('5'):    ##  Relay5
        s = re.findall(r'\b\d+\b', cmd_param)
        if (len(s) < 1):
            print("Valve5 Parameter Error",cmd_param)
            return 0
        if(int(s[0]) == 1):
            valve5_val = 1
            valve_swtch.output(VALVE5_PORT,1)
        else:
            valve5_val = 0
            valve_swtch.output(VALVE5_PORT,0)
        print("Valve5 Cmd", valve5_val)
    elif cmd_code_tmp == ord('6'):    ##  Relay6
        s = re.findall(r'\b\d+\b', cmd_param)
        if (len(s) < 1):
            print("Valve6 Parameter Error",cmd_param)
            return 0
        if(int(s[0]) == 1):
            valve6_val = 1
            valve_swtch.output(VALVE6_PORT,1)
        else:
            valve6_val = 0
            valve_swtch.output(VALVE6_PORT,0)
        print("Valve6 Cmd", valve6_val)
    elif cmd_code_tmp == ord('7'):    ##  Relay7
        s = re.findall(r'\b\d+\b', cmd_param)
        if (len(s) < 1):
            print("Valve7 Parameter Error",cmd_param)
            return 0
        if(int(s[0]) == 1):
            valve7_val = 1
            valve_swtch.output(VALVE7_PORT,1)
        else:
            valve7_val = 0
            valve_swtch.output(VALVE7_PORT,0)
        print("Valve7 Cmd", valve7_val)
    elif cmd_code_tmp == ord('8'):    ##  Relay8
        s = re.findall(r'\b\d+\b', cmd_param)
        if (len(s) < 1):
            print("Valve8 Parameter Error",cmd_param)
            return 0
        if(int(s[0]) == 1):
            valve8_val = 1
            valve_swtch.output(VALVE8_PORT,1)
        else:
            valve8_val = 0
            valve_swtch.output(VALVE8_PORT,0)
        print("Valve8 Cmd", valve8_val)
    elif cmd_code_tmp == ord('9'):    ##  Relay9
        s = re.findall(r'\b\d+\b', cmd_param)
        if (len(s) < 1):
            print("Valve9 Parameter Error",cmd_param)
            return 0
        if(int(s[0]) == 1):
            valve9_val = 1
            valve_swtch.output(VALVE9_PORT,1)
        else:
            valve9_val = 0
            valve_swtch.output(VALVE9_PORT,0)
        print("Valve9 Cmd", valve9_val)
    elif cmd_code_tmp == ord('A'):    ##  Relay10
        s = re.findall(r'\b\d+\b', cmd_param)
        if (len(s) < 1):
            print("Valve10 Parameter Error",cmd_param)
            return 0
        if(int(s[0]) == 1):
            valve10_val = 1
            valve_swtch.output(VALVE10_PORT,1)
        else:
            valve10_val = 0
            valve_swtch.output(VALVE10_PORT,0)
        print("Valve10 Cmd", valve10_val)
    elif cmd_code_tmp == ord('B'):    ##  Relay11
        s = re.findall(r'\b\d+\b', cmd_param)
        if (len(s) < 1):
            print("Valve11 Parameter Error",cmd_param)
            return 0
        if(int(s[0]) == 1):
            valve11_val = 1
            valve_swtch.output(VALVE11_PORT,1)
        else:
            valve11_val = 0
            valve_swtch.output(VALVE11_PORT,0)
        print("Valve11 Cmd", valve11_val)
    elif cmd_code_tmp == ord('C'):    ##  Relay12
        s = re.findall(r'\b\d+\b', cmd_param)
        if (len(s) < 1):
            print("Valve12 Parameter Error",cmd_param)
            return 0
        if(int(s[0]) == 1):
            valve12_val = 1
            valve_swtch.output(VALVE12_PORT,1)
        else:
            valve12_val = 0
            valve_swtch.output(VALVE12_PORT,0)
        print("Valve12 Cmd", valve12_val)
    elif cmd_code_tmp == ord('a'):    ##  Idle_1
        idle_mode1()
        print("Idle1 Cmd")
    elif cmd_code_tmp == ord('b'):    ##  Vent_1
        vent_mode1()
        print("Vent1 Cmd")
    elif cmd_code_tmp == ord('c'):    ##  Inflate_1
        inf_mode1()
        print("Inflate1 Cmd")
    elif cmd_code_tmp == ord('d'):    ##  Idle_2
        idle_mode2()
        print("Idle2 Cmd")
    elif cmd_code_tmp == ord('e'):    ##  Vent_2
        vent_mode2()
        print("Vent2 Cmd")
    elif cmd_code_tmp == ord('f'):    ##  Inflate_2
        inf_mode2()
        print("Inflate2 Cmd")
    elif cmd_code_tmp == ord('g'):    ##  Idle_3
        idle_mode3()
        print("Idle3 Cmd")
    elif cmd_code_tmp == ord('h'):    ##  Vent_3
        vent_mode3()
        print("Vent3 Cmd")
    elif cmd_code_tmp == ord('i'):    ##  Inflate_3
        inf_mode3()
        print("Inflate3 Cmd")
    elif cmd_code_tmp == ord('j'):    ##  Idle_4
        idle_mode4()
        print("Idle4 Cmd")
    elif cmd_code_tmp == ord('k'):    ##  Vent_4
        vent_mode4()
        print("Vent4 Cmd")
    elif cmd_code_tmp == ord('l'):    ##  Inflate_4
        inf_mode4()
        print("Inflate4 Cmd")
    elif cmd_code_tmp == ord('m'):    ##  Idle_5
        idle_mode5()
        print("Idle5 Cmd")
    elif cmd_code_tmp == ord('n'):    ##  Vent_5
        vent_mode5()
        print("Vent5 Cmd")
    elif cmd_code_tmp == ord('o'):    ##  Inflate_5
        inf_mode5()
        print("Inflate5 Cmd")
    elif cmd_code_tmp == ord('p'):    ##  Idle_6
        idle_mode6()
        print("Idle6 Cmd")
    elif cmd_code_tmp == ord('q'):    ##  Vent_6
        vent_mode6()
        print("Vent6 Cmd")
    elif cmd_code_tmp == ord('r'):    ##  Inflate_6
        inf_mode6()
        print("Inflate6 Cmd")
    else:
        print("NA Cmd")

    return ret

def idle_mode():
    global valve1_val
    global valve2_val
    global valve3_val
    global valve4_val
    global valve5_val
    global valve6_val
    global valve7_val
    global valve8_val
    global valve9_val
    global valve10_val
    global valve11_val
    global valve12_val
    global Mode
    valve_swtch.output(VALVE1_PORT,0)
    valve_swtch.output(VALVE2_PORT,0)
    valve_swtch.output(VALVE3_PORT,0)
    valve_swtch.output(VALVE4_PORT,0)
    valve_swtch.output(VALVE5_PORT,0)
    valve_swtch.output(VALVE6_PORT,0)
    valve_swtch.output(VALVE7_PORT,0)
    valve_swtch.output(VALVE8_PORT,0)
    valve_swtch.output(VALVE9_PORT,0)
    valve_swtch.output(VALVE10_PORT,0)
    valve_swtch.output(VALVE11_PORT,0)
    valve_swtch.output(VALVE12_PORT,0)
    time.sleep(0.1)
    valve1_val = 0
    valve2_val = 0
    valve3_val = 0
    valve4_val = 0
    valve5_val = 0
    valve6_val = 0
    valve7_val = 0
    valve8_val = 0
    valve9_val = 0
    valve10_val = 0
    valve11_val = 0
    valve12_val = 0
    Mode = 0

def idle_mode1():
    global valve1_val
    global valve7_val
    global Mode
    valve_swtch.output(VALVE1_PORT,0)
    valve_swtch.output(VALVE7_PORT,0)
    time.sleep(0.1)
    valve1_val = 0
    valve7_val = 0
    Mode = 1

def vent_mode1():
    global valve1_val
    global valve7_val
    global Mode
    valve_swtch.output(VALVE1_PORT,0)
    valve_swtch.output(VALVE7_PORT,1)
    time.sleep(0.1)
    valve1_val = 0
    valve7_val = 1
    Mode = 2

def inf_mode1():
    global valve1_val
    global valve7_val
    global Mode
    valve_swtch.output(VALVE1_PORT,1)
    valve_swtch.output(VALVE7_PORT,0)
    time.sleep(0.1)
    valve1_val = 1
    valve7_val = 0
    Mode = 3

def idle_mode2():
    global valve2_val
    global valve8_val
    global Mode
    valve_swtch.output(VALVE2_PORT,0)
    valve_swtch.output(VALVE8_PORT,0)
    time.sleep(0.1)
    valve1_val = 0
    valve7_val = 0
    Mode = 4

def vent_mode2():
    global valve2_val
    global valve8_val
    global Mode
    valve_swtch.output(VALVE2_PORT,0)
    valve_swtch.output(VALVE8_PORT,1)
    time.sleep(0.1)
    valve2_val = 0
    valve8_val = 1
    Mode = 5

def inf_mode2():
    global valve2_val
    global valve8_val
    global Mode
    valve_swtch.output(VALVE2_PORT,1)
    valve_swtch.output(VALVE8_PORT,0)
    time.sleep(0.1)
    valve2_val = 1
    valve8_val = 0
    Mode = 6

def idle_mode3():
    global valve3_val
    global valve9_val
    global Mode
    valve_swtch.output(VALVE3_PORT,0)
    valve_swtch.output(VALVE9_PORT,0)
    time.sleep(0.1)
    valve1_val = 0
    valve7_val = 0
    Mode = 7

def vent_mode3():
    global valve3_val
    global valve9_val
    global Mode
    valve_swtch.output(VALVE3_PORT,0)
    valve_swtch.output(VALVE9_PORT,1)
    time.sleep(0.1)
    valve3_val = 0
    valve9_val = 1
    Mode = 8

def inf_mode3():
    global valve3_val
    global valve9_val
    global Mode
    valve_swtch.output(VALVE3_PORT,1)
    valve_swtch.output(VALVE9_PORT,0)
    time.sleep(0.1)
    valve3_val = 1
    valve9_val = 0
    Mode = 9

def idle_mode4():
    global valve4_val
    global valve10_val
    global Mode
    valve_swtch.output(VALVE4_PORT,0)
    valve_swtch.output(VALVE10_PORT,0)
    time.sleep(0.1)
    valve4_val = 0
    valve10_val = 0
    Mode = 10

def vent_mode4():
    global valve4_val
    global valve10_val
    global Mode
    valve_swtch.output(VALVE4_PORT,0)
    valve_swtch.output(VALVE10_PORT,1)
    time.sleep(0.1)
    valve4_val = 0
    valve10_val = 1
    Mode = 11

def inf_mode4():
    global valve4_val
    global valve10_val
    global Mode
    valve_swtch.output(VALVE4_PORT,1)
    valve_swtch.output(VALVE10_PORT,0)
    time.sleep(0.1)
    valve4_val = 1
    valve10_val = 0
    Mode = 12

def idle_mode5():
    global valve5_val
    global valve11_val
    global Mode
    valve_swtch.output(VALVE5_PORT,0)
    valve_swtch.output(VALVE11_PORT,0)
    time.sleep(0.1)
    valve5_val = 0
    valve11_val = 0
    Mode = 13

def vent_mode5():
    global valve5_val
    global valve11_val
    global Mode
    valve_swtch.output(VALVE5_PORT,0)
    valve_swtch.output(VALVE11_PORT,1)
    time.sleep(0.1)
    valve5_val = 0
    valve11_val = 1
    Mode = 14

def inf_mode5():
    global valve5_val
    global valve11_val
    global Mode
    valve_swtch.output(VALVE5_PORT,1)
    valve_swtch.output(VALVE11_PORT,0)
    time.sleep(0.1)
    valve5_val = 1
    valve11_val = 0
    Mode = 15

def idle_mode6():
    global valve6_val
    global valve12_val
    global Mode
    valve_swtch.output(VALVE6_PORT,0)
    valve_swtch.output(VALVE12_PORT,0)
    time.sleep(0.1)
    valve6_val = 0
    valve12_val = 0
    Mode = 16

def vent_mode6():
    global valve6_val
    global valve12_val
    global Mode
    valve_swtch.output(VALVE6_PORT,0)
    valve_swtch.output(VALVE12_PORT,1)
    time.sleep(0.1)
    valve6_val = 0
    valve12_val = 1
    Mode = 17

def inf_mode6():
    global valve6_val
    global valve12_val
    global Mode
    valve_swtch.output(VALVE6_PORT,1)
    valve_swtch.output(VALVE12_PORT,0)
    time.sleep(0.1)
    valve6_val = 1
    valve12_val = 0
    Mode = 18

