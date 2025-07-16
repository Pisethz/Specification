import platform
import psutil
import socket
import os
import subprocess
import sys
import io
import re
import os

try:
    import GPUtil
    gpu_available = True
except ImportError:
    gpu_available = False

try:
    import cpuinfo
    cpuinfo_available = True
except ImportError:
    cpuinfo_available = False

try:
    from colorama import init, Fore, Style
    colorama_available = True
    init(autoreset=True)
except ImportError:
    colorama_available = False


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    banner = r"""
                          _____                          
                   _.+sd$$$$$$$$$bs+._                   
               .+d$$$$$$$$$$$$$$$$$$$$$b+.               
            .sd$$$$$$$P^*^T$$$P^*"*^T$$$$$bs.            
          .s$$$$$$$$P*     `*' _._  `T$$$$$$$s.          
        .s$$$$$$$$$P          ` :$;   T$$$$$$$$s.        
       s$$$$$$$$$$;  db..+s.   `**'    T$$$$$$$$$s       
     .$$$$$$$$$$$$'  `T$P*'             T$$$$$$$$$$.     
    .$$$$$$$$$$$$P                       T$$$$$$$$$$.    
   .$$$$$$$$$$$$$b                       `$$$$$$$$$$$.   
  :$$$$$$$$$$$$$$$.                       T$$$$$$$$$$$;  
  $$$$$$$$$P^*' :$$b.                     d$$$$$$$$$$$$  
 :$$$$$$$P'      T$$$$bs._               :P'`*^T$$$$$$$; 
 $$$$$$$P         `*T$$$$$b              '      `T$$$$$$ 
:$$$$$$$b            `*T$$$s                      :$$$$$;
:$$$$$$$$b.                                        $$$$$;
$$$$$$$$$$$b.                                     :$$$$$$
$$$$$$$$$$$$$bs.                                 .$$$$$$$
$$$$$$$$$$$$$$$$$bs.                           .d$$$$$$$$
:$$$$$$$$$$$$$P*"*T$$bs,._                  .sd$$$$$$$$$;
:$$$$$$$$$$$$P     TP^**T$bss++.._____..++sd$$$$$$$$$$$$;
 $$$$$$$$$$$$b           `T$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ 
 :$$$$$$$$$$$$b.           `*T$$P^*"*"*^^*T$$$$$$$$$$$$; 
  $$$b       `T$b+                        :$$$$$$$BUG$$  
  :$P'         `"'               ,._.     ;$$$$$$$$$$$;  
   \                            `*TP*     d$$P*******$   
    \                                    :$$P'      /    
     \                                  :dP'       /     
      `.                               d$P       .'      
[bug]   `.                             `'      .'        
          `-.                               .-'          
             `-.                         .-'             
                `*+-._             _.-+*'                
                      `"*-------*"'
  ___  _____   _____ _          _   _                    _____    _____                                   _ 
 |__ \| ____| |  __ (_)        | | | |             /\   |  __ \  |  __ \                                 | |
    ) | |__   | |__) | ___  ___| |_| |__  ____    /  \  | |__) | | |__) |___  ___  ___ _ ____   _____  __| |
   / /|___ \  |  ___/ / __|/ _ \ __| '_ \|_  /   / /\ \ |  _  /  |  _  // _ \/ __|/ _ \ '__\ \ / / _ \/ _` |
  / /_ ___) | | |   | \__ \  __/ |_| | | |/ /   / ____ \| | \ \  | | \ \  __/\__ \  __/ |   \ V /  __/ (_| |
 |____|____/  |_|   |_|___/\___|\__|_| |_/___| /_/    \_\_|  \_\ |_|  \_\___||___/\___|_|    \_/ \___|\__,_|
                                        Pisethz x JackyJackyHunt!!
                                    © 2025 Pisethz. All Rights Reserved
    """
    if colorama_available:
        print(Fore.CYAN + banner + Style.RESET_ALL)
    else:
        print(banner)
    print("=" * 60)
    print()



def section_header(title):
    if colorama_available:
        print(Fore.GREEN + f"[ {title} ]" + Style.RESET_ALL)
    else:
        print(f"[ {title} ]")
    print("-" * 40)

def get_cpu_info():
    section_header("CPU Info")
    if cpuinfo_available:
        info = cpuinfo.get_cpu_info()
        print(f"  {Style.BRIGHT if colorama_available else ''}Marketing Name:{Style.RESET_ALL if colorama_available else ''} {info.get('brand_raw', 'N/A')}")
    else:
        print("  Marketing Name: (Install 'py-cpuinfo' for this info)")
    print(f"  {Style.BRIGHT if colorama_available else ''}Internal Code:{Style.RESET_ALL if colorama_available else ''} {platform.processor()}")
    print(f"  Cores (physical): {psutil.cpu_count(logical=False)}")
    print(f"  Cores (total): {psutil.cpu_count(logical=True)}")
    print(f"  Frequency: {psutil.cpu_freq().current:.2f} MHz")
    print()

