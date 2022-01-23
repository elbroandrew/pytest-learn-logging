from shutil import disk_usage
from texttable import Texttable


def get_disk_stats(path: str) -> dict:

    # TODO определить в Мб или Гб выдавать инфу
    total, used, free = disk_usage(path)
    print('{:.2f}'.format(total / 1024 / 1024 / 1024))
    print(used / 1024 / 1024 / 1024)
    print(free / 1024 / 1024 / 1024)

    return dict(total=total, used=used, free=free)




def main():
    get_disk_stats("C:")


if __name__ == '__main__':
    main()