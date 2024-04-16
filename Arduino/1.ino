int LED1 = 10;
int LED2 = 8;

void setup() {
   pinMode (LED1, OUTPUT);
   pinMode (LED2, OUTPUT);
}

void loop() {
  digitalWrite(LED1, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(100);                       // wait for a second
  digitalWrite(LED1, LOW);    // turn the LED off by making the voltage LOW
  delay(100); 

  digitalWrite(LED2, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(100);                       // wait for a second
  digitalWrite(LED2, LOW);    // turn the LED off by making the voltage LOW
  delay(100); 
}
