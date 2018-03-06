#!/usr/bin/env python

import argparse
import datetime
import sys
import taglightswitch

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--targettime", type=str, help="time against which ranges will be compared to advise or correct instance power states, e.g. 14:05:00")
    parser.add_argument("-a", "--action", type=str, help="action: advise or correct. default=advise")

    args = parser.parse_args()

    if args.targettime:
        from dateutil import parser
        target_time = parser.parse(args.targettime).time()
    else:
        target_time = datetime.datetime.now().time()

    lightswitcher = taglightswitch.TagLightSwitch(target_time)

    if args.action == 'correct':
        lightswitcher.correct()
    else:
        lightswitcher.advise()


if __name__ == '__main__':
    sys.exit(main())
