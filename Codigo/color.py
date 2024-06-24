import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np
import cv2
from skimage.feature import graycomatrix, graycoprops

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Visualizador de Características de Haralick')
        self.geometry('800x600')
        self.create_widgets()

    def create_widgets(self):
        self.btn_load = tk.Button(self, text="Carregar Imagem", command=self.load_image)
        self.btn_load.pack()

        self.btn_features = tk.Button(self, text="Calcular Características de Haralick", command=self.calculate_haralick)
        self.btn_features.pack()

        self.lbl_image = tk.Label(self)
        self.lbl_image.pack()

        self.txt_features = tk.Text(self, height=10, width=50)
        self.txt_features.pack()

    def load_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image = Image.open(file_path)
            self.photo_image = ImageTk.PhotoImage(self.image)
            self.lbl_image.configure(image=self.photo_image)

    def calculate_haralick(self):
        if hasattr(self, 'image'):
            image_np = np.array(self.image.convert('L')) 
            features = self.haralick_features(image_np)
            feature_text = "\n".join([f"{k}: {v}" for k, v in features.items()])
            self.txt_features.delete('1.0', tk.END)
            self.txt_features.insert(tk.END, feature_text)
        else:
            messagebox.showerror("Erro", "Carregue uma imagem primeiro.")

    def haralick_features(self, image):
        distances = [1]
        angles = [0, np.pi/4, np.pi/2, 3*np.pi/4]
        glcm = graycomatrix(image, distances=distances, angles=angles, levels=256, symmetric=True, normed=True)
        properties = ['contrast', 'dissimilarity', 'homogeneity', 'energy', 'correlation', 'ASM']
        features = {prop: graycoprops(glcm, prop)[0, 0] for prop in properties}
        return features

if __name__ == "__main__":
    app = Application()
    app.mainloop()
