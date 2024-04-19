from tkinter import Tk, filedialog, Frame, Button, Label
from tkinter import ttk
from PIL import Image, ImageTk
import os
import rawpy
import imageio

class CR3Viewer:
    def __init__(self):
        self.root = Tk()
        self.root.title("CR3 Viewer")

        self.top_frame = Frame(self.root)
        self.top_frame.pack(side="top", fill="x")

        self.new_button = Button(self.top_frame, text="New", command=self.open_files)
        self.new_button.pack(side="left")

        self.save_button = Button(self.top_frame, text="Save", command=self.save_image)
        self.save_button.pack(side="left")

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill='both')

    def open_files(self):
        file_paths = filedialog.askopenfilenames(title="Select CR3 Files", filetypes=[("CR3 files", "*.cr3")])
        for file_path in file_paths:
            self.add_tab(file_path)

    def add_tab(self, file_path):
        frame = Frame(self.notebook)
        self.notebook.add(frame, text=os.path.basename(file_path))
        self.update_image(frame, file_path)

    def update_image(self, frame, file_path):
        with rawpy.imread(file_path) as raw:
            rgb = raw.postprocess()
            image = Image.fromarray(rgb)
            image.thumbnail((800, 800), Image.ANTIALIAS)
        tkimage = ImageTk.PhotoImage(image)
        label = Label(frame, image=tkimage)
        label.image = tkimage
        label.pack()

    def save_image(self):
        current_tab_index = self.notebook.index(self.notebook.select())
        frame = self.notebook.nametowidget(self.notebook.select())
        file_path = self.notebook.tab(current_tab_index, "text")

        cr3_file_path = os.path.join("path/to/your/cr3/files", file_path)
        save_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png")])
        if save_path:
            with rawpy.imread(cr3_file_path) as raw:
                rgb = raw.postprocess()
            imageio.imsave(save_path, rgb)
            print(f"Image saved as {save_path}")

if __name__ == "__main__":
    viewer = CR3Viewer()
    viewer.root.mainloop()