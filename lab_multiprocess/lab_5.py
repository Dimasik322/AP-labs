from multiprocessing import Pool
import time
import requests

count_of_image = 0

def load_image(url):
    p = requests.get(url)
    global count_of_image
    out = open(f'lab_multiprocess/img_{count_of_image}.jpg', "wb")
    out.write(p.content)
    out.close()
    count_of_image +=1

def main():
    URLs = input("Введите URL-адреса через пробел:").split(' ')
    #for i in URLs:
     #   print(i, '\n')
    with Pool(10) as p:
        for image in map(load_image, URLs):
            print('картинка сохранилась')

if __name__ == '__main__':
    main()

#картинки в папке были сохранены по адресам: https://opis-cdn.tinkoffjournal.ru/mercury/main___kittens.0a8iazlzhvsg.jpg https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR29sVz45xOw54cDsJq25kB89JCUtFFzY5MXWLbPAqn1_xH81_bOHUwJW2p42ZdjQqaOhk&usqp=CAU https://chudo-prirody.com/uploads/posts/2021-08/thumbs/1628886836_82-p-mnogo-kotyat-foto-87.png https://gala-cat.ru/_nw/1/38721395.jpg