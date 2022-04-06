from cgitb import text
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

class App(Tk):
    def __init__(self):
        super().__init__()
        self.minsize(720, 480)
        self.title("Image Watermark App")
        self.config(bg="#191919")
        #----LABELS----#
        self.label_0 = Label(text="Select an Image", bg="#191919", fg="#F7F7F7")
        self.label_0.place(x=150, y=150)
        self.label_1 = Label(text="Enter some text", bg="#191919", fg="#F7F7F7")
        self.label_1.place(x=150, y=200)
        #----BUTTONS----#
        self.browse_button = Button(text="Browse", width=10, command=self.browse_files, bg="#333333", fg="#F7F7F7")
        self.browse_button.place(x=400, y=150)
        self.text_entry = Entry(width=37)
        self.text_entry.place(x=250, y=200)
        self.save_button = Button(text="Save", width=10, command=self.save_file, bg="#333333", fg="#F7F7F7")
        self.save_button.place(x=300, y=250)

    def browse_files(self):
        self.filename = filedialog.askopenfilename(initialdir="/", title="Select an Image", filetypes=(("Image files", "*.jpg"),("All files", ".*")))

        if self.filename:
            try:
                self.label_0.config(text="File Opened Successfully!!", bg="#191919", fg="#008000")
            except:
                messagebox.showerror(title="Oops!!", message="Failed to Open Image")

    def save_file(self):
        image = self.filename
        image = Image.open(image)
        if image:
            try:
                watermark_image = image.copy()
                draw = ImageDraw.Draw(watermark_image)
                font = ImageFont.truetype("Arial.ttf", 40)
                if self.text_entry.get():
                    text = self.text_entry.get()
                    draw.text((10, 10), text, font=font, fill=(0, 0, 0))
                    watermark_image.save("./watermarked_image.jpg")
                else:
                    messagebox.showerror(title="Oops!!", message="Enter text First")
                
            except OSError:
                messagebox.showerror(title="Oops!!", message="Could not find file path")

app = App()
app.mainloop()