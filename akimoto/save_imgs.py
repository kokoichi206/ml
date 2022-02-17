import get_names
import google_img_search
import os

def main():
    IMG_NUM = 200

    # GET all names for saka
    names = get_names.saka()
    offset = 0
    print(names)
    for name in names:
        print(name)
        os.makedirs(f"saka/{name}", exist_ok=True)
        google_img_search.scrapingImages(name, f"saka/{name}", IMG_NUM, offset=offset)
        offset += IMG_NUM

    # GET all names for akb
    names = get_names.akb()
    offset = 0
    for name in names:
        print(name)
        os.makedirs(f"akb/{name}", exist_ok=True)
        google_img_search.scrapingImages(name, f"akb/{name}", IMG_NUM, offset=offset)
        offset += IMG_NUM

if __name__ == '__main__':
    main()
