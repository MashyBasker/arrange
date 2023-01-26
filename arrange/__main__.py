import sys 
import click
from arrange.app import create_dir_mov_files


@click.group()
@click.version_option("1.0.0")

def main():
    """
    A file-arranging CLI Application
    """
    print("Hey friend")
    pass

@main.command()
@click.argument('keyword', required=False)
def arrange(**kwargs):
    """
    Operation: Arranges files by putting them into a folder based on their
                creation/last-modified date 
    """
    create_dir_mov_files()


if __name__ == "__main__":
    args = sys.argv 
    if "--help" in args:
        print("Arrange")
        main() 
    elif len(args) == 1:
        arrange()
