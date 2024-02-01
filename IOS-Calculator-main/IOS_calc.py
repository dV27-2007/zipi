from tkinter import *
import math
import random

win = Tk()
win.title("CALCUALTOR.ios")

ac1 = True
num = ''
num1 = False
c = False
c1 = False
c3 = False
mc = ''

# ------------------------menu---------------------------

main_menu = Menu()

Exit_menu = Menu(main_menu, tearoff=0)
Edit_menu = Menu(main_menu, tearoff=0)

main_menu.add_cascade(label="Exit", menu=Exit_menu)
main_menu.add_cascade(label="Edit", menu=Edit_menu)
Edit_menu.add_cascade(label='big', command=lambda:b_s())
Edit_menu.add_cascade(label='small', command=lambda:s_b())

win.config(menu=main_menu)

# ------------------------Image---------------------------

acimage = PhotoImage(file = "images\IMG_ac.png").subsample(3,3)
cimage = PhotoImage(file = "images\IMG_or.png").subsample(3,3)
procimage = PhotoImage(file = "images\IMG_%.png").subsample(3,3)
bajimage = PhotoImage(file = "images\IMG_baj.png").subsample(3,3)
sevenimage = PhotoImage(file = "images\IMG_7.png").subsample(6,6)
eghtimage = PhotoImage(file = "images\IMG_8.png").subsample(6,6)
nineimage = PhotoImage(file = "images\IMG_9.png").subsample(6,6)
bazimage = PhotoImage(file="images\IMG_baz.png").subsample(3,3)
fourimage = PhotoImage(file = "images\IMG_4.png").subsample(6,6)
fiveimage = PhotoImage(file = "images\IMG_5.png").subsample(6,6)
seximage = PhotoImage(file = "images\IMG_6.png").subsample(6,6)
minimage = PhotoImage(file="images\IMG_min.png").subsample(3,3)
oneimage = PhotoImage(file = "images\IMG_1.png").subsample(6,6)
twoimage = PhotoImage(file = "images\IMG_2.png").subsample(6,6)
threeimage = PhotoImage(file = "images\IMG_3.png").subsample(6,6)
plusimage = PhotoImage(file="images\IMG_plus.png").subsample(3,3)
zeroimage = PhotoImage(file = "images\IMG_0.png").subsample(3,3)
dotimage = PhotoImage(file = "images\IMG_dot.png").subsample(6,6)
havimage = PhotoImage(file="images\IMG_hav.png").subsample(3,3)

