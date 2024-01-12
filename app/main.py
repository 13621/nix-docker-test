import argparse
import sys
import os
from pathlib import Path
import yaml


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', '--key')
    parser.add_argument('-c', '--config')
    parser.add_argument('-e', '--env')
    args = parser.parse_args()

    d = yaml.safe_load(Path(args.config).open('r'))
    print(d[args.key])

    if args.env:
        print(os.environ.get(args.env))

    sys.exit(0)


if __name__ == '__main__':
    main()
