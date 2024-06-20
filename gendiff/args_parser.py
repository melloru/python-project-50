import argparse


def arg_pars():
    parser = argparse.ArgumentParser(
        description="Compares two configuration "
                    "files and shows a difference."
    )
    parser.add_argument('first_file', type=str,
                        help='First file to compare'
                        )
    parser.add_argument('second_file', type=str,
                        help='Second file to compare'
                        )
    parser.add_argument('-f', '--format', type=str, default='stylish',
                        help='Output format (default: "stylish")')

    args = parser.parse_args()

    return args.first_file, args.second_file, args.format
