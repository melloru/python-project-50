from gendiff import generate_diff
from gendiff import args_parser


def main():
    file_path1, file_path2 = args_parser.arg_pars()

    print(generate_diff(file_path1, file_path2))


if __name__ == '__main__':
    main()
