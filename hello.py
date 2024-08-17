import argparse

def parse_args(arg_str: str | None = ""):
    parser = argparse.ArgumentParser()
    parser.add_argument('-g', '--greeting', type=str, default='Hello')
    parser.add_argument('-n', '--name', type=str, default='World')
    arg_list = None if arg_str is None else arg_str.split()
    return parser.parse_args(arg_list)

# API
def full_output(arg_str: str | None = ""):
    args = parse_args(arg_str)
    return f"{args.greeting}, {args.name}!"

# application
def main(arg_str: str | None = ""):
    output = full_output(arg_str)
    print(output)

if __name__ == '__main__':
    main(None)
