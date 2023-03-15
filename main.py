from get_links import get_links
from extract_data import extract_data
from transform_data import transform_data
from load_data import load_data


def main():
    get_links()
    extract_data()
    transform_data()
    load_data()


main()