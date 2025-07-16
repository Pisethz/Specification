# 🚀 Computer/Device Full Specification CLI Tool

![Python](https://img.shields.io/badge/python-3.7%2B-blue)

A modern, cross-platform (Windows, Linux, Android) CLI tool to display and save detailed hardware & system specs for your computer or device—with style!

---

## 🪟🐧 Windows/Linux Features
- 🎨 Stylish CLI Output: ASCII art banner & colorized sections (with `colorama`)
- 🧠 CPU Info: Marketing name, internal code, core count, frequency
- 💾 Memory (RAM): Total & available memory
- 💽 Disk Info: All partitions, sizes, usage
- 🖥️ Operating System: Name, version, machine type
- 🎮 GPU Info: Name, memory, driver (if available)
- 🌐 Network Info: Hostname, IP address
- 📶 WiFi Info: Adapter name, MAC, status (platform-dependent)
- 🟦 Bluetooth Info: Adapter name, MAC, status (platform-dependent)
- 🔋 Battery Info: Percentage, charging status, time left (if available)
- 🏷️ System/Brand Info: Manufacturer, model, serial, BIOS version
- 🧩 Motherboard Info: Vendor, product, serial
- 💾 Export Option: Save the full output (including ASCII banner) to a `.txt` file, with all color codes stripped for readability

---

## 🤖 Android Features
- 🎨 Stylish CLI Output: ASCII art banner
- 📱 Device Info: Brand, model, Android version, security patch, build ID
- 🧠 CPU Info: ABI, supported ABIs, hardware
- 🏷️ Device Identifiers: Device, manufacturer, board, product, fingerprint, IMEI (if accessible)
- 🔋 Battery Info: (if available via getprop)
- 📶 Connectivity: WiFi, mobile data, Bluetooth, Airplane mode, location, hotspot status (where possible)
- 📦 Installed Apps: List all installed app package names
- 💾 Export Option: (add if implemented)
- ⚠️ Note: Some info may require root or special permissions; not all fields are available on all devices

---

## ⚡ Installation

1. **Clone this repository or download the scripts:**
   ```sh
   git clone https://github.com/Pisethz/Specification
   cd yourrepo
   # or just download spec.py, mobilespec.py, and requirements.txt
   ```
2. **Install the required Python packages for desktop usage:**
   ```sh
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```
   - For full GPU info: `pip install gputil`
   - For best WiFi/Bluetooth info on Linux:
     ```sh
     sudo apt install network-manager bluez
     # or
     sudo dnf install NetworkManager bluez
     ```

---

## 🛠️ Usage

### Desktop/PC (Windows, Linux)
Run the script from your terminal:
```sh
python spec.py
```
- View your full system specification in the terminal.
- Choose to save the output to a file if desired.

### 📱 Mobile/Android/Termux
Run the dedicated Android script:
```sh
python mobilespec.py
```
- No extra dependencies required (uses only standard Python and getprop)
- Shows Android device info: brand, model, version, CPU ABI, device, manufacturer, board, and more

#### 📋Example Output (Android)
```
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
============================================================
[ASCII Banner]
[ Android Device Info ]
------------------------------
Brand: samsung
Model: SM-G991B
Android Version: 13
Security Patch: 2023-07-01
Build ID: TP1A.220624.014
CPU ABI: arm64-v8a
Supported ABIs: arm64-v8a,armeabi-v7a,armeabi
Device: o1q
Manufacturer: samsung
Board: o1q
Hardware: qcom
Bootloader: G991BXXU4BULF
Radio Version: G991BXXU4BULF
Fingerprint: samsung/o1q/o1q:13/TP1A.220624.014/G991BXXU4BULF:user/release-keys
Display: TP1A.220624.014
Product: o1q
IMEI: 123456789012345

End of Mobile Specification
```

---

## 📝 Notes
- Some features may require administrator/root privileges (especially on Linux).
- Android/Termux support is limited to what Python and system commands can access.
- The script gracefully handles missing or unsupported information.

---

## 📋 Example Output
```
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
============================================================

[ System/Brand Info ]
----------------------------------------
  Manufacturer: Dell Inc.
  Model: XPS 15 9500
  Serial Number: 1234ABCD5678
  BIOS Version: 1.2.3

[ Motherboard Info ]
----------------------------------------
  Manufacturer: Dell Inc.
  Product: 0N7TVV
  Serial Number: MB123456789

[ CPU Info ]
----------------------------------------
  Marketing Name: Intel(R) Core(TM) i7-10750H CPU @ 2.60GHz
  Internal Code: Intel64 Family 6 Model 165 Stepping 2, GenuineIntel
  Cores (physical): 6
  Cores (total): 12
  Frequency: 2592.00 MHz

[ Memory (RAM) ]
----------------------------------------
  Total: 32.00 GB
  Available: 21.50 GB

[ Disk Info ]
----------------------------------------
  Device: C:\
    Mountpoint: C:\
    File system type: NTFS
    Total Size: 1000.00 GB
    Used: 400.00 GB
    Free: 600.00 GB
    Usage: 40%

[ Operating System Info ]
----------------------------------------
  System: Windows
  Node Name: DELL-XPS
  Release: 10
  Version: 10.0.19044
  Machine: AMD64
  Processor: Intel64 Family 6 Model 165 Stepping 2, GenuineIntel

[ GPU Info ]
----------------------------------------
  GPU: NVIDIA GeForce GTX 1650 Ti
    ID: 0
    Memory Total: 4096MB
    Memory Free: 2048MB
    Memory Used: 2048MB
    Driver: 471.11
    Serial: N/A
    UUID: GPU-FAKE-UUID-1234

[ Network Info ]
----------------------------------------
  Hostname: DELL-XPS
  IP Address: 192.168.0.101

[ WiFi Info ]
----------------------------------------
  Name: Wi-Fi
  Description: Intel(R) Wi-Fi 6 AX201 160MHz
  State: connected
  Physical address: 00:1A:2B:3C:4D:5E
  SSID: HomeNetwork

[ Bluetooth Info ]
----------------------------------------
  Name: Bluetooth Device (Personal Area Network)
  State: connected
  MAC Address: 11:22:33:44:55:66

[ Battery Info ]
----------------------------------------
  Percentage: 95%
  Plugged in: Yes
  Time left: 3h 10m

============================================================
End of Specification

Are you want to save this? (y/n):
```

---

## 📄 License
MIT License

# Specification
🔥⚙️Computer/Device Full Specification CLI Tool This Python script provides a comprehensive, cross-platform (Windows, Linux, and Android) command-line interface to display and optionally save detailed hardware and system specifications for your computer or device.🛠️🔥

