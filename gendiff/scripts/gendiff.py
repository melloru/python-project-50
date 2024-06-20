from gendiff import generate_diff
from gendiff import args_parser


def main():
    file_path1, file_path2, format = args_parser.arg_pars()
    print(generate_diff(file_path1, file_path2, format))


if __name__ == '__main__':
    main()
