from constants import COLOR_THRESHOLDS

class ColorDetector:
    def detect(self, r, g, b):
        for name, cond in COLOR_THRESHOLDS.items():
            if cond(r, g, b):
                return name
        return "linetrace mode"