int trig_pin = 2,echo_pin = 3,buzzer_pin = 10,time,distance;
void setup()
{
  Serial.begin(9600);
  pinMode (trig_pin, OUTPUT);
  pinMode (echo_pin, INPUT);
  pinMode (buzzer_pin, OUTPUT);
}
void loop()
{
  digitalWrite (trig_pin, HIGH);
  delayMicroseconds (10);
  digitalWrite (trig_pin, LOW);
  time = pulseIn (echo_pin, HIGH);
  distance = (time * 0.034)/2;
  
  if (distance <= 10)
  {
    Serial.println ("Door Open");
    Serial.print ("Distance=");
    Serial.println (distance);
    digitalWrite (buzzer_pin, HIGH);
    delay (500);
  }
  else
  {
    Serial.println ("Door Closed");
    Serial.print ("Distance=");
    Serial.println (distance);
    digitalWrite (buzzer_pin, LOW);
    delay (500);
  }
}