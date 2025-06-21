from tkinter import *
from PIL import Image, ImageTk
import webbrowser

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="DEVELOPER", font=("Sketchy In Snow", 35, "bold"), bg="darkgreen", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Background Image
        bg_img = Image.open(r"collage imgs\developerImg.jpg")
        bg_img = bg_img.resize((1530, 720), Image.LANCZOS)
        self.photoimg_bg = ImageTk.PhotoImage(bg_img)

        bg_label = Label(self.root, image=self.photoimg_bg)
        bg_label.place(x=0, y=55, width=1530, height=720)

        # Developer 1 Frame
        self.create_developer_frame(
            parent=bg_label,
            x=1000,
            y=0,
            image_path=r"collage imgs\devPic.jpg",
            name="Arun Tiwari",
            role="Aspiring Data Analyst",
            college="BBDNIIT, Lucknow",
            github="https://github.com/aruntiwari-dev",
            linkedin="https://www.linkedin.com/in/arun-tiwari6930"
        )

    def create_developer_frame(self, parent, x, y, image_path, name, role, college, github, linkedin):
        def callback(url):
            webbrowser.open_new(url)

        frame = Frame(parent, bd=2, bg="white")
        frame.place(x=x, y=y, width=500, height=300)

        # Developer Image
        img = Image.open(image_path)
        img = img.resize((200, 200), Image.LANCZOS)
        photo = ImageTk.PhotoImage(img)
        label_img = Label(frame, image=photo)
        label_img.image = photo  # keep a reference
        label_img.place(x=300, y=0, width=200, height=200)

        # Developer Text Info
        Label(frame, text=f"Hello, this is {name}", font=("times new roman", 15, "bold"), bg="white").place(x=10, y=50)
        Label(frame, text=f"I'm an {role}", font=("times new roman", 15, "bold"), bg="white").place(x=10, y=100)
        Label(frame, text=f"A student of {college}", font=("times new roman", 15, "bold"), bg="white").place(x=10, y=150)

        github_label = Label(frame, text="My GitHub", fg="blue", cursor="hand2", bg="white")
        github_label.place(x=10, y=200)
        github_label.bind("<Button-1>", lambda e: callback(github))

        linkedin_label = Label(frame, text="My LinkedIn", fg="blue", cursor="hand2", bg="white")
        linkedin_label.place(x=10, y=230)
        linkedin_label.bind("<Button-1>", lambda e: callback(linkedin))


if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
