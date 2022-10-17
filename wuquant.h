#pragma once

#include <stdbool.h>

#ifdef __cplusplus
extern "C" {
#endif

/**
 * Given a 24bit (8bpc) image, outputs a quantized list of colors.
 *
 * `targetColors` can be at most 256.
 *
 * The caller should allocate `outputPalette` (`targetColors * 3` bytes),
 * and is responsible for freeing `imageData` and `outputPalette`.
 *
 * Returns true on success, false on failure (malloc failed).
 */
bool wuquant(const unsigned char *imageData, unsigned int pixelCount, unsigned int targetColors, unsigned char *outputPalette);

#ifdef __cplusplus
}
#endif
