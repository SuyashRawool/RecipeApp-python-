from tkinter import *
from SearchEngine import SearchEngine
from PIL import Image, ImageTk
from urllib.request import urlopen
import io
from functools import partial
import webbrowser
import tkinter.font as font


def openUrl(url): # to open new link
    webbrowser.open_new_tab(url)


def fullScreen():
    root.attributes("-fullscreen", True)


def windowScreen():
    root.attributes("-fullscreen", False)


def newFrame(id): #After clicking on more info
    se = SearchEngine()
    se.setData(id)
    print(se.data)

    for wid in frame1.winfo_children(): # deleting previous items on this frame
        wid.destroy()


    labelTitle = Label(frame1, text=se.getTitlef(), font=(
        "arial italic", 18), bg='#a855ff', fg='white')
    labelTitle.place(relx=0.5, y=20, anchor=CENTER)

    imgUrl = se.getImagef()
    u = urlopen(imgUrl)
    my_picture = io.BytesIO(u.read())

    image = Image.open(my_picture)
    resize = image.resize((420, 340))
    img = ImageTk.PhotoImage(resize)
    labelImg = Label(frame1, image=img, bd=3)
    labelImg.image = img
    labelImg.place(x=10, y=80, relwidth=0.5, relheight=0.4)

    publisher = Label(frame1, text='Publisher : '+se.getPublisherf(),
                      font=("arial italic", 14), bg='#a855ff', fg='white')
    publisher.place(x=400, y=200)

    source = Button(frame1, text='Source', font=("arial italic", 12),
                    bg='#55FFFD', command=partial(openUrl, se.getSourceUrlf()))
    source.place(x=400, y=250)

    recipeTilte = Label(frame1, text='Recipe :', bg='#a855ff',
                        fg='#66FF33', font=("arial italic", 20, 'bold'))
    recipeTilte.place(y=445, x=40)
    recipeFrame = Frame(frame1, bg='#ECF0F1')
    recipeFrame.place(relwidth=0.9, relheight=0.35, relx=0.05, y=480)
    scrollbar2 = Scrollbar(recipeFrame)
    scrollbar2.pack(side=RIGHT, fill=Y)
    recipeList = Listbox(recipeFrame, width=400,
                         yscrollcommand=scrollbar2.set, font=("arial italic", 14))

    for line in se.getRecipef():
        recipeList.insert(END, "->" + str(line))

    recipeList.pack(side=LEFT, fill=BOTH)
    scrollbar2.config(command=recipeList.yview)


