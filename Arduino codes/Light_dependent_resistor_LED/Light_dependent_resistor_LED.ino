int LedPin = 3;
int resistancePin = A0;
int value;

void setup() {

pinMode(LedPin,OUTPUT);

}

void loop() {

  value = analogRead(resistancePin);


  if(value > 600){
  
    digitalWrite(LedPin,LOW);
  
  }
  else {
    
    digitalWrite(LedPin,HIGH);
    
  }


  
}
