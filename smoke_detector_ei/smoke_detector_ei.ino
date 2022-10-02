/* Edge Impulse Arduino examples
 * Copyright (c) 2021 EdgeImpulse Inc.
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 * 
 * Modified October 2022 by Nick Bild
 * Smart Smoke Alarm
 * https://github.com/nickbild/smart_smoke_alarm
 */

/* Includes ---------------------------------------------------------------- */
#include <smart_smoke_alarm_inferencing.h>
#include <Adafruit_MLX90640.h>

#define DETECTION_PIN 12

Adafruit_MLX90640 mlx;
float frame[32*24];

float features[768] = {};

/**
 * @brief      Copy raw feature data in out_ptr
 *             Function called by inference library
 *
 * @param[in]  offset   The offset
 * @param[in]  length   The length
 * @param      out_ptr  The out pointer
 *
 * @return     0
 */
int raw_feature_get_data(size_t offset, size_t length, float *out_ptr) {
    memcpy(out_ptr, features + offset, length * sizeof(float));
    return 0;
}


/**
 * @brief      Arduino setup function
 */
void setup()
{
    // put your setup code here, to run once:
    Serial.begin(115200);
    // comment out the below line to cancel the wait for USB connection (needed for native USB)
    // while (!Serial);
    Serial.println("Edge Impulse Inferencing Demo");

    if (!mlx.begin(MLX90640_I2CADDR_DEFAULT, &Wire)) {
      Serial.println("MLX90640 not found!");
    }
  
    mlx.setMode(MLX90640_INTERLEAVED);
    mlx.setResolution(MLX90640_ADC_18BIT);
    mlx.setRefreshRate(MLX90640_8_HZ);
    Wire.setClock(1000000);

    pinMode(DETECTION_PIN, OUTPUT);
    digitalWrite(DETECTION_PIN, LOW);
}

/**
 * @brief      Arduino main function
 */
void loop()
{
    ei_printf("Edge Impulse standalone inferencing (Arduino)\n");

    if (mlx.getFrame(frame) != 0) {
      Serial.println("Failed to capture IR image.");
      return;
    }

    int cnt = 0;
    for (uint8_t h=0; h<24; h++) {
      for (uint8_t w=0; w<32; w++) {
        float t = frame[h*32 + w];
        features[cnt] = t;
        cnt++;
      }
    }

    if (sizeof(features) / sizeof(float) != EI_CLASSIFIER_DSP_INPUT_FRAME_SIZE) {
        ei_printf("The size of your 'features' array is not correct. Expected %lu items, but had %lu\n",
            EI_CLASSIFIER_DSP_INPUT_FRAME_SIZE, sizeof(features) / sizeof(float));
        delay(1000);
        return;
    }

    ei_impulse_result_t result = { 0 };

    // the features are stored into flash, and we don't want to load everything into RAM
    signal_t features_signal;
    features_signal.total_length = sizeof(features) / sizeof(features[0]);
    features_signal.get_data = &raw_feature_get_data;

    // invoke the impulse
    EI_IMPULSE_ERROR res = run_classifier(&features_signal, &result, false /* debug */);
    ei_printf("run_classifier returned: %d\n", res);

    if (res != 0) return;

    // print the predictions
    ei_printf("Predictions ");
    ei_printf("(DSP: %d ms., Classification: %d ms., Anomaly: %d ms.)",
        result.timing.dsp, result.timing.classification, result.timing.anomaly);
    ei_printf(": \n");
    ei_printf("[");
    for (size_t ix = 0; ix < EI_CLASSIFIER_LABEL_COUNT; ix++) {
        ei_printf("%.5f", result.classification[ix].value);
#if EI_CLASSIFIER_HAS_ANOMALY == 1
        ei_printf(", ");
#else
        if (ix != EI_CLASSIFIER_LABEL_COUNT - 1) {
            ei_printf(", ");
        }
#endif
    }
#if EI_CLASSIFIER_HAS_ANOMALY == 1
    ei_printf("%.3f", result.anomaly);
#endif
    ei_printf("]\n");

    // human-readable predictions
    String pred = "";
    for (size_t ix = 0; ix < EI_CLASSIFIER_LABEL_COUNT; ix++) {
        // ei_printf("    %s: %.5f\n", result.classification[ix].label, result.classification[ix].value);
        // Serial.println("   " + String(result.classification[ix].label) + ": " + String(result.classification[ix].value, 5) );
        if (result.classification[ix].value > 0.6) {
          pred = result.classification[ix].label;
        }
    }
    
    // Serial.print("Prediction: ");
    // Serial.println(pred);
    if (pred == "person") {
      // A person has been detected.
      Serial.println("**** PERSON DETECTED ****");
      digitalWrite(DETECTION_PIN, HIGH);
      delay(1500);
      digitalWrite(DETECTION_PIN, LOW);
      delay(30000);
    }
    
#if EI_CLASSIFIER_HAS_ANOMALY == 1
    ei_printf("    anomaly score: %.3f\n", result.anomaly);
#endif

    delay(1000);
}
