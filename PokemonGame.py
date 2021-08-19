#libraries being used in this game.
import glob
import random
import PIL.Image
from tkinter import *
from PIL import Image, ImageTk


#@total: the total number of questions.
#@correctNum : the number of correct answer.
#@dic_index: To keep in track of the index for dictionary_lookup.
total = 0
correctNum = 0
dic_index = 0

#Setting up the screen size of width x height.
#bg : Background color.
#wm_title : Title of the screen.
root = Tk()
root['bg'] ='light sky blue'
root.wm_title("Pokemon Quiz")
root.geometry("600x400")

#Setting up the frame for question, status, and actions (buttons/choices).
questionsFrame = Frame(root)
Click4Choice = Frame(root)
statusFrame = Frame(root)


#Display a question on the window screen blod
#bg: background color 
#fg = the text line color
questionLabel = Label(questionsFrame,font = 'Helvetica 10 bold')
questionLabel['text'] = "Pick a choice that represent the name of the Pokemon above: "
questionLabel['bg'] = 'plum1'
questionLabel['fg'] = 'red'
questionLabel.pack(side = TOP,fill = X)

#pack : declare the postion of the widgets
#Setting up the button for 4 different pokemon names(One of them is the answer)
Pokemon_choice1 = Button(Click4Choice, text= "")
Pokemon_choice1.pack(side = LEFT, expand= YES, fill = X)

Pokemon_choice2 = Button(Click4Choice, text= "")
Pokemon_choice2.pack(side = LEFT, expand= YES, fill = X)

Pokemon_choice3 = Button(Click4Choice, text= "")
Pokemon_choice3.pack(side = RIGHT, expand= YES, fill = X)

Pokemon_choice4 = Button(Click4Choice, text= "")
Pokemon_choice4.pack(side = RIGHT, expand= YES, fill = X)

#Setting up the display to show the result of whether the user got it correct or wrong
status_result = Label(statusFrame, text = "")
status_result.pack(side = BOTTOM,expand = YES, fill = X)

#Setting up the isplay the user's score
current_score = Label(statusFrame, text = f'Your current score is : {correctNum} / {total}', bg= 'gold')
current_score.pack(side= BOTTOM,expand= YES,fill = X)


##Setting up the display for final result of the user in percentage towards the end
final_score = Label(statusFrame, text = " ")
final_score.pack(side = BOTTOM,expand= YES,fill =X )





#This function will ignore the folder name ("Pokemon_image/"). Which has 13 index of the string.
#It will also ignore the string of ".jpg" or ".png".
#@ImagePath: is the image path. Ex : Pokemon_image\Abra.jpg -> will give you Abra image.
#@Pokemon_name: return pokemon name from the image(.png or .jpg).
def getImagePokemon_name(ImagePath):
    Pokemon_name = ""
    for x in range(0,len(ImagePath)):
        if x<=13 and x>=0:
            pass
        elif ImagePath[x] == ".":
            return Pokemon_name
        else:
            Pokemon_name += ImagePath[x]
    return Pokemon_name

#glob.glob will returns a list of (images/files) paths to @Image_list.
Image_list = glob.glob('Pokemon_image/*.*')




#@Pokemon_name : a list will restore all the Pokemon name corresponding to it's image paths. 
Pokemon_name = []
for i in range(0, len(Image_list)):
    image_path = Image_list[i]
    Pokemon_name.append(getImagePokemon_name(image_path))


#@dictionary: hash_map that store key(image_path) with value(string of the path) and another key(answer)  with value(Pokemon_name).
#Then dictionary will be added into the list of dictionary_lookup.
#@dictionary_lookup: a list of dictionary that stores the Pokemon_name and image_path into the same index.
dictionary_lookup = []
for x in range(0 , len(Image_list)):
    dictionary = {}
    dictionary["image_path"] = Image_list[x]
    dictionary["answer"] = Pokemon_name[x]
    dictionary_lookup.append(dictionary)


#@current_pic: opens the very first image.
#@resize_img: resize the image into better fit of the window tk.
#@new_curr_pic = load up the image.
current_pic = Image.open(Image_list[0])
resize_img = current_pic.resize((300,225),Image.ANTIALIAS)
new_curr_pic = ImageTk.PhotoImage(resize_img)

