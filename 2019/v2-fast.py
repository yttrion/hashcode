from random import choice
import os


dicoH, dicoV, slides, slides_tags = dict(), dict(), dict(), dict()


def load():
    global nombre, listeV, listeH
    with open("d_pet_pictures.txt", 'r') as f:
        nombre = int(f.readline())
        n = 0
        o, p = 0, 0
        for line in f:
            ligne = line.strip().split()
            if ligne[0] == "H":
                dicoH[o] = [n, ligne[2:]]
                o += 1
            else:
                dicoV[p] = [n, ligne[2:]]
                p += 1
            n += 1


def create_slides():
    global slides_list
    n = 0
    slides_list = []
    for i in range(len(dicoH)):
        slides[n] = dicoH[i]
        slides_tags[n] = slides[n][1]
        slides_list.append(n)
        n += 1

    for i in range(int(len(dicoV)/2)):
        slides[n] = [dicoV[2*i], dicoV[2*i + 1]]
        slides_tags[n] = slides[n][0][1] + slides[n][1][1]
        slides_list.append(n)
        for tag in slides[n][0][1]:
            if tag in slides[n][1][1]:
                slides_tags[n].pop(slides_tags[n].index(tag))
        n += 1


def slides_choice():
    global total_list, scoretot
    total_list = []
    scoretot = 0

    for i in range(nbslides):

        if i == 0:
            slide = choice(slides_list)
            index = slides_list.index(slide)
            slides_list.pop(index)
            precslide = slide
            prectags = set(slides_tags[index])
        else:
            maxi = -1
            for number in slides_list:
                score2 = 0
                tags = set(slides_tags[number])

                score2 = len(tags & prectags)
                score = min(len(prectags) - score2, score2, len(tags) - score2)
                if score > maxi:
                    maxi = score
                    imagemaxi = number
            scoretot += maxi
            slides_list.pop(slides_list.index(imagemaxi))
            precslide = imagemaxi
            prectags = set(slides_tags[imagemaxi])

        total_list.append(precslide)

        #print(str(len(total_list)) + "/" + str(nbslides))
        print(scoretot)


def ecriture():
    with open("slideshow.txt", "w") as f:
        f.write(str(len(total_list)) + "\n")
        for i in total_list:
            if type(slides[i][0]) == int:
                image = str(slides[i][0])
            else:
                image = str(slides[i][0][0]) + " " + str(slides[i][1][0])
            f.write(image + "\n")


def launch():
    global nbslides
    load()
    create_slides()
    temp = len(dicoV)/2 + len(dicoH)
    nbslides = int(temp//1)
    slides_choice()
    ecriture()
    os.system('cls||clear')
    print('Score: ',scoretot)
    '''
    if scoretot<1520:
        launch()
    else :
        print('Score: ',scoretot)
    '''

launch()
