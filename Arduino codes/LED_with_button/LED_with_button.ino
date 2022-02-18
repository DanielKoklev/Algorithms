int buttonCurrent = LOW;
int buttonPrevious = LOW;
int buttonState = LOW;

void setup() {
pinMode(7,INPUT_PULLUP);
pinMode(10,OUTPUT);

}

void loop() {

button();
buttonPrevious = buttonCurrent;

digitalWrite(10,buttonState);

}

boolean button(){

buttonCurrent = digitalRead (7);

if(buttonCurrent == HIGH && buttonPrevious == LOW){
  
  
  if(buttonState == HIGH){
  
  buttonState = LOW;
  return buttonState;
  
  }
  else{ 

  buttonState = HIGH;
  return buttonState;
 
  }
