#include <ArduinoBLE.h>
#include <Arduino_LSM6DS3.h>

BLEService motionService("180C"); // Custom BLE Service

// Characteristics for Timestamp & Acceleration Data (X, Y, Z)
BLEUnsignedLongCharacteristic timestampChar("2A60", BLERead | BLENotify);
BLEFloatCharacteristic accXChar("2A57", BLERead | BLENotify);
BLEFloatCharacteristic accYChar("2A58", BLERead | BLENotify);
BLEFloatCharacteristic accZChar("2A59", BLERead | BLENotify);

// New characteristic to send packet ID
BLEUnsignedLongCharacteristic packetIDChar("2A61", BLERead | BLENotify);

const int duration = 50000; // 45 seconds
const int samplingRate = 10; // 150Hz ≈ every 10 ms
unsigned long startTime;
unsigned long packetCounter = 0;

void setup() {
  Serial.begin(9600);
  if (!IMU.begin()) {
    Serial.println("Failed to initialize IMU!");
    while (1);
  }

  if (!BLE.begin()) {
    Serial.println("Failed to initialize BLE!");
    while (1);
  }

  BLE.setLocalName("Nano33IoT_Motion");
  BLE.setAdvertisedService(motionService);

  // Add Characteristics to the BLE Service
  motionService.addCharacteristic(timestampChar);
  motionService.addCharacteristic(accXChar);
  motionService.addCharacteristic(accYChar);
  motionService.addCharacteristic(accZChar);
  motionService.addCharacteristic(packetIDChar); // Add new packet ID characteristic

  BLE.addService(motionService);
  BLE.advertise();
  Serial.println("Bluetooth device active, waiting for connections...");
  startTime = millis();
}

void loop() {
  BLEDevice central = BLE.central();

  if (central) {
    Serial.print("Connected to central: ");
    Serial.println(central.address());

    while (central.connected()) {
      if (millis() - startTime >= duration) {
        Serial.println("Data collection completed.");
        break;
      }

      float x, y, z;
      if (IMU.accelerationAvailable()) {
        IMU.readAcceleration(x, y, z);
        unsigned long currentTimestamp = millis() - startTime;

        // Send values over BLE
        packetIDChar.writeValue(packetCounter);
        timestampChar.writeValue(currentTimestamp);
        accXChar.writeValue(x);
        accYChar.writeValue(y);
        accZChar.writeValue(z);

        // Serial print (CSV-friendly format)
        Serial.print("Packet: ");
        Serial.print(packetCounter);
        Serial.print(", Timestamp: ");
        Serial.print(currentTimestamp);
        Serial.print(" ms, X: ");
        Serial.print(x, 6);
        Serial.print(", Y: ");
        Serial.print(y, 6);
        Serial.print(", Z: ");
        Serial.println(z, 6);

        packetCounter++;
        delay(samplingRate);
      }
    }

    Serial.println("Disconnected from central.");
  }
}