b_pag_image = PhotoImage(file = "images\img\IMG_big_pag.png").subsample(2,2)
b_bac_image = PhotoImage(file = "images\img\IMG_big_bac.png").subsample(2,2)
b_o_image = PhotoImage(file = "images\img\IMG_big_O.png").subsample(2,2)
b_one_image = PhotoImage(file = "images\img\IMG_big_1.png").subsample(2,2)
b_two_image = PhotoImage(file = "images\img\IMG_big_2.png").subsample(2,2)
b_three_image = PhotoImage(file = "images\img\IMG_big_3.png").subsample(2,2)
b_four_image = PhotoImage(file = "images\img\IMG_big_4.png").subsample(2,2)
b_five_image = PhotoImage(file="images\img\IMG_big_5.png").subsample(2,2)
b_six_image = PhotoImage(file = "images\img\IMG_big_6.png").subsample(2,2)
b_seven_image = PhotoImage(file = "images\img\IMG_big_7.png").subsample(2,2)
b_eght_image = PhotoImage(file = "images\img\IMG_big_8.png").subsample(2,2)
b_nine_image = PhotoImage(file="images\img\IMG_big_9.png").subsample(2,2)
b_1x_image = PhotoImage(file = "images\img\IMG_big_1x.png").subsample(2,2)
b_2_x_image = PhotoImage(file = "images\img\IMG_big_2_x.png").subsample(2,2)
b_3_x_image = PhotoImage(file = "images\img\IMG_big_3_x.png").subsample(2,2)
b_2nd_image = PhotoImage(file="images\img\IMG_big_2nd.png").subsample(2,2)
b_10x_image = PhotoImage(file = "images\img\IMG_big_10x.png").subsample(2,2)
b_ac_image = PhotoImage(file = "images\img\IMG_big_ac.png").subsample(2,2)
b_baj_image = PhotoImage(file="images\img\IMG_big_baj.png").subsample(2,2)
b_baz_image = PhotoImage(file = "images\img\IMG_big_baz.png").subsample(2,2)
b_cos_image = PhotoImage(file = "images\img\IMG_big_cos.png").subsample(2,2)
b_cosh_image = PhotoImage(file = "images\img\IMG_big_cosh.png").subsample(2,2)
b_dot_image = PhotoImage(file = "images\img\IMG_big_dot.png").subsample(2,2)
b_e_image = PhotoImage(file = "images\img\IMG_big_e.png").subsample(2,2)
b_EE_image = PhotoImage(file = "images\img\IMG_big_EE.png").subsample(2,2)
b_ex_image = PhotoImage(file = "images\img\IMG_big_ex.png").subsample(2,2)
b_hav_image = PhotoImage(file="images\img\IMG_big_hav.png").subsample(2,2)
b_ln_image = PhotoImage(file = "images\img\IMG_big_ln.png").subsample(2,2)
b_log10_image = PhotoImage(file = "images\img\IMG_big_log10.png").subsample(2,2)
b_m_min_image = PhotoImage(file = "images\img\IMG_big_m_min.png").subsample(2,2)
b_m_plus_image = PhotoImage(file="images\img\IMG_big_m_plus.png").subsample(2,2)
b_mc_image = PhotoImage(file = "images\img\IMG_big_mc.png").subsample(2,2)
b_min_image = PhotoImage(file = "images\img\IMG_big_min.png").subsample(2,2)
b_mr_image = PhotoImage(file = "images\img\IMG_big_mr.png").subsample(2,2)
b_or_image = PhotoImage(file="images\img\IMG_big_or.png").subsample(2,2)
b_pi_image = PhotoImage(file = "images\img\IMG_big_pi.png").subsample(2,2)
b_plus_image = PhotoImage(file = "images\img\IMG_big_plus.png").subsample(2,2)
b_Rad_image = PhotoImage(file="images\img\IMG_big_Rad.png").subsample(2,2)
b_Rand_image = PhotoImage(file = "images\img\IMG_big_Rand.png").subsample(2,2)
b_sin_image = PhotoImage(file = "images\img\IMG_big_sin.png").subsample(2,2)
b_sinh_image = PhotoImage(file = "images\img\IMG_big_sinh.png").subsample(2,2)
b_tan_image = PhotoImage(file="images\img\IMG_big_tan.png").subsample(2,2)
b_tanh_image = PhotoImage(file = "images\img\IMG_big_tanh.png").subsample(2,2)
b_xf_image = PhotoImage(file = "images\img\IMG_big_x_fac.png").subsample(2,2)
b_x2_image = PhotoImage(file = "images\img\IMG_big_x2.png").subsample(2,2)
b_x3_image = PhotoImage(file="images\img\IMG_big_x3.png").subsample(2,2)
b_xy_image = PhotoImage(file = "images\img\IMG_big_xy.png").subsample(2,2)
b_y_x_image = PhotoImage(file = "images\img\IMG_big_y_x.png").subsample(2,2)
b_tok_image = PhotoImage(file="images\img\IMG_big_tokos.png").subsample(2,2)

# ------------------------enter---------------------------

calc = Label(win, text='0', width=13, fg='white', height=3 ,background="black", anchor="e", justify="right", font=('Arial', 35))

# ------------------------button---------------------------

