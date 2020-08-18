from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
from random import randint, choice
from twitter import api

names = ['chitãozinhoo',
    'miguel ángel', 
    'quetzalcoatl', 
    'xochiquetzal', 
    'munkhtsetseg', 
    'chalchihuitl', 
    'iztaccíhuatl', 
    'purificación', 
    'tonalpouhque', 
    'kan imix che', 
    'purushottama',
    'sibonakaliso']

Thumbs = ['thumbs/Img1.jpg', 'thumbs/Img2.jpg', 'thumbs/Img3.jpg', 'thumbs/Img4.jpeg', 'thumbs/Img5.jpeg', 'thumbs/Img6.jpeg', 'thumbs/Img7.jpeg', 'thumbs/Img8.jpeg', 'thumbs/Img9.jpeg', 'thumbs/Img10.jpeg', 'thumbs/Img11.jpg', 'thumbs/Img12.jpeg', 'thumbs/Img13.jpeg', 'thumbs/Img14.jpeg', 'thumbs/Img15.jpeg', 'thumbs/Img16.jpeg', 'thumbs/Img17.jpeg', 'thumbs/Img18.jpeg', 'thumbs/Img19.jpeg', 'thumbs\Img19.jpeg', 'thumbs\Img20.jpeg', 'thumbs\Img21.jpg', 'thumbs\Img22.jpeg', 'thumbs\Img23.jpg', 'thumbs\Img24.jpg', 'thumbs\Img25.jpg', 'thumbs\Img26.jpg', 'thumbs\Img27.jpg', 'thumbs\Img28.jpg', 'thumbs\Img29.jpg', 'thumbs\Img30.jpg', 'thumbs\Img31.jpg', 'thumbs\Img32.jpeg', 'thumbs\Img33.jpeg', 'thumbs\Img34.jpeg', 'thumbs\Img35.png', 'thumbs\Img36.png', 'thumbs\Img37.jpg', 'thumbs\Img38.jpg', 'thumbs\Img39.jpg', 'thumbs\Img40.png', 'thumbs\Img41.jpg' ]

def prepare_text(text=None):
    brk = []
    for i in range(1, 7):
        brk.append(50*i)
    i = 0
    splited = text.split()
    new_text = ''
    for part in splited:
        if len(new_text + part) < brk[i]:
            new_text += part +' '
        else:
            new_text += '\n' +part +' '
            i += 1
    return new_text


def create_image_1(text=None):
    txt = prepare_text(text)
    like = randint(10, 30)
    dislike = randint(90, 350)
    img = Image.open('TemplatesTwitter/OneLine.jpg')
    fonte = ImageFont.truetype('Roboto-Medium.ttf', 27)
    font2 = ImageFont.truetype("Roboto-Medium.ttf", 16)
    draw = ImageDraw.Draw(img)
    draw.text((233, 458), txt, font=fonte, fill=(255,255,255), spacing=10)
    draw.text((282, 628), f'{like}', (174,174,174),font=font2)
    draw.text((439, 628), f'{dislike}', (174,174,174),font=font2)
    img.save('images/atual.png', 'PNG')
    
    thumbnail = choice(Thumbs)
    img2 = Image.open(thumbnail)
    new_image = img2.resize((798, 432))
    img.paste(new_image, (201, 1))
    img.save('images/atual.png', 'PNG')


def create_image_2(text=None):
    txt = prepare_text(text)
    like = randint(10, 30)
    dislike = randint(90, 350)
    vilcem = randint(100, 300)
    vilmil = randint(100, 900)
    img = Image.open('TemplatesTwitter\TwoLine.jpg')
    fonte = ImageFont.truetype('Roboto-Medium.ttf', 27)
    font2 = ImageFont.truetype("Roboto-Medium.ttf", 17)
    font3 = ImageFont.truetype("Roboto-Medium.ttf", 20)
    draw = ImageDraw.Draw(img)
    draw.text((256, 430), txt, font=fonte, fill=(255,255,255), spacing=12)
    draw.text((298, 623), f'{like} mil', (174,174,174),font=font2)
    draw.text((445, 623), f'{dislike}', (174,174,174),font=font2)
    draw.text((256, 520), f'{vilcem}.{vilmil} visualizações', (174,174,174),font=font3)
    img.save('images/atual.png', 'PNG')
    
    thumbnail = choice(Thumbs)
    img2 = Image.open(thumbnail)
    new_image = img2.resize((739, 407))
    img.paste(new_image, (226, 1))
    img.save('images/atual.png', 'PNG')


