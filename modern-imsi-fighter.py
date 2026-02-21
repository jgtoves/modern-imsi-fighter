import subprocess
import json
import time
from datetime import datetime

# --- Configuration ---
# Set your "Nominal" home network (e.g., 'IT&E' or 'Docomo Pacific')
HOME_NETWORK = "671" # Example Mobile Country Code for USA/Guam areas

def get_telephony_data():
    try:
        # Pulls current network type and signal info
        res = subprocess.check_output(['termux-telephony-device-id'])
        return json.loads(res)
    except:
        return None

print("--- DOWNGRADE ANALYSIS ACTIVE ---")
print("[*] Monitoring for 5G/4G -> 3G Forced Flips...")

last_state = None

try:
    while True:
        data = get_telephony_data()
        if data:
            current_type = data.get('network_type', 'UNKNOWN')
            data_state = data.get('data_state', 'DISCONNECTED')
            
            # 1. Detection: Forced Downgrade to 3G/HSPA
            # In 2026, 3G is largely 'dead'—seeing it appear out of nowhere is a major red flag.
            if "HSPA" in current_type or "UMTS" in current_type:
                print(f"\n[!!!] CRITICAL: FORCED 3G DOWNGRADE [!!!]")
                print(f"TIME: {datetime.now().strftime('%H:%M:%S')}")
                print(f"PROTOCOL: {current_type}")
                print(f"ALERT: Possible 4G/5G Jamming in progress.")

            # 2. Detection: Rapid Fluctuation (The 'Hunting' Phase)
            if last_state and current_type != last_state:
                print(f"[*] Signal Shift: {last_state} -> {current_type}")
            
            last_state = current_type

        time.sleep(1) # High-frequency polling to catch the 'Jolt'

except KeyboardInterrupt:
    print("\n[!] Service Offline.")
