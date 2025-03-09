from PIL import Image, ImageTk
import io
import tkinter as tk
import os

class ImageGridWidget:
    def __init__(self, images):
        self.images = images
        self.selected_images = []
        self.root = None
        self.save_path = os.path.join(os.path.expanduser("~"), 'OneDrive','Imágenes','genAI')

        
    def toggle_selection(self, img_data, img_frame):
        """Toggle selection of an image by adding/removing a halo effect."""
        if img_data in self.selected_images:
            self.selected_images.remove(img_data)
            img_frame.config(bg="white")  # Reset background color
        else:
            self.selected_images.append(img_data)
            img_frame.config(bg="blue")  # Add blue halo effect
        print(f"Selected images: {len(self.selected_images)}")  # Debugging

    def save_selected(self, window):
        """Save selected images and close the window."""
        if not self.selected_images:
            print("No images selected to save.")
            return
        
        for index, img_data in enumerate(self.selected_images):
            with open(os.path.join('./Img', f"Image_{index + 1}.jpeg"), "wb") as img_file:
                img_file.write(img_data)
        print(f"Saved {len(self.selected_images)} images.")
        window.destroy()

    def display_images(self):
        """Display images in a Tkinter window for selection."""
        self.root = tk.Tk()
        self.root.title("Select Images")
        self.root.geometry("600x750")  # Larger window size

        # Create a frame for image display
        frame = tk.Frame(self.root)
        frame.pack(padx=10, pady=13)

        # Create a grid for images
        for index, img_data in enumerate(self.images):
            img = Image.open(io.BytesIO(img_data))  # Open image from bytes
            img = img.resize((300, 300), Image.LANCZOS)  # Increase image size

            # Convert to PhotoImage for Tkinter
            photo = ImageTk.PhotoImage(img)

            # Create a frame for each image
            img_frame = tk.Frame(frame, width=320, height=320, bg="white", highlightthickness=2)
            img_frame.grid(row=index // 2, column=index % 2, padx=10, pady=10)  # Adjust grid placement

            # Create a label for the image
            label = tk.Label(img_frame, image=photo, bg="white")
            label.image = photo  # Keep a reference to avoid garbage collection
            label.pack(padx=5, pady=5)

            # Bind click event to both the frame and the image label
            img_frame.bind("<Button-1>", lambda event, data=img_data, frame=img_frame: self.toggle_selection(data, frame))
            label.bind("<Button-1>", lambda event, data=img_data, frame=img_frame: self.toggle_selection(data, frame))

        # Save button with styling
        save_btn = tk.Button(self.root, text="Save Selected Images", command=lambda: self.save_selected(self.root), bg="#A0EBA0", relief="flat", borderwidth=0)
        save_btn.pack(pady=10)
        save_btn.bind("<Enter>", lambda e: save_btn.config(bg="#90E390"))  # Hover effect
        save_btn.bind("<Leave>", lambda e: save_btn.config(bg="#A0EBA0"))  # Leave effect

        self.root.mainloop()
