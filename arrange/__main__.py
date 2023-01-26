import click
import sys
from arrange.app import create_dir_mov_files


@click.group()
@click.version_option("1.0.0")

def main():
    """
    A file-arranging CLI Application
    """
    pass

@main.command()
def arrange():
    """
    Operation: Arranges files by putting them into a folder based on their
                creation/last-modified date 
    """
    create_dir_mov_files()


if __name__ == "__main__":
    args = sys.args
    if "--help" in args:
        print("CVE")
    main()

