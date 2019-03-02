from random import choice, randint

dicoH, dicoV, slides = dict(), dict(), dict()

def load():
    global nombre, listeV, listeH
    with open("b_lovely_landscapes.txt", 'r') as f:
        nombre = int(f.readline())
        n = 0
        o,p = 0,0
        for line in f:
            ligne = line.strip().split()
            if ligne[0] == "H":
                dicoH[o] = [n, ligne[0], ligne[1], ligne[2:]]
                o += 1
            else:
                dicoV[p] = [n, ligne[0], ligne[1], ligne[2:]]
                p += 1
            n += 1 
def create_slides ():
    global slides_list
    n = 0
    for i in range(len(dicoH)):
        slides[n] = dicoH[i]
        n += 1
    for i in range(int(len(dicoV)/2)):
        slides[n] = [dicoV[2*i], dicoV[2*i + 1]]
        n += 1
    slides_list = []
    for i in range(len(dicoH) + int(len(dicoV)/2)):
        slides_list.append(i)
def slides_choice():
    global total_list
    total_list = []
    for i in range(nbslides):
        if i == 0:
            slide = choice(slides_list)
            index = slides_list.index(slide)
            slides_list.pop(index)
            precslide = slide
            if len(slides[index]) != 2:
                prectags = slides[index][3]
            else :
                prectags = slides[index][0][3] + slides[index][1][3]
        else:
            maxi = -1
            imagemaxi = 0
            for number in slides_list:
                score2 = 0 
                score3 = 0
                if len(slides[number]) != 2:
                    tags = slides[number][3]
                else :
                    tags = slides[number][0][3] + slides[number][1][3]
                    
                for tag in tags:
                    if tag in prectags:
                        score2 += 1
                    else:
                        score3 +=1
                score1 = len(prectags) - score2
                score = min(score1, score2, score3)
                if score > 90:
                    maxi = score
                    imagemaxi = number
                    break
            if score <= 90:
                imagemaxi = choice(slides_list)
            with open("slideshow.txt","a") as f:
                    if len(slides[imagemaxi]) != 2:
                        image = str(slides[imagemaxi][0])
                    else :
                        image = str(slides[imagemaxi][0][0]) + " " + str(slides[imagemaxi][1][0])
                    f.write(image + "\n")
            
            slide = imagemaxi
            index = slides_list.index(slide)
            slides_list.pop(index)
            precslide = slide
            if len(slides[imagemaxi]) != 2:
                prectags = slides[imagemaxi][3]
            else :
                prectags = slides[imagemaxi][0][3] + slides[imagemaxi][1][3]
        total_list.append(precslide)
        print (str(len(total_list)) + "/" + str(nbslides))
def ecriture():
    with open("slideshow.txt","w") as f:
        f.write(str(len(total_list)) + "\n")
        for i in total_list:
            if len(slides[i]) != 2:
                image = str(slides[i][0])
            else :
                image = str(slides[i][0][0]) + " " + str(slides[i][1][0])
            f.write(image + "\n")
load()
create_slides()
nbslides = int(len(dicoV)/2 + len(dicoH)) // 1
slides_choice()

with open("slideshow.txt","w") as f:
        f.write(str(len(total_list)) + "\n")
        
ecriture()
