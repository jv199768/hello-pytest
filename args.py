import sys
import argparse


def parse_args(arg_str: str | None = ""):
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--count', type=int, default=0)
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('-o', '--out', type=str, default='out.txt')
    arg_list = None if arg_str is None else arg_str.split()
    args = parser.parse_args(arg_list)

    print(f'in parse_args({arg_str=})')
    print(f'   {arg_list=}')
    print(f'   {args=}\n')
    print(f'   {args.count=}\n')
    print(f'   {args.verbose=}\n')
    print(f'   {args.out=}\n')
    return args


def main():
    print(f'\n{sys.argv=}\n')

    parse_args(None)  # for normal CLI use
    parse_args("-c 2 -v --out foo.py")  # to test args
    parse_args("")  # to test no args


if __name__ == '__main__':
    main()