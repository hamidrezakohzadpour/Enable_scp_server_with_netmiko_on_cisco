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
if not os.path.exists("configs"):
    os.mkdir("configs")
if not os.path.exists("configs\\device_ip.txt"):
    file = open("configs\\device_ip.txt", 'a')
    print (Fore.RED + "Please add IP Addresses to configs\\device_ip.txt" + Fore.WHITE)
    file.close()
    exit()
with open ("configs\\device_ip.txt",'r') as f:
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