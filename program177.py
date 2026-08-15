from tkinter import*
from time import sleep;
def aprilfool():
    label.config(text="Your Your account no. *************** just debited ₹9999 to ****************.")
    #sleep(10);
    #label.config(text="Aprill Fool!!!!!!!!!")

    
root = Tk();
root.title("My Window")
root.geometry("3000x1500");

label = Label(root, text = "Hello World");
label.pack(pady=100);
Button(root, text="Press to do something that is maybe risky.", command=aprilfool).pack()
root.mainloop();