#@my_label: The screen will display the image on top .
my_label = Label(root, image = new_curr_pic)
my_label.pack(side = TOP)



#@list_num: a list that contains 4 random choices for user.
#Fuction will return false if the list contains less than 4 choices.
#Else return true.
def fourListCheck(list_num):
    list_size = len(list_num)-1
    if list_size >=0 and list_size <=2:
        return False
    else:
        return True



#@Pokemon_index: is the index from dictionary_lookup list of dictionary
#@Pokemon_name: The list of name for pokemon names
#@list_num : a list of dictionary containning key and value
def random_4choice_generator(Pokemon_index):
    list_num = []
    hash_map = {"True": Pokemon_index}
    list_num.append(hash_map)
    for x in range(3):
        Original_pokemon_index = random.randint(0,len(Pokemon_name)-1)
        hash_map = {"False": Original_pokemon_index}
        list_num.append(hash_map)
    if not fourListCheck(list_num):
        random_4choice_generator(Pokemon_index)
    else:
        return list_num

#Display exit button towards the end of the game.
#Click on exit button will close the screen / game.
def no_more_image():
    exit_game = Button(root)
    exit_game['text'] = "Exit"
    exit_game['fg'] = 'red'
    exit_game['command'] = root.destroy
    exit_game.pack(side = BOTTOM,expand=YES,fill =X )