def findBtn():

    se = SearchEngine()
    query = searchBox.get('1.0', END)
    query = query.strip()



    try:
        data = se.searchQuery(query)['recipes']
        strVar.set("")
    except:
        print('There was an error!')
        strVar.set("Sorry, We don't have this key word")

        return
    #data=[{'publisher': '101 Cookbooks', 'title': 'Best Pizza Dough Ever', 'source_url': 'http://www.101cookbooks.com/archives/001199.html', 'recipe_id': '47746', 'image_url': 'http://forkify-api.herokuapp.com/images/best_pizza_dough_recipe1b20.jpg', 'social_rank': 100, 'publisher_url': 'http://www.101cookbooks.com'}, {'publisher': 'The Pioneer Woman', 'title': 'Deep Dish Fruit Pizza', 'source_url': 'http://thepioneerwoman.com/cooking/2012/01/fruit-pizza/', 'recipe_id': '46956', 'image_url': 'http://forkify-api.herokuapp.com/images/fruitpizza9a19.jpg', 'social_rank': 100, 'publisher_url': 'http://thepioneerwoman.com'}, {'publisher': 'Closet Cooking', 'title': 'Pizza Dip', 'source_url': 'http://www.closetcooking.com/2011/03/pizza-dip.html', 'recipe_id': '35477', 'image_url': 'http://forkify-api.herokuapp.com/images/Pizza2BDip2B12B500c4c0a26c.jpg', 'social_rank': 99.99999999999994, 'publisher_url': 'http://closetcooking.com'}, {'publisher': 'Closet Cooking', 'title': 'Cauliflower Pizza Crust (with BBQ Chicken Pizza)', 'source_url': 'http://www.closetcooking.com/2013/02/cauliflower-pizza-crust-with-bbq.html', 'recipe_id': '41470', 'image_url': 'http://forkify-api.herokuapp.com/images/BBQChickenPizzawithCauliflowerCrust5004699695624ce.jpg', 'social_rank': 99.9999999999994, 'publisher_url': 'http://closetcooking.com'}, {'publisher': 'Closet Cooking', 'title': 'Pizza Quesadillas (aka Pizzadillas)', 'source_url': 'http://www.closetcooking.com/2012/11/pizza-quesadillas-aka-pizzadillas.html', 'recipe_id': '35478', 'image_url': 'http://forkify-api.herokuapp.com/images/Pizza2BQuesadillas2B2528aka2BPizzadillas25292B5002B834037bf306b.jpg', 'social_rank': 99.99999999999835, 'publisher_url': 'http://closetcooking.com'}, {'publisher': 'Two Peas and Their Pod', 'title': 'Sweet Potato Kale Pizza with Rosemary & Red Onion', 'source_url': 'http://www.twopeasandtheirpod.com/sweet-potato-kale-pizza-with-rosemary-red-onion/', 'recipe_id': '54454', 'image_url': 'http://forkify-api.herokuapp.com/images/sweetpotatokalepizza2c6db.jpg', 'social_rank': 99.9999999991673, 'publisher_url': 'http://www.twopeasandtheirpod.com'}, {'publisher': 'My Baking Addiction', 'title': 'Pizza Dip', 'source_url': 'http://www.mybakingaddiction.com/pizza-dip/', 'recipe_id': '2ec050', 'image_url': 'http://forkify-api.herokuapp.com/images/PizzaDip21of14f05.jpg', 'social_rank': 99.99999999826605, 'publisher_url': 'http://www.mybakingaddiction.com'}, {'publisher': 'The Pioneer Woman', 'title': 'Pizza Potato Skins', 'source_url': 'http://thepioneerwoman.com/cooking/2013/04/pizza-potato-skins/', 'recipe_id': '6fab1c', 'image_url': 'http://forkify-api.herokuapp.com/images/pizza3464.jpg', 'social_rank': 99.99999999760887, 'publisher_url': 'http://thepioneerwoman.com'}, {'publisher': 'Bon Appetit', 'title': 'No-Knead Pizza Dough', 'source_url': 'http://www.bonappetit.com/recipes/2012/03/no-knead-pizza-dough', 'recipe_id': '49346', 'image_url': 'http://forkify-api.herokuapp.com/images/nokneadpizzadoughlahey6461467.jpg', 'social_rank': 99.99999999743466, 'publisher_url': 'http://www.bonappetit.com'}, {'publisher': 'Simply Recipes', 'title': 'Homemade Pizza', 'source_url': 'http://www.simplyrecipes.com/recipes/homemade_pizza/', 'recipe_id': '36453', 'image_url': 'http://forkify-api.herokuapp.com/images/pizza292x2007a259a79.jpg', 'social_rank': 99.99999998833789, 'publisher_url': 'http://simplyrecipes.com'}, {'publisher': 'Closet Cooking', 'title': 'Taco Quesadilla Pizzas', 'source_url': 'http://www.closetcooking.com/2012/08/taco-quesadilla-pizza.html', 'recipe_id': '35626', 'image_url': 'http://forkify-api.herokuapp.com/images/Taco2BQuesadilla2BPizza2B5002B4417a4755e35.jpg', 'social_rank': 99.99999998319973, 'publisher_url': 'http://closetcooking.com'}, {'publisher': 'All Recipes', 'title': 'Jay’s Signature Pizza Crust', 'source_url': 'http://allrecipes.com/Recipe/Jays-Signature-Pizza-Crust/Detail.aspx', 'recipe_id': '17796', 'image_url': 'http://forkify-api.herokuapp.com/images/237891b5e4.jpg', 'social_rank': 99.99999997246182, 'publisher_url': 'http://allrecipes.com'}, {'publisher': 'Closet Cooking', 'title': 'Avocado Breakfast Pizza with Fried Egg', 'source_url': 'http://www.closetcooking.com/2012/07/avocado-breakfast-pizza-with-fried-egg.html', 'recipe_id': '35097', 'image_url': 'http://forkify-api.herokuapp.com/images/Avocado2Band2BFried2BEgg2BBreakfast2BPizza2B5002B296294dcea8a.jpg', 'social_rank': 99.99999990783806, 'publisher_url': 'http://closetcooking.com'}, {'publisher': 'The Pioneer Woman', 'title': 'Pepperoni Pizza Burgers', 'source_url': 'http://thepioneerwoman.com/cooking/2012/10/pepperoni-pizza-burgers/', 'recipe_id': '46895', 'image_url': 'http://forkify-api.herokuapp.com/images/pizzaburgera5bd.jpg', 'social_rank': 99.99999990525365, 'publisher_url': 'http://thepioneerwoman.com'}, {'publisher': 'Closet Cooking', 'title': 'Thai Chicken Pizza with Sweet Chili Sauce', 'source_url': 'http://www.closetcooking.com/2012/02/thai-chicken-pizza-with-sweet-chili.html', 'recipe_id': '35635', 'image_url': 'http://forkify-api.herokuapp.com/images/Thai2BChicken2BPizza2Bwith2BSweet2BChili2BSauce2B5002B435581bcf578.jpg', 'social_rank': 99.99999990065892, 'publisher_url': 'http://closetcooking.com'}, {'publisher': 'The Pioneer Woman', 'title': 'One Basic Pizza Crust', 'source_url': 'http://thepioneerwoman.com/cooking/2011/09/steakhouse-pizza/', 'recipe_id': '47000', 'image_url': 'http://forkify-api.herokuapp.com/images/steakhousepizza0b87.jpg', 'social_rank': 99.99999981149679, 'publisher_url': 'http://thepioneerwoman.com'}, {'publisher': 'Two Peas and Their Pod', 'title': 'Peach, Basil, Mozzarella, & Balsamic Pizza', 'source_url': 'http://www.twopeasandtheirpod.com/peach-basil-mozzarella-balsamic-pizza/', 'recipe_id': '54491', 'image_url': 'http://forkify-api.herokuapp.com/images/peachbasilpizza6c7de.jpg', 'social_rank': 99.99999980232263, 'publisher_url': 'http://www.twopeasandtheirpod.com'}, {'publisher': 'Real Simple', 'title': 'English-Muffin Egg Pizzas', 'source_url': 'http://www.realsimple.com/food-recipes/browse-all-recipes/english-muffin-egg-pizzas-10000000663044/index.html', 'recipe_id': '38812', 'image_url': 'http://forkify-api.herokuapp.com/images/pizza_300d938bd58.jpg', 'social_rank': 99.99999978548222, 'publisher_url': 'http://realsimple.com'}, {'publisher': 'My Baking Addiction', 'title': 'Simple No Knead Pizza Dough', 'source_url': 'http://www.mybakingaddiction.com/no-knead-pizza-dough-recipe/', 'recipe_id': 'dd21dd', 'image_url': 'http://forkify-api.herokuapp.com/images/PizzaDough1of12edit5779.jpg', 'social_rank': 99.9999995838859, 'publisher_url': 'http://www.mybakingaddiction.com'}, {'publisher': 'The Pioneer Woman', 'title': 'Grilled Veggie Pizza', 'source_url': 'http://thepioneerwoman.com/cooking/2011/07/grilled-vegetable-pizza/', 'recipe_id': '47011', 'image_url': 'http://forkify-api.herokuapp.com/images/grilledveggie79bd.jpg', 'social_rank': 99.99999947603048, 'publisher_url': 'http://thepioneerwoman.com'}, {'publisher': 'My Baking Addiction', 'title': 'Spicy Chicken and Pepper Jack Pizza', 'source_url': 'http://www.mybakingaddiction.com/spicy-chicken-and-pepper-jack-pizza-recipe/', 'recipe_id': '0fb8f4', 'image_url': 'http://forkify-api.herokuapp.com/images/FlatBread21of1a180.jpg', 'social_rank': 99.99999927351223, 'publisher_url': 'http://www.mybakingaddiction.com'}, {'publisher': 'Simply Recipes', 'title': 'How to Grill Pizza', 'source_url': 'http://www.simplyrecipes.com/recipes/how_to_grill_pizza/', 'recipe_id': '36476', 'image_url': 'http://forkify-api.herokuapp.com/images/howtogrillpizzad300x20086a60e1b.jpg', 'social_rank': 99.99999704095504, 'publisher_url': 'http://simplyrecipes.com'}, {'publisher': 'The Pioneer Woman', 'title': 'PW’s Favorite Pizza', 'source_url': 'http://thepioneerwoman.com/cooking/2010/02/my-favorite-pizza/', 'recipe_id': '47161', 'image_url': 'http://forkify-api.herokuapp.com/images/4364270576_302751a2a4f3c1.jpg', 'social_rank': 99.99999689667648, 'publisher_url': 'http://thepioneerwoman.com'}, {'publisher': 'My Baking Addiction', 'title': 'Barbecue Chicken Pizza', 'source_url': 'http://www.mybakingaddiction.com/barbecue-chicken-pizza-recipe/', 'recipe_id': 'a723e8', 'image_url': 'http://forkify-api.herokuapp.com/images/BBQChickenPizza3e2b.jpg', 'social_rank': 99.9999968917598, 'publisher_url': 'http://www.mybakingaddiction.com'}, {'publisher': 'Two Peas and Their Pod', 'title': 'Avocado Pita Pizza with Cilantro Sauce', 'source_url': 'http://www.twopeasandtheirpod.com/avocado-pita-pizza-with-cilantro-sauce/', 'recipe_id': '54388', 'image_url': 'http://forkify-api.herokuapp.com/images/avocadopizzawithcilantrosauce4bf5.jpg', 'social_rank': 99.99999665701256, 'publisher_url': 'http://www.twopeasandtheirpod.com'}, {'publisher': "What's Gaby Cooking", 'title': 'Pizza Monkey Bread', 'source_url': 'http://whatsgabycooking.com/pizza-monkey-bread/', 'recipe_id': 'ead4e0', 'image_url': 'http://forkify-api.herokuapp.com/images/PizzaMonkeyBread67f8.jpg', 'social_rank': 99.99999570141472, 'publisher_url': 'http://whatsgabycooking.com'}, {'publisher': 'The Pioneer Woman', 'title': 'Supreme Pizza Burgers', 'source_url': 'http://thepioneerwoman.com/cooking/2012/10/supreme-pizza-burgers/', 'recipe_id': '46892', 'image_url': 'http://forkify-api.herokuapp.com/images/burger53be.jpg', 'social_rank': 99.99999283988569, 'publisher_url': 'http://thepioneerwoman.com'}, {'publisher': 'Closet Cooking', 'title': 'Balsamic Strawberry and Chicken Pizza with Sweet Onions and Smoked Bacon', 'source_url': 'http://www.closetcooking.com/2012/07/balsamic-strawberry-and-chicken-pizza.html', 'recipe_id': '35128', 'image_url': 'http://forkify-api.herokuapp.com/images/Strawberry2BBalsamic2BPizza2Bwith2BChicken252C2BSweet2BOnion2Band2BSmoked2BBacon2B5002B300939d125e2.jpg', 'social_rank': 99.99998682928603, 'publisher_url': 'http://closetcooking.com'}]



    for wid in myFrame.winfo_children(): # deleting previous list of search
        wid.destroy()

    cnt = 0
    for d in data: # to
        if(cnt==8):
            break
        frame3 = Frame(myFrame, width=600, height=100, bg='blue', bd=4)
        frame3.pack()

        imgUrl = d['image_url']
        u = urlopen(imgUrl)
        my_picture = io.BytesIO(u.read())

        image = Image.open(my_picture)
        resize = image.resize((120, 90))
        img = ImageTk.PhotoImage(resize)
        labelImg = Label(frame3, image=img)
        labelImg.image = img
        labelImg.place(x=5, rely=0.05, relwidth=0.2, relheight=0.9)

        labelTitle = Label(frame3, text=d['title'], bg='blue', fg='white')
        labelTitle.place(x=200, rely=0.2)

        labelPub = Label(frame3, text=d['publisher'], bg='blue', fg='white')
        labelPub.place(x=200, rely=0.5)

        moreInfo = Button(frame3, text='More Info', bg='#3498DB',
                          command=partial(newFrame, d['recipe_id'])) #partial is used to call a fuction and if theres a parameter
        moreInfo.place(relwidth=0.2, relx=0.7, rely=0.45)

        Frame(myFrame, height=5, width=600, pady=10, bg='white').pack()
        cnt+=1


