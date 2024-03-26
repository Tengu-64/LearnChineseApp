# -*- coding: utf8 -*-
from tkinter import *
import tkinter as tk
from tkhtmlview import HTMLLabel
import random as rand

window = Tk()
window.geometry('1024x700')
photo = tk.PhotoImage(file='logo.png')
window.iconphoto(False, photo)
window.resizable(False,False)
window.title("Подготовка HSK1")

word = ['爱','八','爸爸','杯子','北京','本','不客气','不','菜','茶','吃','出租车','打电话','大','的','点','电脑','电视','电影','东西','都','读','对不起','多','多少','儿子','二','饭馆','飞机','分钟','高兴','个','工作','狗','汉语','好','喝','和','很','后面','回','会','火车站','几','家','叫','今天','九','开','看'] # 50 слов
translate = ['любить','восемь','папа','стакан','Пекин','счётное слово для растений','пожалуйста','не','блюдо','чай','есть','такси','звонить по телефону','большой','суффикс притяжательности','капля; немножко, чуточку; точка; запятая','компьютер','телевизор','кино','вещь; предмет','все; всё','читать','виноват!, простите!, извините!','много','сколько?','сын','два; второй','ресторан','самолет','минута','радоваться; радостный ','универсальное счетное слово','работать; работа ','собака','китайский язык','хороший; хорошо; приятный; удобный','пить','мирный; союз и; предлог с','очень; весьма ','задняя сторона; зад; позади, сзади; задний ','возвращаться','уметь; мочь; владеть; собрание; заседание','вокзал; железнодорожная станция','сколько?; несколько; немного ','семья; семейство; дом; домашний ','кричать; крик; звать; подзывать; вызывать','сегодня','девять; девятый','открывать; управлять; вести; включать ','смотреть; читать (про себя); навестить']


def wrdList(): # показывает список слов
    aboutHsk.pack_forget() 
    wordsValue.pack_forget()
    startButton.pack_forget()
    shoWords.pack_forget()
    
    title['text'] = 'Список слов HSK1'

    val = 0
    for i in word:  
        wrd = tk.Label(window, 
                    text = f"{word[val]} - {translate[val]}", 
                    height= 2,
                    font=("Arial Bold", 16) )
        wrd.pack()
        val+=1


        
wrdLen = len(word)
randWords = [0,1,2,3]# 4 числа, которые будут случайными
for x in range(4):
    randWords[x] = rand.randint(0,wrdLen-1)  # замена значений массива на действительно случайные
    print(randWords[x])

answer = rand.randint(0,3) # рандомный ответ
print('-------')
print(answer)
print('Правильный ответ (индекс)',randWords[answer])



def test(): # функция удаляет кнопку и все Label (за исключением title) и создает тест (...)
    aboutHsk.pack_forget() 
    wordsValue.pack_forget()
    startButton.pack_forget()
    shoWords.pack_forget() 
    title['text'] = 'Тест к словам HSK1'
    
    
    
    answr = tk.Label(window, 
                    text=f'{translate[randWords[answer]]}',
                    font=("Arial Bold", 20),
                    height=10,)
    answr.pack() # вывод случайного слова на русском

    a = tk.Label(window, text='')
    a.pack()

    btn1.pack() # вывод кнопок для идентификации ответа
    btn2.pack()
    btn3.pack()
    btn4.pack()
   
def TrueOrFalseAnswer():

    # answer - индекс правильного ответа в randWords
    # randWords[answer] - индекс правильного ответа для words[] или translate
    ch = tk.Label(window, text='', font = ('Bold', 16), pady=20, fg='green')
    ch.pack()

    if (btn1['value'] == randWords[answer]):
        btn1['bg'] = 'green'
    else:
         btn1['bg'] = 'red'

    if (btn2['value'] == randWords[answer]):
        btn2['bg'] = 'green'
    else:
         btn2['bg'] = 'red'

    if (btn3['value'] == randWords[answer]):
        btn3['bg'] = 'green'
    else:
        btn3['bg'] = 'red'

    if (btn4['value'] == randWords[answer]):
        btn4['bg'] = 'green' 
    else:
        btn4['bg'] = 'red'

    



title = tk.Label(window, text="HSK 1",
                font=("Arial Bold", 20),  
              height=2)

aboutHsk = HTMLLabel(window, 
                    html='''
                    <p>HSK (Hanyu Shuiping Kaoshi, Ханьюй Шуйпин Каоши, 汉语水平考试) - это государственный экзамен КНР для сертификации уровня владения китайским языком лицами,
не являющимися носителями китайского языка.</p>

<p>По сути, это китайский аналог TOEFL или IELTS. Тест проводится по трем уровням: базовому, начально-среднему и высшему. К 1 и 2 уровню HSK допускаются те, кто на 
начальном или среднем уровне знают китайский язык и проучились около 400-2000 часов на курсах. К высшему уровню допускаются те, кто прослушал 3000 и более 
часов на курсах.</p>

<p>Базовый уровень (基础) - длительность экзамена 135 минут. Рекомендуется сдавать лицам, изучавшим китайский язык от 100 до 800 часов и овладевшим словарным
запасом в объеме 400-3000 слов.</p>

<p>Данное приложение предназначено для того, чтобы повторить выученные слова к HSK 1</p>
''',
                    width=140, 
                    height=20)

wordsValue = tk.Label(window,
                    text = f"всего {len(word)} слов, нажмите на кнопку чтобы посмотреть список слов или начать тестирование",
                    font="Bold",
                    height=3
                    )

shoWords = tk.Button(window,
                    text='Список слов',
                    command=wrdList,
                    font='Bold',
                    height=2,
                    padx=40,
                    pady=5
                    )

startButton = tk.Button(window, 
                    text='Начать изучение слов',
                    command = test,
                    font = 'Bold',
                    height=2,
                    padx=5,
                    pady=6  
                      )                    

var = IntVar()

# 4 кнопки для идентификации ответа
btn1 = tk.Radiobutton(window, text=f'{word[randWords[0]]}', font=("Arial Bold", 20), variable=var ,value=randWords[0], command=TrueOrFalseAnswer)
btn2 = tk.Radiobutton(window, text=f'{word[randWords[1]]}', font=("Arial Bold", 20), variable=var ,value=randWords[1], command=TrueOrFalseAnswer)
btn3 = tk.Radiobutton(window, text=f'{word[randWords[2]]}', font=("Arial Bold", 20), variable=var, value=randWords[2], command=TrueOrFalseAnswer)
btn4 = tk.Radiobutton(window, text=f'{word[randWords[3]]}', font=("Arial Bold", 20), variable=var, value=randWords[3], command=TrueOrFalseAnswer)

title.pack()
aboutHsk.pack(padx=5, pady=1)
wordsValue.pack()
shoWords.pack()
startButton.pack()
window.mainloop()