def s_button():
    global ac1, calc, acimage, cimage, procimage, bajimage, sevenimage, eghtimage, nineimage, bazimage, fourimage, fiveimage, seximage, minimage, oneimage, twoimage, threeimage, plusimage, zeroimage, dotimage, havimage
    calc["width"] = 13
    calc["height"] = 3
    calc.grid(row=0, column=0, columnspan=4, padx=5)
    ac = Button(win, text="AC",cursor="hand2", fg="black", image= acimage, bd=0, bg="black",command=lambda:fun('ac')).grid(row=1, column=0)
    c = Button(win, text="+/-", fg="black",cursor="hand2", image= cimage, bd=0, bg="black",command=lambda:fun('or')).grid(row=1, column=1)
    proc = Button(win, text="%", fg="black",cursor="hand2", image= procimage, bd=0, bg="black",command=lambda:fun('%')).grid(row=1, column=2)
    baj = Button(win, text="/", fg="black",cursor="hand2", image= bajimage, bd=0, bg="black",command=lambda:fun('/')).grid(row=1, column=3)
    seven = Button(win, text="7", fg="black",cursor="hand2", image= sevenimage, bd=0, bg="black",command=lambda:calcuater('7')).grid(row=2, column=0, pady=20)
    eght = Button(win, text="8", fg="black",cursor="hand2", image= eghtimage, bd=0, bg="black",command=lambda:calcuater('8')).grid(row=2, column=1)
    nine = Button(win, text="9", fg="black",cursor="hand2", image= nineimage, bd=0, bg="black",command=lambda:calcuater('9')).grid(row=2, column=2)
    baz = Button(win, text="*", fg="black",cursor="hand2", image= bazimage, bd=0, bg="black",command=lambda:fun('*')).grid(row=2, column=3)
    four = Button(win, text="4", fg="black",cursor="hand2", image= fourimage, bd=0, bg="black",command=lambda:calcuater('4')).grid(row=3, column=0)
    five = Button(win, text="5", fg="black",cursor="hand2", image= fiveimage, bd=0, bg="black",command=lambda:calcuater('5')).grid(row=3, column=1)
    sex = Button(win, text="6", fg="black",cursor="hand2", image= seximage, bd=0, bg="black",command=lambda:calcuater('6')).grid(row=3, column=2)
    smin = Button(win, text="-", fg="black",cursor="hand2", image= minimage, bd=0, bg="black",command=lambda:fun('-')).grid(row=3, column=3)
    one = Button(win, text="1", fg="black",cursor="hand2", image= oneimage, bd=0, bg="black",command=lambda:calcuater('1')).grid(row=4, column=0, pady=20)
    two = Button(win, text="2", fg="black",cursor="hand2", image= twoimage, bd=0, bg="black",command=lambda:calcuater('2')).grid(row=4, column=1)
    three = Button(win, text="3", fg="black",cursor="hand2", image= threeimage, bd=0, bg="black",command=lambda:calcuater('3')).grid(row=4, column=2)
    plus = Button(win, text="+", fg="black",cursor="hand2", image= plusimage, bd=0, bg="black",command=lambda:fun('+')).grid(row=4, column=3)
    zero = Button(win, text="0", fg="black",cursor="hand2", image= zeroimage, bd=0, bg="black",command=lambda:calcuater('0')).grid(row=5, column=0, columnspan=2)
    dot = Button(win, text=".", fg="black",cursor="hand2", image= dotimage, bd=0, bg="black",command=lambda:calcuater('.')).grid(row=5, column=2)
    hav = Button(win, text="=", fg="black",cursor="hand2", image= havimage, bd=0, bg="black",command=lambda:fun('=')).grid(row=5, column=3)
    ac1 = True
s_button()


