import asyncio
from bleak import BleakClient, BleakScanner
import csv
import struct

DEVICE_NAME = "Nano33IoT_Motion"
CHAR_TIMESTAMP = "2A60"
CHAR_ACC_X = "2A57"
CHAR_ACC_Y = "2A58"
CHAR_ACC_Z = "2A59"
OUTPUT_FILE = "chest_motion_data_ble_timer_02(heavy_no_duration).csv"

data = []
latest_timestamp = None
latest_values = {"x": None, "y": None, "z": None}
start_time = None  # Track the first timestamp to normalize time

def handle_timestamp(_, value):
    global latest_timestamp, start_time
    latest_timestamp = int.from_bytes(value, byteorder='little', signed=False)

    # Set the first timestamp as the reference time
    if start_time is None:
        start_time = latest_timestamp

def handle_acc_x(_, value):
    x = struct.unpack('<f', value)[0]
    latest_values["x"] = x
    record_if_complete()

def handle_acc_y(_, value):
    y = struct.unpack('<f', value)[0]
    latest_values["y"] = y
    record_if_complete()

def handle_acc_z(_, value):
    z = struct.unpack('<f', value)[0]
    latest_values["z"] = z
    record_if_complete()

def record_if_complete():
    global latest_timestamp, start_time
    if None not in latest_values.values() and latest_timestamp is not None:
        if start_time is None:
            start_time = latest_timestamp  # Set first timestamp as reference
        
        # Normalize timestamp to start at 0 ms
        normalized_timestamp = max((latest_timestamp - start_time), 0)

        data.append([
            latest_timestamp,  # Original timestamp (for reference)
            latest_values["x"],
            latest_values["y"],
            latest_values["z"],
            normalized_timestamp / 1000  # Convert to seconds (0 to ~30 sec)
        ])

        # Clear buffers for next set
        latest_values["x"] = None
        latest_values["y"] = None
        latest_values["z"] = None
        latest_timestamp = None

async def run():
    device = await BleakScanner.find_device_by_name(DEVICE_NAME)
    if not device:

        print("Nano 33 IoT not found. Is it advertising?")
        return

    async with BleakClient(device) as client:
        print(f"Connected to {DEVICE_NAME}")

        await client.start_notify(CHAR_TIMESTAMP, handle_timestamp)
        await client.start_notify(CHAR_ACC_X, handle_acc_x)
        await client.start_notify(CHAR_ACC_Y, handle_acc_y)
        await client.start_notify(CHAR_ACC_Z, handle_acc_z)

        await asyncio.sleep(50)  # Collect data for 30s

        await client.stop_notify(CHAR_TIMESTAMP)
        await client.stop_notify(CHAR_ACC_X)
        await client.stop_notify(CHAR_ACC_Y)
        await client.stop_notify(CHAR_ACC_Z)

    # Save data to CSV
    if data:  # Prevent empty file issue
        with open(OUTPUT_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Timestamp_ms", "AccX", "AccY", "AccZ", "Timestamp_sec"])
            writer.writerows(data)

        print(f"Data saved to {OUTPUT_FILE}")
    else:
        print("⚠️ No data was collected!")

asyncio.run(run())
