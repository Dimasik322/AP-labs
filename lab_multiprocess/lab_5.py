from multiprocessing import Pool
from time import sleep
import requests

def load_image(url):
    p = requests.get(url)
    out = open(f'lab_multiprocess/img.jpg', "wb")
    out.write(p.content)
    out.close()

def main():
    URLs = input("Введите URL-адреса через пробел:").split(' ')
    with Pool(10) as p:
        for image in p.map(load_image, URLs):
            print('картинка сохранилась')

if __name__ == '__main__':
    main()
