import os
import paramiko
from colorama import Fore
from datetime import datetime
from netmiko  import ConnectHandler

def str_date_time():
    now = datetime.now()
    str_date = now.strftime("%Y%m%d")
    str_time = now.strftime("%H%M%S")
    return "_" + str_date + "_" + str_time

def input_file_address():
    OSNAME = (os.name)
    if OSNAME == "nt":
        return 'configs\\device_ip.txt'
    elif OSNAME == "posix":
        return 'configs/device_ip.txt'

if not os.path.exists(input_file_address()):
    os.mkdir('configs')
    file = open(input_file_address(), 'a')
    print (Fore.RED + "Please add IP Addresses to configs\\device_ip.txt" + Fore.WHITE)
    file.close()
    exit()

with open (input_file_address(),'r') as f:
    devices_list = f.read().splitlines()
    f.close()
for ip_address in devices_list:
    Switch = { 
            'device_type': 'cisco_ios',
            "ip": ip_address,
            "username": "username",
            "password": "password"
            }
    try:
        print(Fore.WHITE + f"{'=' * 50}\nConnecting to the Device {Switch['ip']}")    
        net_connect = ConnectHandler(**Switch)
    except:
        print(Fore.RED + f"Connecting Failed on {Switch['ip']}" + Fore.WHITE)
    else:
        config_commands = [ "ip scp server enable"]
        output = net_connect.send_config_set(config_commands)
        print(Fore.GREEN + output + Fore.WHITE)           