#Get the very next image from random corresponding with it is Pokemon_name in the dictionary_lookup.
#Display 4  different choices button for user to answer the image from the screen.
#Only one of the choice will be a correct answer.
def getNextImage():
    global dic_index

    #If the the dictionary_lookup list is empty, then display user's final score in percentage.
    #All of the choice buttons will be disable from clicking.
    if len(dictionary_lookup) == 0:
        final_Score = correctNum/ total
        final_score['text'] = f"Quiz ended. Your final score is: {round(final_Score*100)}%. You may click on 'Exit' now"
        Pokemon_choice1['state'] = DISABLED
        Pokemon_choice2['state'] = DISABLED
        Pokemon_choice3['state'] = DISABLED
        Pokemon_choice4['state'] = DISABLED
        no_more_image()
    
    else:
        #Base Case when there is the size of one.
        #@random_image_generator: The index of the list for image_path and pokemon name.
        if len(dictionary_lookup) == 1:
            random_image_generator = 0
            image_direction= dictionary_lookup[random_image_generator]['image_path']
        #Else there's more than size of one in the list of dictionary_lookup.
        #@random_image_generator: Will get the index randomly from the list size.
        else:   
            random_image_generator = random.randint(0,len(dictionary_lookup)-1)
            image_direction= dictionary_lookup[random_image_generator]['image_path']

        # @current_pic: opens the very next image.
        # @resize_img: resize the image into better fit of the window tk.
        # @new_curr_pic = load up the image.
        current_pic = Image.open(image_direction)
        resize_img = current_pic.resize((300,225),Image.ANTIALIAS)
        new_curr_pic = ImageTk.PhotoImage(resize_img)
        my_label.config(image=new_curr_pic)
        my_label.image= new_curr_pic
        
        #@list_choice : a list that will store dictionary containning one random index from dictionary_lookup and 3 from Pokemon_name.
        #@The one index from dictionary_lookup will True as a key.
        list_choice = []
        list_choice = random_4choice_generator(Pokemon_index=random_image_generator)

        #@answer_to_image: is the pokemon name corresponding to the image.
        answer_to_image = ""

        #@random_pick: randomly being picked from the one of the four choice as the answer.
        #Afterward it will be removed from the list.
        #Repeat this process until all of the list_choice list is empty.
        random_pick = random.choice(list_choice)
        key = list(random_pick.keys())
        boolvalue = key[0]
        if boolvalue == "True":
            IndexNum = random_pick["True"]
            answer_to_image = dictionary_lookup[IndexNum]['answer']
            Pokemon_choice1['text'] = dictionary_lookup[IndexNum]['answer']
        else:
            IndexNum = random_pick["False"]
            Pokemon_choice1['text'] = Pokemon_name[IndexNum]
        list_choice.remove(random_pick)


        random_pick = random.choice(list_choice)
        key = list(random_pick.keys())
        boolvalue = key[0]
        if boolvalue == "True":
            dic_index = random_pick["True"]
            answer_to_image = dictionary_lookup[dic_index]['answer']
            Pokemon_choice2['text'] = dictionary_lookup[dic_index]['answer']
        else:
            IndexNum = random_pick["False"]
            Pokemon_choice2['text'] = Pokemon_name[IndexNum]
        list_choice.remove(random_pick)

        random_pick = random.choice(list_choice)
        key = list(random_pick.keys())
        boolvalue = key[0]
        if boolvalue == "True":
            dic_index = random_pick["True"]
            answer_to_image = dictionary_lookup[dic_index]['answer']
            Pokemon_choice3['text'] = dictionary_lookup[dic_index]['answer']
        else:
            IndexNum = random_pick["False"]
            Pokemon_choice3['text'] = Pokemon_name[IndexNum]
        list_choice.remove(random_pick)


        random_pick = random.choice(list_choice)
        key = list(random_pick.keys())
        boolvalue = key[0]
        if boolvalue == "True":
            dic_index = random_pick["True"]
            answer_to_image = dictionary_lookup[dic_index]['answer']
            Pokemon_choice4['text'] = dictionary_lookup[dic_index]['answer']
        else:
            IndexNum = random_pick["False"]
            Pokemon_choice4['text'] = Pokemon_name[IndexNum]
        list_choice.remove(random_pick)

        #Removing the previous current image being displayed to prevent same image shown up twice
        dictionary_lookup.remove(dictionary_lookup[dic_index])

        #To check if the user clicked the right answer that matches the dictionary_lookup pokemon name
        if Pokemon_choice1['text'] == answer_to_image:
            Pokemon_choice1['command'] = CorrectAnswer
            Pokemon_choice2['command'] = IncorrectAnswer
            Pokemon_choice3['command'] = IncorrectAnswer
            Pokemon_choice4['command'] = IncorrectAnswer
        elif Pokemon_choice2['text'] == answer_to_image:
            Pokemon_choice1['command'] = IncorrectAnswer
            Pokemon_choice2['command'] = CorrectAnswer
            Pokemon_choice3['command'] = IncorrectAnswer
            Pokemon_choice4['command'] = IncorrectAnswer
        elif Pokemon_choice3['text'] == answer_to_image:
            Pokemon_choice1['command'] = IncorrectAnswer
            Pokemon_choice2['command'] = IncorrectAnswer
            Pokemon_choice3['command'] = CorrectAnswer
            Pokemon_choice4['command'] = IncorrectAnswer
        else:
            Pokemon_choice1['command'] = IncorrectAnswer
            Pokemon_choice2['command'] = IncorrectAnswer
            Pokemon_choice3['command'] = IncorrectAnswer
            Pokemon_choice4['command'] = CorrectAnswer

#Update the window display with new status_result and the current score.
#@total: total # of questions answered.
#@correctNum : number of correct answers, the user answered.
#@getNextImage : continue getting the next image
def CorrectAnswer():
    global total, correctNum
    total +=1
    correctNum +=1
    status_result['text'] = "That's a correct answer"
    status_result['bg'] = 'light green'
    current_score['text'] = f'Your current score is : {correctNum} / {total} '
    current_score['bg'] = 'gold'
    getNextImage()

#Update the window display with new status_result and the current score.
#@total: total # of questions answered.
#@status_result['bg'] = 'red' : Display a red highlight for each time the user answered incorrect answer.
#@getNextImage : continue getting the next image
def IncorrectAnswer():
    global total, correctNum
    total +=1
    status_result['text'] = "That's a incorrect answer"
    status_result['bg'] = 'red'
    current_score['text'] = f'Your current score is: {correctNum} / {total} '
    current_score['bg'] = 'gold'
    getNextImage()

#Declare the postion of the widgets
questionsFrame.pack(expand = YES, fill = BOTH)
Click4Choice.pack(expand = YES, fill = BOTH)
statusFrame.pack(expand = YES, fill = BOTH)

#Get the very next image
getNextImage()
root.mainloop()
