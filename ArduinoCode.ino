#include <Mouse.h>

void setup() {
  Serial.begin(9600);
  Mouse.begin();
}

void loop() {
  
  if (Serial.available()) {

    String input = Serial.readStringUntil('\n');
    if (input == "FIRE") {
      Mouse.press(MOUSE_LEFT);
      Mouse.release(MOUSE_LEFT);
    } 

  }
  
}