def b_button():
    global ac1, calc, b_pag_image, b_bac_image, b_o_image, b_one_image, b_two_image, b_three_image, b_four_image, b_five_image, b_six_image, b_seven_image, b_eght_image, b_nine_image, b_1x_image, b_2_x_image, b_3_x_image, b_2nd_image, b_10x_image, b_ac_image, b_baj_image, b_baz_image, b_cos_image, b_dot_image, b_e_image, b_EE_image, b_ex_image, b_hav_image, b_ln_image, b_log10_image, b_m_min_image, b_m_plus_image, b_mc_image, b_mr_image, b_or_image, b_pi_image, b_plus_image, b_Rad_image, b_Rand_image, b_sin_image, b_sinh_image, b_tan_image, b_tanh_image, b_xf_image,b_x2_image, b_x3_image, b_xy_image, b_y_x_image
    calc['width'] = 33
    calc["height"] = 3
    calc.grid(row=0, column=0, columnspan=10, padx=5)
    pag= Button(win, text="(",cursor="hand2", fg="black", image= b_pag_image, bd=0, bg="black",command=lambda:calcuater('(')).grid(row=1, column=0)
    bac = Button(win, text=")", fg="black",cursor="hand2", image= b_bac_image, bd=0, bg="black",command=lambda:calcuater(')')).grid(row=1, column=1)
    mac = Button(win, text="%", fg="black",cursor="hand2", image= b_mc_image, bd=0, bg="black",command=lambda:big_fun('mc')).grid(row=1, column=2)
    mp = Button(win, text="/", fg="black",cursor="hand2", image= b_m_plus_image, bd=0, bg="black",command=lambda:big_fun('m+')).grid(row=1, column=3)
    mm = Button(win, text="7", fg="black",cursor="hand2", image= b_m_min_image, bd=0, bg="black",command=lambda:big_fun('m-')).grid(row=1, column=4, pady=5)
    mr = Button(win, text="8", fg="black",cursor="hand2", image= b_mr_image, bd=0, bg="black",command=lambda:big_fun('mr')).grid(row=1, column=5)
    bac = Button(win, text="9", fg="black",cursor="hand2", image= b_ac_image, bd=0, bg="black",command=lambda:fun('ac')).grid(row=1, column=6)
    bor = Button(win, text="*", fg="black",cursor="hand2", image= b_or_image, bd=0, bg="black",command=lambda:fun('or')).grid(row=1, column=7)
    btok = Button(win, text="4", fg="black",cursor="hand2", image= b_tok_image, bd=0, bg="black",command=lambda:fun('%')).grid(row=1, column=8)
    bbaj = Button(win, text="5", fg="black",cursor="hand2", image= b_baj_image, bd=0, bg="black",command=lambda:fun('/')).grid(row=1, column=9)
    
    nd = Button(win, text="6", fg="black",cursor="hand2", image= b_2nd_image, bd=0, bg="black",command=lambda:big_fun('2nd')).grid(row=2, column=0)
    x2 = Button(win, text="x2", fg="black",cursor="hand2", image= b_x2_image, bd=0, bg="black",command=lambda:fun('x2')).grid(row=2, column=1)
    x3 = Button(win, text="1", fg="black",cursor="hand2", image= b_x3_image, bd=0, bg="black",command=lambda:fun('x3')).grid(row=2, column=2, pady=5)
    xy = Button(win, text="2", fg="black",cursor="hand2", image= b_xy_image, bd=0, bg="black",command=lambda:fun('xy')).grid(row=2, column=3)
    ex = Button(win, text="3", fg="black",cursor="hand2", image= b_ex_image, bd=0, bg="black",command=lambda:fun('ex')).grid(row=2, column=4)
    x10 = Button(win, text="0", fg="black",cursor="hand2", image= b_10x_image, bd=0, bg="black",command=lambda:fun('x10')).grid(row=2, column=5)
    bseven = Button(win, text="+", fg="black",cursor="hand2", image= b_seven_image, bd=0, bg="black",command=lambda:calcuater('7')).grid(row=2, column=6)
    beght = Button(win, text="0", fg="black",cursor="hand2", image= b_eght_image, bd=0, bg="black",command=lambda:calcuater('8')).grid(row=2, column=7)
    bnine = Button(win, text=".", fg="black",cursor="hand2", image= b_nine_image, bd=0, bg="black",command=lambda:calcuater('9')).grid(row=2, column=8)
    bbaz = Button(win, text="*", fg="black",cursor="hand2", image= b_baz_image, bd=0, bg="black",command=lambda:fun('*')).grid(row=2, column=9)
    
    x1 = Button(win, text="1/x", fg="black",cursor="hand2", image= b_1x_image, bd=0, bg="black",command=lambda:fun('1/x')).grid(row=3, column=0)
    x_2 = Button(win, text="x_2",cursor="hand2", fg="black", image= b_2_x_image, bd=0, bg="black",command=lambda:fun('x_2')).grid(row=3, column=1)
    x_3 = Button(win, text="x_3", fg="black",cursor="hand2", image= b_3_x_image, bd=0, bg="black",command=lambda:fun('x_3')).grid(row=3, column=2)
    x_y = Button(win, text="x_y", fg="black",cursor="hand2", image= b_y_x_image, bd=0, bg="black",command=lambda:fun('x_y')).grid(row=3, column=3)
    ln = Button(win, text="ln", fg="black",cursor="hand2", image= b_ln_image, bd=0, bg="black",command=lambda:fun('ln')).grid(row=3, column=4)
    log = Button(win, text="log", fg="black",cursor="hand2", image= b_log10_image, bd=0, bg="black",command=lambda:fun('log')).grid(row=3, column=5, pady=5)
    bfour = Button(win, text="4", fg="black",cursor="hand2", image= b_four_image, bd=0, bg="black",command=lambda:calcuater('4')).grid(row=3, column=6)
    bfive = Button(win, text="5", fg="black",cursor="hand2", image= b_five_image, bd=0, bg="black",command=lambda:calcuater('5')).grid(row=3, column=7)
    bsix = Button(win, text="6", fg="black",cursor="hand2", image= b_six_image, bd=0, bg="black",command=lambda:calcuater('6')).grid(row=3, column=8)
    bmin = Button(win, text="-", fg="black",cursor="hand2", image= b_min_image, bd=0, bg="black",command=lambda:fun('-')).grid(row=3, column=9)
    
    xf = Button(win, text="5", fg="black",cursor="hand2", image= b_xf_image, bd=0, bg="black",command=lambda:fun('x!')).grid(row=4, column=0)
    sin = Button(win, text="6", fg="black",cursor="hand2", image= b_sin_image, bd=0, bg="black",command=lambda:fun('sin')).grid(row=4, column=1)
    cos = Button(win, text="-", fg="black",cursor="hand2", image= b_cos_image, bd=0, bg="black",command=lambda:fun('cos')).grid(row=4, column=2)
    tan = Button(win, text="1", fg="black",cursor="hand2", image= b_tan_image, bd=0, bg="black",command=lambda:fun('tan')).grid(row=4, column=3, pady=5)
    e = Button(win, text="2", fg="black",cursor="hand2", image= b_e_image, bd=0, bg="black",command=lambda:fun('e')).grid(row=4, column=4)
    EE = Button(win, text="3", fg="black",cursor="hand2", image= b_EE_image, bd=0, bg="black",command=lambda:fun('EE')).grid(row=4, column=5)
    bone = Button(win, text="0", fg="black",cursor="hand2", image= b_one_image, bd=0, bg="black",command=lambda:calcuater('1')).grid(row=4, column=6)
    btwo = Button(win, text="+", fg="black",cursor="hand2", image= b_two_image, bd=0, bg="black",command=lambda:calcuater('2')).grid(row=4, column=7)
    bthree = Button(win, text="0", fg="black",cursor="hand2", image= b_three_image, bd=0, bg="black",command=lambda:calcuater('3')).grid(row=4, column=8)
    bplus = Button(win, text=".", fg="black",cursor="hand2", image= b_plus_image, bd=0, bg="black",command=lambda:fun('+')).grid(row=4, column=9)
    
    Rad = Button(win, text="=", fg="black",cursor="hand2", image= b_Rad_image, bd=0, bg="black",command=lambda:fun('Rad')).grid(row=5, column=0)
    sinh = Button(win, text="1", fg="black",cursor="hand2", image= b_sinh_image, bd=0, bg="black",command=lambda:fun('sinh')).grid(row=5, column=1, pady=5)
    cosh = Button(win, text="2", fg="black",cursor="hand2", image= b_cosh_image, bd=0, bg="black",command=lambda:fun('cosh')).grid(row=5, column=2)
    tanh = Button(win, text="3", fg="black",cursor="hand2", image= b_tanh_image, bd=0, bg="black",command=lambda:fun('tanh')).grid(row=5, column=3)
    pi = Button(win, text="0", fg="black",cursor="hand2", image= b_pi_image, bd=0, bg="black",command=lambda:fun('pi')).grid(row=5, column=4)
    Rand = Button(win, text="+", fg="black",cursor="hand2", image= b_Rand_image, bd=0, bg="black",command=lambda:fun('Rand')).grid(row=5, column=5)
    bzero = Button(win, text="0", fg="black",cursor="hand2", image= b_o_image, bd=0, bg="black",command=lambda:calcuater('0')).grid(row=5, column=6, columnspan=2)
    bdot = Button(win, text=".", fg="black",cursor="hand2", image= b_dot_image, bd=0, bg="black",command=lambda:calcuater('.')).grid(row=5, column=8)
    bhav = Button(win, text="=", fg="black",cursor="hand2", image= b_hav_image, bd=0, bg="black",command=lambda:fun('=')).grid(row=5, column=9)
    ac1 = False

