import tkinter as tk

class PDFApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Secure PDF Viewer")
        
        self.label = tk.Label(master, text="Enter Password:")
        self.label.pack()

        self.password_entry = tk.Entry(master, show='*')
        self.password_entry.pack()

        self.open_button = tk.Button(master, text="Open PDF", command=self.open_pdf)
        self.open_button.pack()

    def open_pdf(self):
        password = self.password_entry.get()
       
if __name__ == "__main__":
    root = tk.Tk()
    app = PDFApp(root)
    root.mainloop()
    