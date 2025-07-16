import os

def clear_screen():
    os.system('clear' if os.name != 'nt' else 'cls')

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
                                        Android Device Specification
                                    © 2025 Pisethz. All Rights Reserved
    """
    print(banner)
    print("=" * 50)
    print()

def section_header(title):
    print(f"[ {title} ]")
    print("-" * 30)

def getprop(prop):
    value = os.popen(f"getprop {prop}").read().strip()
    return value if value else 'N/A'

def command_exists(cmd):
    return os.system(f'command -v {cmd} > /dev/null 2>&1') == 0

def get_android_info():
    section_header("Android Device Info")
    print(f"Brand: {getprop('ro.product.brand')}")
    print(f"Model: {getprop('ro.product.model')}")
    print(f"Android Version: {getprop('ro.build.version.release')}")
    print(f"Security Patch: {getprop('ro.build.version.security_patch')}")
    print(f"Build ID: {getprop('ro.build.display.id')}")
    print(f"CPU ABI: {getprop('ro.product.cpu.abi')}")
    print(f"Supported ABIs: {getprop('ro.product.cpu.abilist')}")
    print(f"Device: {getprop('ro.product.device')}")
    print(f"Manufacturer: {getprop('ro.product.manufacturer')}")
    print(f"Board: {getprop('ro.product.board')}")
    print(f"Hardware: {getprop('ro.hardware')}")
    print(f"Bootloader: {getprop('ro.bootloader')}")
    print(f"Radio Version: {getprop('gsm.version.baseband')}")
    print(f"Fingerprint: {getprop('ro.build.fingerprint')}")
    print(f"Display: {getprop('ro.build.display.id')}")
    print(f"Product: {getprop('ro.build.product')}")
    # IMEI is not accessible without root and special permissions, but try anyway
    imei = getprop('ril.gsm.imei')
    if imei == 'N/A':
        imei = getprop('persist.radio.imei')
    print(f"IMEI: {imei}")
    print()

def get_android_connectivity():
    section_header("Connectivity & Services")

    # WiFi status and SSID
    if command_exists('dumpsys'):
        ssid = os.popen("dumpsys wifi | grep 'SSID' | head -1").read().strip()
    else:
        ssid = 'dumpsys not available'
    wifi_state = getprop('wifi.interface')
    wifi_enabled = getprop('wifi.status')
    print(f"WiFi Interface: {wifi_state}")
    print(f"WiFi Status: {wifi_enabled if wifi_enabled != 'N/A' else 'Unknown'}")
    print(f"WiFi SSID: {ssid if ssid else 'N/A'}")

    # Mobile data
    mobile_data = getprop('gsm.defaultpdpcontext.active')
    print(f"Mobile Data: {'On' if mobile_data == 'true' else 'Off or Unknown'}")

    # Bluetooth
    bt_state = getprop('bluetooth.status')
    if bt_state == 'N/A' and command_exists('settings'):
        bt_state = os.popen("settings get global bluetooth_on").read().strip()
    print(f"Bluetooth: {'On' if bt_state == '1' else 'Off or Unknown'}")

    # Airplane mode
    if command_exists('settings'):
        airplane = os.popen("settings get global airplane_mode_on").read().strip()
        print(f"Airplane Mode: {'On' if airplane == '1' else 'Off'}")
    else:
        print("Airplane Mode: settings command not available")

    # Location
    if command_exists('settings'):
        location = os.popen("settings get secure location_providers_allowed").read().strip()
        print(f"Location (GPS): {'Enabled' if location else 'Disabled'}")
    else:
        print("Location (GPS): settings command not available")

    # Personal Hotspot (Tethering)
    if command_exists('settings'):
        tethering = os.popen("settings get global tether_dun_required").read().strip()
        print(f"Personal Hotspot: {'Maybe On' if tethering == '1' else 'Off or Unknown'}")
    else:
        print("Personal Hotspot: settings command not available")

    print()

def list_installed_apps():
    section_header("Installed Apps")
    if not command_exists('pm'):
        print("pm command not found. Cannot list apps.")
        return
    apps = os.popen("pm list packages").read().strip().split('\n')
    if not apps or apps == ['']:
        print("Could not retrieve app list (may require Termux:API or root).")
    else:
        for app in apps:
            print(app.replace('package:', ''))
    print()

def main():
    clear_screen()
    print_banner()
    get_android_info()
    get_android_connectivity()
    list_installed_apps()
    print("=" * 50)
    print("End of Mobile Specification\n")

if __name__ == "__main__":
    main()
