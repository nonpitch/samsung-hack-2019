int var_pin = 0;
int var = 0;
int led_pin = 5;

void setup() {
   Serial.begin(9600);
}

void loop() {
  var = analogRead(var_pin);
  var = map(var, 30, 700, 0, 1023);
  Serial.println(var);
  analogWrite(led_pin,var/4); 
}