# ------------------------function---------------------------

def b_s():
    global b_pag_image, b_bac_image, b_mc_image, b_m_plus_image, b_2nd_image, b_x2_image, b_x3_image, b_xy_image, b_1x_image, b_2_x_image, b_3_x_image, b_y_x_image , b_xf_image, b_sin_image, b_cos_image, b_tan_image, b_Rad_image, b_sinh_image, b_cosh_image, b_tanh_image
    win.geometry("1050x710")
    b_pag_image = PhotoImage(file = "images\img\IMG_big_pag.png").subsample(2,2)
    b_bac_image = PhotoImage(file = "images\img\IMG_big_bac.png").subsample(2,2)
    b_m_plus_image = PhotoImage(file="images\img\IMG_big_m_plus.png").subsample(2,2)
    b_mc_image = PhotoImage(file = "images\img\IMG_big_mc.png").subsample(2,2)
    b_2nd_image = PhotoImage(file="images\img\IMG_big_2nd.png").subsample(2,2)
    b_x2_image = PhotoImage(file = "images\img\IMG_big_x2.png").subsample(2,2)
    b_x3_image = PhotoImage(file="images\img\IMG_big_x3.png").subsample(2,2)
    b_xy_image = PhotoImage(file = "images\img\IMG_big_xy.png").subsample(2,2)
    b_1x_image = PhotoImage(file = "images\img\IMG_big_1x.png").subsample(2,2)
    b_2_x_image = PhotoImage(file = "images\img\IMG_big_2_x.png").subsample(2,2)
    b_3_x_image = PhotoImage(file = "images\img\IMG_big_3_x.png").subsample(2,2)
    b_y_x_image = PhotoImage(file = "images\img\IMG_big_y_x.png").subsample(2,2)
    b_xf_image = PhotoImage(file = "images\img\IMG_big_x_fac.png").subsample(2,2)
    b_sin_image = PhotoImage(file = "images\img\IMG_big_sin.png").subsample(2,2)
    b_cos_image = PhotoImage(file = "images\img\IMG_big_cos.png").subsample(2,2)
    b_tan_image = PhotoImage(file="images\img\IMG_big_tan.png").subsample(2,2)
    b_Rad_image = PhotoImage(file="images\img\IMG_big_Rad.png").subsample(2,2)
    b_sinh_image = PhotoImage(file = "images\img\IMG_big_sinh.png").subsample(2,2)
    b_cosh_image = PhotoImage(file = "images\img\IMG_big_cosh.png").subsample(2,2)
    b_tanh_image = PhotoImage(file = "images\img\IMG_big_tanh.png").subsample(2,2)
    b_button()
