//DS3231 / RTC
#include <Wire.h>
#include <DS3231.h>
DS3231 clock;
RTCDateTime dt;

// TEMP
#include <DHT.h>
#define DHTPIN 2
#define DHTTYPE DHT22
DHT dht(DHTPIN, DHTTYPE);
float temperature;

// GY-61
const int xPin = A0;
const int yPin = A1;
const int zPin = A2;
int xOffset = 0;
int yOffset = 0;
int zOffset = 0;

// GPS
#include <TinyGPS++.h>
TinyGPSPlus gps;
float GPSLat;
float GPSLon;
float GPSAlt;
uint8_t GPSSats;
uint32_t startGetFixmS;
uint32_t endFixmS;
bool GPSfixUpdated;

//Til Raspberry PI
String datastring = "";
String time = "";

void setup()
{
  // RTC
  clock.begin();
  // Disable this after setting the time once
  //clock.setDateTime(__DATE__, __TIME__);
 //Communication with Raspberry PI
  Serial2.begin(115200);
  //GPS
  Serial1.begin(9600);

  //SERIAL
  Serial.begin(9600);
  Serial.println();

  //DHT
  dht.begin();

  // GY-61
  // Kalibrér sensoren
  Serial.println("Kalibrerer... Hold sensoren stille.");
  delay(2000); // Vent to sekunder, mens sensoren holdes stille

  // Tag gennemsnitlige målinger for at finde offset
  xOffset = analogRead(xPin);
  yOffset = analogRead(yPin);
  zOffset = analogRead(zPin);
  Serial.print("Offsets: X="); Serial.print(xOffset);
  Serial.print(" Y="); Serial.print(yOffset);
  Serial.print(" Z="); Serial.println(zOffset);

  //GPS millis
  startGetFixmS = millis();
}

void loop()
{
  GPSfixUpdated = false;

  if (gpsWaitFix(5000))                            //read the GPS for up to 2000mS for an updated location
  {
    GPSfixUpdated = true;
    GPSLat = gps.location.lat();
    GPSLon = gps.location.lng();
    GPSAlt = gps.altitude.meters();
    GPSSats = gps.satellites.value();
      Serial.println("");
        Serial.println("");
          Serial.println("");
            Serial.println("");
              Serial.println("");

    Serial.print("Latitude= ");
    Serial.println(GPSLat, 6);
    Serial.print("Longtitude= ");
    Serial.println(GPSLon, 6);
    Serial.println();
    startGetFixmS = millis();    //have a fix, next thing that happens is checking for a fix, so restart timer
  }
  else
  {
    Serial.println();
          Serial.println("");
        Serial.println("");
          Serial.println("");
            Serial.println("");
              Serial.println("");
    Serial.println(F("Timeout - No GPS Fix "));
    GPSfixUpdated = true;
  }

  if (GPSfixUpdated)
  {
// DS3231 / RTC
dt = clock.getDateTime();
  Serial.print("Reading at: ");
  Serial.print(dt.year);   Serial.print("-");
  // print month
  Serial.print(dt.month);   Serial.print("-");
  // print day
  Serial.print(dt.day);   Serial.print(" ");
  // print hour
  Serial.print(dt.hour);    Serial.print(":");
  // print minute
  Serial.print(dt.minute);    Serial.print(":");
  // print second
  Serial.print(dt.second);
  Serial.println();
      Serial.println("");
  time = dt.year; time += "-";
  time += dt.month; time += "-";
  time += dt.day; time += " ";
  time += dt.hour; time += ":";
  time += dt.minute; time += ":";
  time += dt.second;
// DHT    
  temperature = dht.readTemperature();
  Serial.print("Temperature: ");
  Serial.print(temperature);
  Serial.println();

// GY-61
// Læs analoge værdier fra GY-61
  int xValue = analogRead(xPin) - xOffset;
  int yValue = analogRead(yPin) - yOffset;
  int zValue = analogRead(zPin) - zOffset;

// Fjern små udsving (støj)
  if (abs(xValue) < 5) xValue = 0;
  if (abs(yValue) < 5) yValue = 0;
  if (abs(zValue) < 5) zValue = 0;

// Debugging i Serial Monitor
  Serial.println("Gyro data: ");
  Serial.print(" X: "); Serial.println(xValue);
  Serial.print(" Y: "); Serial.println(yValue);
  Serial.print(" Z: "); Serial.println(zValue);
    datastring = temperature;
    datastring += ";";
    datastring += GPSLat;
    datastring += ";";
    datastring += GPSLon;
    datastring += ";";
    datastring += time;
    datastring += ";";
    datastring += xValue;
    datastring += ";";
    datastring += yValue;
    datastring += ";";
    datastring += zValue;
    Serial2.print(datastring);
    Serial.println("TEST STRING:");
    Serial.print(datastring);
    delay(5000);
  }
}


bool gpsWaitFix(uint32_t waitFixmS)
{
  //waits a specified number of milli seconds for a fix, returns true for updated fix

  uint32_t startmS, waitmS;
  uint8_t GPSchar;

  startmS = millis();

  while ( (uint32_t) (millis() - startmS) < waitFixmS)       //allows for millis() overflow
  {
    if (Serial1.available() > 0)
    {
      GPSchar = Serial1.read();
      gps.encode(GPSchar);
    }

    if (gps.speed.isUpdated() && gps.satellites.isUpdated()) //ensures that GGA and RMC sentences have been received
    {
      endFixmS = millis();                                //record the time when we got a GPS fix
      return true;
    }
  }
  return false;                                           //there was no fix
}
