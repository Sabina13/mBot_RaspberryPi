String data="Hello From Arduino!";
 
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(13,OUTPUT);
}
 
void loop() {
  // put your main code here, to run repeatedly:
  if (analogRead(7)<100)
  {
    Serial.println(data);
  }
  else{
    Serial.println("off");
  }
  delay(50);
}