def get_memory_info():
    section_header("Memory (RAM)")
    mem = psutil.virtual_memory()
    print(f"  Total: {mem.total / (1024 ** 3):.2f} GB")
    print(f"  Available: {mem.available / (1024 ** 3):.2f} GB")
    print()

def get_disk_info():
    section_header("Disk Info")
    for part in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(part.mountpoint)
            print(f"  Device: {part.device}")
            print(f"    Mountpoint: {part.mountpoint}")
            print(f"    File system type: {part.fstype}")
            print(f"    Total Size: {usage.total / (1024 ** 3):.2f} GB")
            print(f"    Used: {usage.used / (1024 ** 3):.2f} GB")
            print(f"    Free: {usage.free / (1024 ** 3):.2f} GB")
            print(f"    Usage: {usage.percent}%")
        except PermissionError:
            continue
    print()

def get_os_info():
    section_header("Operating System Info")
    print(f"  System: {platform.system()}")
    print(f"  Node Name: {platform.node()}")
    print(f"  Release: {platform.release()}")
    print(f"  Version: {platform.version()}")
    print(f"  Machine: {platform.machine()}")
    print(f"  Processor: {platform.processor()}")
    print()

def get_gpu_info():
    section_header("GPU Info")
    if gpu_available:
        gpus = GPUtil.getGPUs()
        if not gpus:
            print("  No GPU found.")
        for gpu in gpus:
            print(f"  GPU: {gpu.name}")
            print(f"    ID: {gpu.id}")
            print(f"    Memory Total: {gpu.memoryTotal}MB")
            print(f"    Memory Free: {gpu.memoryFree}MB")
            print(f"    Memory Used: {gpu.memoryUsed}MB")
            print(f"    Driver: {gpu.driver}")
            print(f"    Serial: {gpu.serial}")
            print(f"    UUID: {gpu.uuid}")
    else:
        print("  GPUtil not installed. Run 'pip install gputil' to get GPU info.")
    print()

def get_network_info():
    section_header("Network Info")
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print(f"  Hostname: {hostname}")
    print(f"  IP Address: {ip_address}")
    print()

def get_battery_info():
    section_header("Battery Info")
    battery = psutil.sensors_battery()
    if battery is None:
        print("  No battery found or not supported on this device.")
    else:
        print(f"  Percentage: {battery.percent}%")
        print(f"  Plugged in: {'Yes' if battery.power_plugged else 'No'}")
        if battery.secsleft != psutil.POWER_TIME_UNLIMITED and battery.secsleft != psutil.POWER_TIME_UNKNOWN:
            hours, remainder = divmod(battery.secsleft, 3600)
            minutes, _ = divmod(remainder, 60)
            print(f"  Time left: {hours}h {minutes}m")
        else:
            print("  Time left: Calculating or unlimited.")
    print()

def get_platform():
    plat = sys.platform
    if plat.startswith('win'):
        return 'windows'
    elif plat.startswith('linux'):
        # Try to detect Android
        try:
            with open('/system/build.prop') as f:
                return 'android'
        except Exception:
            return 'linux'
    else:
        return plat

PLATFORM = get_platform()

def run_cmd(cmd):
    try:
        result = subprocess.check_output(cmd, shell=True, stderr=subprocess.DEVNULL, universal_newlines=True)
        return result.strip()
    except Exception:
        return None

def get_wifi_info():
    section_header("WiFi Info")
    if PLATFORM == 'windows':
        output = run_cmd('netsh wlan show interfaces')
        if output:
            for line in output.splitlines():
                if any(key in line for key in ['Name', 'Description', 'State', 'Physical address', 'SSID']):
                    print(' ', line.strip())
        else:
            print("  No WiFi adapter found or not connected.")
    elif PLATFORM == 'linux':
        output = run_cmd('nmcli device status')
        if output:
            print(output)
        else:
            print("  No WiFi info available (try running as root or install nmcli).")
    elif PLATFORM == 'android':
        output = run_cmd('ip addr')
        if output:
            for line in output.splitlines():
                if 'wlan' in line or 'wifi' in line:
                    print(' ', line.strip())
        else:
            print("  No WiFi info available on Android.")
    else:
        print("  Platform not supported.")
    print()

