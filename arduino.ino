//keycodes for 1, 2, 3, 4

#define KEY_NUMBERS 4

int keydown[KEY_NUMBERS] = {49, 50, 51, 52};
int keyup[KEY_NUMBERS] = {149, 150, 151, 152};

void setup() {
Serial.begin(9600);
}
  
void loop() {
  int rand1 = random(KEY_NUMBERS);
  int rand2 = random(KEY_NUMBERS);
  
  int randKeydown = keydown[rand1];
  int randKeyup = keyup[rand2];

  Serial.println(randKeydown);
  delay(5000);
  Serial.println(randKeyup);
  delay(5000);
}
