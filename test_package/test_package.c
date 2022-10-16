#include <stdio.h>
#include <stdlib.h>
#include <wuquant.h>

int main()
{
	FILE *fp = fopen("../../Badger.rgb", "rb");
	if (!fp)
	{
		fprintf(stderr, "error: couldn't open test image.\n");
		return 1;
	}
	unsigned int pixelCount = 256 * 342;
	unsigned char *imageData = malloc(pixelCount * 3);
	fread(imageData, 3, pixelCount, fp);

	int targetColors = 16;
	unsigned char palette[targetColors * 3];
	wuquant(imageData, pixelCount, targetColors, palette);

	if (palette[0] == 22 && palette[1] == 16 && palette[2] == 13)
		return 0;

	fprintf(stderr, "error: unexpected palette results:\n");
	for (int k = 0; k < targetColors; ++k)
		fprintf(stderr, "%3u %3u %3u\n", palette[k * 3 + 0], palette[k * 3 + 1], palette[k * 3 + 2]);

	return 0;
}