def get_bluetooth_info():
    section_header("Bluetooth Info")
    if PLATFORM == 'windows':
        output = run_cmd('powershell "Get-PnpDevice -Class Bluetooth | Format-Table -AutoSize"')
        if output:
            print(output)
        else:
            print("  No Bluetooth adapter found.")
    elif PLATFORM == 'linux':
        output = run_cmd('bluetoothctl list')
        if output:
            print(output)
        else:
            print("  No Bluetooth info available (try running as root or install bluetoothctl).")
    elif PLATFORM == 'android':
        output = run_cmd('getprop | grep bluetooth')
        if output:
            print(output)
        else:
            print("  No Bluetooth info available on Android.")
    else:
        print("  Platform not supported.")
    print()

def get_system_info():
    section_header("System/Brand Info")
    if PLATFORM == 'windows':
        manufacturer = run_cmd('wmic computersystem get manufacturer')
        model = run_cmd('wmic computersystem get model')
        serial = run_cmd('wmic bios get serialnumber')
        bios = run_cmd('wmic bios get smbiosbiosversion')
        print(f"  Manufacturer: {manufacturer.splitlines()[1].strip() if manufacturer and len(manufacturer.splitlines()) > 1 else 'N/A'}")
        print(f"  Model: {model.splitlines()[1].strip() if model and len(model.splitlines()) > 1 else 'N/A'}")
        print(f"  Serial Number: {serial.splitlines()[1].strip() if serial and len(serial.splitlines()) > 1 else 'N/A'}")
        print(f"  BIOS Version: {bios.splitlines()[1].strip() if bios and len(bios.splitlines()) > 1 else 'N/A'}")
    elif PLATFORM == 'linux':
        def read_sys_file(path):
            try:
                with open(path) as f:
                    return f.read().strip()
            except Exception:
                return 'N/A'
        manufacturer = read_sys_file('/sys/class/dmi/id/sys_vendor')
        model = read_sys_file('/sys/class/dmi/id/product_name')
        serial = read_sys_file('/sys/class/dmi/id/product_serial')
        bios = read_sys_file('/sys/class/dmi/id/bios_version')
        print(f"  Manufacturer: {manufacturer}")
        print(f"  Model: {model}")
        print(f"  Serial Number: {serial}")
        print(f"  BIOS Version: {bios}")
    elif PLATFORM == 'android':
        brand = run_cmd('getprop ro.product.brand')
        model = run_cmd('getprop ro.product.model')
        serial = run_cmd('getprop ro.serialno')
        print(f"  Brand: {brand if brand else 'N/A'}")
        print(f"  Model: {model if model else 'N/A'}")
        print(f"  Serial Number: {serial if serial else 'N/A'}")
    else:
        print("  Platform not supported.")
    print()

def get_motherboard_info():
    section_header("Motherboard Info")
    if PLATFORM == 'windows':
        board = run_cmd('wmic baseboard get product,manufacturer,serialnumber')
        if board:
            print(board)
        else:
            print("  No motherboard info found.")
    elif PLATFORM == 'linux':
        def read_sys_file(path):
            try:
                with open(path) as f:
                    return f.read().strip()
            except Exception:
                return 'N/A'
        manufacturer = read_sys_file('/sys/class/dmi/id/board_vendor')
        product = read_sys_file('/sys/class/dmi/id/board_name')
        serial = read_sys_file('/sys/class/dmi/id/board_serial')
        print(f"  Manufacturer: {manufacturer}")
        print(f"  Product: {product}")
        print(f"  Serial Number: {serial}")
    elif PLATFORM == 'android':
        board = run_cmd('getprop ro.product.board')
        print(f"  Board: {board if board else 'N/A'}")
    else:
        print("  Platform not supported.")
    print()

def strip_ansi_codes(text):
    ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
    return ansi_escape.sub('', text)


def main():
    clear_screen()
    output_buffer = io.StringIO()
    sys_stdout = sys.stdout
    sys.stdout = output_buffer
    print_banner()
    get_system_info()
    get_motherboard_info()
    get_cpu_info()
    get_memory_info()
    get_disk_info()
    get_os_info()
    get_gpu_info()
    get_network_info()
    get_wifi_info()
    get_bluetooth_info()
    get_battery_info()
    get_platform()
    print("=" * 60)
    if colorama_available:
        print(Fore.YELLOW + Style.BRIGHT + "End of Specification" + Style.RESET_ALL)
    else:
        print("End of Specification")
    sys.stdout = sys_stdout
    # Print to screen
    print(output_buffer.getvalue())
    # Ask to save
    answer = input("Are you want to save this? (y/n): ").strip().lower()
    if answer == 'y':
        filename = input("Enter filename to save (e.g., spec.txt): ").strip()
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(strip_ansi_codes(output_buffer.getvalue()))
            print(f"Specification saved to {filename}")
        except Exception as e:
            print(f"Failed to save file: {e}")
    else:
        print("Specification not saved.")

if __name__ == "__main__":
    main()
