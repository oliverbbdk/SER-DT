"""Measure contrast for two opaque sRGB hex colors. Python standard library only."""

import argparse
import json
import re
import sys


def luminance(value):
    color = value.removeprefix("#")
    if not re.fullmatch(r"[0-9a-fA-F]{3}|[0-9a-fA-F]{6}", color):
        raise ValueError("Use a 3- or 6-digit hex color, for example #F2EFE6.")
    if len(color) == 3:
        color = "".join(character * 2 for character in color)
    channels = [int(color[index:index + 2], 16) / 255 for index in (0, 2, 4)]
    linear = [channel / 12.92 if channel <= 0.04045 else
              ((channel + 0.055) / 1.055) ** 2.4 for channel in channels]
    return sum(channel * weight for channel, weight in
               zip(linear, (0.2126, 0.7152, 0.0722)))


def contrast_ratio(first, second):
    light, dark = sorted((luminance(first), luminance(second)), reverse=True)
    return (light + 0.05) / (dark + 0.05)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("foreground")
    parser.add_argument("background")
    parser.add_argument("--minimum", type=float, choices=(3.0, 4.5, 7.0), default=4.5)
    args = parser.parse_args()
    try:
        ratio = contrast_ratio(args.foreground, args.background)
    except ValueError as error:
        parser.error(str(error))
    passed = ratio >= args.minimum
    print(json.dumps({"foreground": args.foreground, "background": args.background,
                      "ratio": round(ratio, 3), "minimum": args.minimum,
                      "passes": passed}))
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
