from tkinterdnd2 import DND_FILES, TkinterDnD
from tkinter import filedialog, Frame, Button, Label
from tkinter import ttk
from PIL import Image, ImageTk
import os
import rawpy
import imageio

class CR3Viewer:
    def __init__(self):
        self.root = TkinterDnD.Tk()
        self.root.title("CR3 Viewer")

        self.top_frame = Frame(self.root)
        self.top_frame.pack(side="top", fill="x")

        self.new_button = Button(self.top_frame, text="New", command=self.open_files)
        self.new_button.pack(side="left")

        self.save_button = Button(self.top_frame, text="Save", command=self.save_image)
        self.save_button.pack(side="left")

        # Add a close button to the top frame
        self.close_button = Button(self.top_frame, text="Close", command=self.close_current_tab)
        self.close_button.pack(side="left")

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill='both')

        self.root.bind("<Right>", self.switch_tab_right)
        self.root.bind("<Left>", self.switch_tab_left)
        self.root.bind("<Control-s>", self.save_image)

        # Enable drag and drop
        self.root.drop_target_register(DND_FILES)
        self.root.dnd_bind('<<Drop>>', self.on_drop)

    def open_files(self, file_paths=None):
        if file_paths is None:
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

    def save_image(self, event=None):
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

    def switch_tab_right(self, event):
        current_tab_index = self.notebook.index(self.notebook.select())
        next_tab_index = (current_tab_index + 1) % self.notebook.index("end")
        self.notebook.select(next_tab_index)

    def switch_tab_left(self, event):
        current_tab_index = self.notebook.index(self.notebook.select())
        prev_tab_index = (current_tab_index - 1) % self.notebook.index("end")
        self.notebook.select(prev_tab_index)

    def on_drop(self, event):
        file_paths = self.root.tk.splitlist(event.data)
        self.open_files(file_paths)

    def close_current_tab(self):
        """Closes the currently selected tab in the notebook."""
        current_tab = self.notebook.select()
        if current_tab:
            self.notebook.forget(current_tab)

if __name__ == "__main__":
    viewer = CR3Viewer()
    viewer.root.mainloop()
