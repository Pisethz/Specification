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

def get_android_info():
    section_header("Android Device Info")
    print(f"Brand: {getprop('ro.product.brand')}")
    print(f"Model: {getprop('ro.product.model')}")
    print(f"Android Version: {getprop('ro.build.version.release')}")
    print(f"CPU ABI: {getprop('ro.product.cpu.abi')}")
    print(f"Device: {getprop('ro.product.device')}")
    print(f"Manufacturer: {getprop('ro.product.manufacturer')}")
    print(f"Board: {getprop('ro.product.board')}")
    print()

def main():
    clear_screen()
    print_banner()
    get_android_info()
    print("=" * 50)
    print("End of Mobile Specification\n")

if __name__ == "__main__":
    main()
