int led_pin = 8;
int sw_pin = 10;
int sw_state;

void setup() {
   pinMode (led_pin, OUTPUT);
   pinMode (sw_pin, INPUT);
}

void loop() {
  sw_state = digitalRead(sw_pin);
  if(sw_state == 1){
    digitalWrite(led_pin, HIGH);
  }
  else{
    digitalWrite(led_pin, LOW);
  }
}
