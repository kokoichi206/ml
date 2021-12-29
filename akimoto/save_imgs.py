import get_names
import google_img_search

def main():
    IMG_NUM = 100

    names = get_names.saka()
    offset = 0
    print(names)
    for name in names:
        print(name)
        google_img_search.scrapingImages(name, "saka", IMG_NUM, offset=offset)
        offset += IMG_NUM

    names = get_names.akb()
    offset = 0
    for name in names:
        print(name)
        google_img_search.scrapingImages(name, "akb", IMG_NUM, offset=offset)
        offset += IMG_NUM

if __name__ == '__main__':
    main()
