import tkinter as tk


splash = tk.Tk()        # Create an instance of tkinter for the main menu
splash.geometry('900x700')
splash.resizable(False, False)
splash.title("Welcome!")
splash.config(bg="#2b8e99")

startquiz_btn = tk.Button(splash, text="Medium", font=("Helvetica", 40), width=36, bg="#b38878",
                       command=lambda: displayQuiz("page1"))
startquiz_btn.pack(side="top", pady=20)

#Create landing page with 2 buttons. 'Begin Quiz' and 'Read Some Facts'


#Define buttons functionality

def change_clr(button, color):
    button.configure(background=color)

#Create Facts page, where you can scroll through facts or return to landing page


#Quiz page 1 asks first question with buttons to choose an answer
def displayQuiz(page):
    global window
    window = tk.Toplevel(splash)

    window.geometry('900x700')
    window.resizable(False,False)
    window.title("Carbon Quiz")
    window.config(bg="#2b8e99")
#Each page asks a relevant question and uses the answer to add to footprint_s
#'footprint_s' is a score for how big their footprint is


#At the end of quiz, an animation shows how user compares to world average. Button for returning to splash

def run():
    

if __name__ == '__main__':
    run()