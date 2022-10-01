#include <Adafruit_MLX90640.h>

Adafruit_MLX90640 mlx;
float frame[32*24];

void setup() {
  Serial.begin(115200);
  while (!Serial);

  if (!mlx.begin(MLX90640_I2CADDR_DEFAULT, &Wire)) {
    Serial.println("MLX90640 not found!");
  }

  mlx.setMode(MLX90640_INTERLEAVED);
  mlx.setResolution(MLX90640_ADC_18BIT);
  mlx.setRefreshRate(MLX90640_8_HZ);
  Wire.setClock(1000000);
}

void loop() {
  if (mlx.getFrame(frame) != 0) {
    Serial.println("Failed to capture IR image.");
    return;
  }

  Serial.println("-- Image start --");
  for (uint8_t h=0; h<24; h++) {
    for (uint8_t w=0; w<32; w++) {
      float t = frame[h*32 + w];
      Serial.print(t, 1); Serial.print(",");
    }
    Serial.println("");
  }
  
  delay(1000);

}
