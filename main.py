import platform 
import psutil
import wmi
import os

kernel = os.name

computerName = platform.node() # Computer name (Desktop xxxxx)

# Your operating system {
operatingSystem = platform.system() # OS name
operatingSystemVersion = platform.version() # OS version
windowsVersion = platform.win32_edition() # Windows edition (pro, home vs.)
operatingSystemArc = platform.architecture()[0] # OS Arc
userNames = psutil.users()[0] # Usernames
userName = userNames[0] # Username
# }

# SYSTEM {

system = wmi.WMI()

# === CPU INFO === #

# CPU name { 
CPUInfo = system.Win32_Processor()[0]
CPUName = CPUInfo.Name
# }

# CPU speed {
CPUSpeed = psutil.cpu_freq()[0] 
CPUSpeed = str(CPUSpeed)  
CPUSpeed = CPUSpeed[0] + "." + CPUSpeed[1:3]
# }

# CPU arc {
CPUArc = platform.machine() # CPU Arc
# }

# === STORGE === #

# RAM {
RAM = psutil.virtual_memory()[0] # RAM
RAM = int(RAM) / 1024 / 1024 / 1024 #kb to mb to gb
RAM = str(RAM)
RAM = RAM[0:3]

swap = psutil.swap_memory()[0] # Swap
swap = int(swap) / 1024 / 1024 / 1024 #kb to mb to gb
# }

# Discs {
discs = psutil.disk_partitions() 
# }

# Battery and power {
charge = psutil.sensors_battery()[0]
power = psutil.sensors_battery()[2] 

if power == False:
    power = "Not connected"
    
elif power == True:
    power = "Connected"
# }
# }

# Language versions {
pythonVersion = platform.python_version() 
# }

def windowsEng():
    return f"""Computer Name : {computerName}
          
\t\tOPERATING SYSTEM

Operating System              : {operatingSystem}
Operating System Version      : {operatingSystemVersion} 
Windows Version               : {windowsVersion}
Operating System Architecture : {operatingSystemArc}
User Name                     : {userName}

\t\tABOUT SYSTEM

CPU                          : {CPUName}
CPU Speed                    : {CPUSpeed} GHz
CPU Architecture             : {CPUArc}
RAM Capacity                 : {RAM} GB
Swap                         : {swap} GB
Charge                       : {charge}
Is it connected to a power?  : {power}

\t\tLANGUAGE VERSIONS
Python Version               : {pythonVersion}

Discs                        :\n
{discs}
"""
    
with open("Your System.txt","w",encoding="utf8") as file:
    file.write(windowsEng())
    file.close()
    
input("You can exit by pressing any key...")  