root = Tk()
canvas = Canvas(root, height=768, width=1366, bg='#263D42')
canvas.pack()

frame1 = LabelFrame(root, bg='#a855ff')
frame2 = LabelFrame(root, bg='#edaaff')
frame1.place(relheight=1.0, relwidth=0.5, x=0, y=0)
frame2.place(relheight=1.0, relwidth=0.5, relx=0.5, y=0)

searchBox = Text(frame2, height=1, bg='#E5E7E9')
searchBox.config(font=("Courier", 18))
searchBox.place(relwidth=0.6, relx=0.2, rely=0.04)
searchBox.insert(END, 'Search...')

myFont = font.Font(size=14)
submit = Button(frame2, text='Find', fg='white',
                bg='#3498DB', command=findBtn, bd=4)
submit['font'] = myFont
submit.place(relwidth=0.2, relx=0.4, rely=0.1)

frame3 = LabelFrame(frame2, bg='#6872fd')
frame3.place(relheight=0.8, relwidth=0.8, relx=0.05, rely=0.17)

# Below is a procedure to add a scroll to a frame since we cannot add directly
myCanvas = Canvas(frame3)
myCanvas.place(relwidth=1.0, relheight=1.0)

scrollbar = Scrollbar(frame3, orient='vertical', command=myCanvas.yview)
scrollbar.pack(side=RIGHT, fill='y')

myCanvas.configure(yscrollcommand=scrollbar.set)

myCanvas.bind('<Configure>', lambda e: myCanvas.configure(
    scrollregion=myCanvas.bbox('all')))

myFrame = Frame(myCanvas)
myCanvas.create_window((0, 0), window=myFrame, anchor='nw')
# procedure end

#Home Screen Image
homeCanvas = Canvas(frame1)
homeCanvas.place( relwidth = 1.0, relheight = 1.0, relx=0.0, rely=0.0)

homeImage = Image.open("./src/side1.jpg")
resize1 = homeImage.resize((800, 800))

img = ImageTk.PhotoImage(resize1)
homeCanvas.create_image(0,0, anchor=NW, image=img)
#Home Screen Image

#Error Label
strVar = StringVar()
strVar.set("")
erLabel = Label(frame2,textvariable=strVar, bg='#edaaff')
erLabel.place( relx=0.7, rely=0.12)
#Error Label

# scroll does'nt work if content is added after mainloop call so create space for it
for i in range(8):
    Frame(myFrame, height=100, width=600, pady=10, padx=10, bg='white').pack()

# main loop
root.mainloop()
#home()