def s_b():
    global b_pag_image, b_bac_image, b_mc_image, b_m_plus_image,  b_2nd_image, b_x2_image, b_x3_image, b_xy_image, b_1x_image, b_2_x_image, b_3_x_image, b_y_x_image, b_xf_image, b_sin_image, b_cos_image, b_tan_image, b_Rad_image, b_sinh_image, b_cosh_image, b_tanh_image
    win.geometry("400x710")
    b_pag_image = ''
    b_bac_image = ''
    b_mc_image = ''
    b_m_plus_image = ''
    b_2nd_image = ''
    b_x2_image = ''
    b_x3_image = ''
    b_xy_image = ''
    b_1x_image = ''
    b_2_x_image = ''
    b_3_x_image = ''
    b_y_x_image = ''
    b_xf_image = ''
    b_sin_image = ''
    b_cos_image = ''
    b_tan_image = ''
    b_Rad_image = ''
    b_sinh_image = ''
    b_cosh_image = ''
    b_tanh_image = ''
    s_button()

def calcuater(val):
    global calc, acimage, b_ac_image, ac1
    global c
    global num
    global c3
        
    
        
    if c == True:
        calc['text'] = '0'
        c = False

    if val == '.':pass
    
    elif calc["text"][0] == '0' and '.' not in calc["text"]:
        calc["text"] = calc["text"][1:]

    calc["text"]  = calc["text"]  + val
    
    if c3 == True:
        num = num+'0'*int(calc['text'])
        calc["text"] = num
        num = ''
        c3 = False
        
    acimage = ''
    acimage = PhotoImage(file = "images\IMG_c.png").subsample(3,3)
        
    if ac1 == False:
       b_ac_image = PhotoImage(file="images\img\IMG_big_c.png").subsample(2,2)
    
    


def big_fun(val):
    global calc
    global mc
    global num
    
    calc["text"] = str(calc["text"])
    
    if val == 'mc' or 'm+' or 'm-' or 'mr' and calc["text"]:
        if val == 'mc':
                mc = ''
        elif val == 'm+':
                mc = calc['text']
        elif val == 'm-':
                mc = '-'+calc["text"]    
        else:
            calc["text"] = calc["text"][len(calc["text"]):] + mc
            
            
    if val == "2nd":
        pass
    



