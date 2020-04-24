#include <SparkFunHTU21D.h>

HTU21D humidity;

void setup() {
  Serial.begin(9600); // open serial port, set the baud rate as 9600 bps
  humidity.begin();
}

void loop() {
  String moisture = String(analogRead(0), DEC); //connect sensor to Analog 0
  String humd = String(humidity.readHumidity(), 1);
  String temp = String(humidity.readTemperature(), 1);

  String moisture_msg = String("moisture:" + moisture);
  String humidity_msg = String("humidity:" + humd);
  String temp_msg = String("temp:" + temp);
  
  Serial.println(moisture_msg);
  Serial.println(humidity_msg);
  Serial.println(temp_msg);

  delay(1000);
}
