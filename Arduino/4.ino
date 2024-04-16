int var_pin=0;
int var=0;
int led_pin=5;

void setup() {
  Serial.begin(9600);
}

void loop() {
  var = analogRead(var_pin);
  float voltage = var * 5.0;
  voltage /= 1024.0;      
  float temperatureC = (voltage - 0.5) * 100; 
  Serial.println(temperatureC);

}