def fun(val):
    global calc, acimage, ac1, b_ac_image
    global num
    global num1
    global c
    global c1
    global c3
    
    calc["text"] = str(calc["text"])
    
    if val == 'ac':
        calc["text"] = '0'
        if ac1 == True:
            acimage = ''
            acimage = PhotoImage(file = "images\IMG_ac.png").subsample(3,3)
            
        elif ac1 == False:
            b_ac_image = PhotoImage(file = "images\img\IMG_big_ac.png").subsample(2,2)
    
    elif val == 'or':
        if c1 == False:
            calc["text"] = '-' + calc["text"]
            c1 = True
            
        elif c1 == True and calc["text"][0] == "-":
            calc["text"] = calc["text"][1:]
            c1 = False
    
    elif val == '%':
        calc["text"] = int(calc["text"])/100
        calc["text"] = str(calc["text"])
        num += calc["text"]
    
    elif val == '/':
        num += calc['text']+'/'
        c = True
    
    elif val == '*':
        num += calc['text']+'*'
        c = True
    
    elif val == '-':
        num += calc['text']+'-'
        c = True
    
    elif val == '+':
        num += calc['text']+'+'
        c = True
        
    elif val == "x2":
        calc['text'] = str(eval(calc["text"]+'**2'))
        
    elif val == "x3":
        calc['text'] = str(eval(calc["text"]+'**3'))
        
    elif val == "xy":
        num = calc["text"]+'**'
        c = True
        
    elif val == "ex":
        calc["text"] = calc["text"]+'**'+str(math.e)
        fun('=')
        
    elif val == "x10":
        calc["text"] = "10"+'**'+calc["text"]
        fun('=')
    
    elif val == "1/x":
        calc["text"] = '1/'+calc["text"]
        fun('=')
        
    elif val == 'x_2':
        calc['text'] = calc["text"]+'**0.5'
        fun('=')
    
    elif val == 'x_3':
        calc['text'] = calc["text"]+'**(1/3)'
        fun('=')
    
    elif val == 'x_y':
        num+=calc["text"]+'**(1/'
        num1 = True
        c = True
        
    elif val == 'ln':
        a = calc["text"]
        calc['text'] = str(math.log(a))
        calc["text"] = calc["text"][:-2]
        
    elif val == 'log':
        a = int(calc["text"])
        calc["text"] = str(math.log10(a))
        calc["text"] = calc["text"][:-2]
        
    elif val == 'x!':
        s = 1
        for el in range(1,int(calc["text"])+1):
            s=s*el
        calc['text'] = s
        s = 1
    
    elif val == 'sin':
        calc["text"] = str(math.sin(int(calc['text'])))
        calc["text"] = calc["text"][:-2]
        
    elif val == 'cos':
        calc["text"] = str(math.cos(int(calc['text'])))
        calc["text"] = calc["text"][:-2]
        
    elif val == 'tan':
        calc["text"] = str(math.tan(int(calc['text'])))
        calc["text"] = calc["text"][:-2]
        
    elif val == 'e':
        calc["text"] = str(math.e)
        
    elif val == 'EE':
        num += calc['text']
        c = True
        c3 = True
        
    elif val == 'Rad':
        pass
    
    elif val == 'sinh':
        calc["text"] = str(math.sinh(int(calc["text"])))
        
    elif val == 'cosh':
        calc["text"] = str(math.cosh(int(calc["text"])))
        
    elif val == 'tanh':
        calc["text"] = str(math.tanh(int(calc["text"])))
        
    elif val == 'pi':
        calc["text"] = str(math.pi)
        
    elif val == 'Rand':
        calc["text"] = str(random.random())
        
    
    if val == '=':
        if c3 == True:
            calc["text"] = calc["text"]+"0"*int(calc["text"])
            num = ''
            c3 = False
            
        if num1 == True:
            num+=calc["text"]
            num=num+')'
            calc["text"] = num
            num = ''
            num1 = False
            
        num = num + calc["text"]
        calc["text"] = str(eval(num))
        num = ''
        c = True
        
        if calc["text"][-1] == "0" and calc["text"][-2] == ".":
            calc["text"] = calc["text"][:-2]


win.grid_columnconfigure(0, minsize=15)
win.grid_columnconfigure(1, minsize=15)
win.grid_columnconfigure(2, minsize=15)
win.grid_rowconfigure(1, minsize=15)
win.grid_rowconfigure(2, minsize=15)
win.grid_rowconfigure(3, minsize=15)
win.grid_rowconfigure(4, minsize=15)

win.iconbitmap("images\icon.ico")
win.config(bg="black")
win.resizable(False, False)
win.mainloop()

