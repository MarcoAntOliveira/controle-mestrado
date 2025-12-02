    #include <Arduino.h>

// Pinos do ESP8266
#define IN1 14  // D5
#define IN2 12  // D6
#define ENA 13  // D7 (PWM)

// Velocidade (0 a 1023 no ESP8266)
int speedValue = 800;

void forward() {
    digitalWrite(IN1, HIGH);
    digitalWrite(IN2, LOW);
    analogWrite(ENA, speedValue);
}

void backward() {
    digitalWrite(IN1, LOW);
    digitalWrite(IN2, HIGH);
    analogWrite(ENA, speedValue);
}

void stopMotor() {
    analogWrite(ENA, 0);
    digitalWrite(IN1, LOW);
    digitalWrite(IN2, LOW);
}

void setup() {
    Serial.begin(115200);

    pinMode(IN1, OUTPUT);
    pinMode(IN2, OUTPUT);
    pinMode(ENA, OUTPUT);

    Serial.println("Motor DC + L298N + ESP8266");
}

void loop() {
    Serial.println("Frente");
    forward();
    delay(3000);

    Serial.println("Parado");
    stopMotor();
    delay(2000);

    Serial.println("Re");
    backward();
    delay(3000);

    Serial.println("Parado");
    stopMotor();
    delay(2000);
}