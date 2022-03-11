#include <Servo.h>
Servo lBrow;
Servo rBrow;
Servo lMouth;
Servo rMouth;

int mood;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  Serial.setTimeout(1);
  lBrow.attach(3);
  rBrow.attach(5);
  lMouth.attach(6);
  rMouth.attach(9);

}

void loop() {
  while (!Serial.available());
  mood = Serial.readString().toInt();
  lBrow.write(60 + mood * 0.8);
  rBrow.write(120 - mood * 0.8);
  lMouth.write(140 - mood);
  rMouth.write(40 + mood);
  Serial.println(mood);
}