def create_image_3(text=None):
    txt = prepare_text(text)
    like = randint(1, 4)
    dislike = randint(90, 350)
    dezena = randint(10, 50)
    centena = randint(100, 999)
    centena1 = randint(100, 999)
    img = Image.open('TemplatesTwitter\ThreeLine.jpg')
    fonte = ImageFont.truetype('Roboto-Medium.ttf', 27)
    font2 = ImageFont.truetype("Roboto-Medium.ttf", 17)
    font3 = ImageFont.truetype("Roboto-Medium.ttf", 20)
    draw = ImageDraw.Draw(img)
    draw.text((248, 515), f'{dezena}.{centena}.{centena1} visualizações', font=font3,fill=(174,174,174))
    draw.text((248, 390), txt, font=fonte, fill=(255,255,255), spacing=12)
    draw.text((296, 627), f'{like} mi', (174,174,174),font=font2)
    draw.text((425, 627), f'{dislike} mil', (174,174,174),font=font2)
    img.save('images/atual.png', 'PNG')
    
    thumbnail = choice(Thumbs)
    img2 = Image.open(thumbnail)
    new_image = img2.resize((755, 368))
    img.paste(new_image, (218, 1))
    img.save('images/atual.png', 'PNG')


def create_image_4(text=None):
    txt = prepare_text(text)
    like = randint(100, 999)
    minute = randint(1, 9)
    nome = choice(names)
    img = Image.open('TemplatesTwitter\Comment.jpg')
    fonte = ImageFont.truetype('arial', 22)
    font2 = ImageFont.truetype("Roboto-Medium.ttf", 17)
    font3 = ImageFont.truetype("Roboto-Medium.ttf", 17)
    font4 = ImageFont.truetype('arial', 19)
    draw = ImageDraw.Draw(img)
    draw.text((357, 370), txt, font=fonte, fill=(255,255,255), spacing=9)
    draw.text((357, 335), f'{nome}  •  {minute} minutos atrás', (174,174,174),font=font4)
    draw.text((398, 598), f'{like}', (174,174,174),font=font4)
    img.save('images/atual.png', 'PNG')
    
    thumbnail = choice(Thumbs)
    img2 = Image.open(thumbnail)
    new_image = img2.resize((755, 368))
    img.paste(new_image, (219, -83))
    img.save('images/atual.png', 'PNG')

def create_image_5(text=None):
    txt = prepare_text(text)
    like = randint(10, 57)
    minute = randint(1, 9)
    nome = choice(names)
    img = Image.open('TemplatesTwitter\CommentMax.jpg')
    fonte = ImageFont.truetype('arial', 22)
    font2 = ImageFont.truetype("Roboto-Medium.ttf", 17)
    font3 = ImageFont.truetype("Roboto-Medium.ttf", 17)
    font4 = ImageFont.truetype('arial', 19)
    draw = ImageDraw.Draw(img)
    draw.text((357, 370), txt, font=fonte, fill=(255,255,255), spacing=8)
    draw.text((357, 335), f'{nome}  •  {minute} minutos atrás', (174,174,174),font=font4)
    draw.text((398, 598), f'{like}', (174,174,174),font=font4)
    img.save('images/atual.png', 'PNG')

def create_image_end(text=None):
    size = len(text)
    if size <= 49:
        create_image_1(text)
    elif 98 > size > 49:
        create_image_2(text)
    elif 148 > size > 98:
        create_image_3(text)
    elif 236 > size > 148:
        create_image_4(text)
    else:
        create_image_5(text)
