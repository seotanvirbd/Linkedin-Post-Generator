import customtkinter as ctk 
from few_shot import FewShotPosts
from post_generator import generate_post
from typing import List
import random



class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
         # Configure appearance
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        
        # Configure window
        self.title("LinkedIn Post Generator")
        self.geometry("900x700")
        
        # Configure grid layout (3x3)
        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure((0, 1,2,3), weight=1)
        
        # Initialize data
        self.fs = FewShotPosts()
        self.LENGTH_OPTIONS: List[str] = ["Short", "Medium", "Long"]
        self.LANGUAGE_OPTIONS: List[str] = ["English", "Hinglish"]
        
    # create_widgets:  
        # Title
        self.title_label = ctk.CTkLabel(self,text="LinkedIn Post Generator",font=("Helvetica", 28, "bold"))
        
        # Create frames for each section
        self.input_frame = ctk.CTkFrame(self)
        self.input_frame.grid_columnconfigure((0, 1, 2), weight=1)
        
        # Topic selection
        self.topic_label = ctk.CTkLabel(self.input_frame,text="Topic:",font=("Helvetica", 16))
        self.topic_var = ctk.StringVar(value=self.fs.get_tags()[0])
        self.topic_menu = ctk.CTkOptionMenu(self.input_frame,values= self.fs.get_tags(),variable=self.topic_var,width=250)
        
        # Length selection
        self.length_label = ctk.CTkLabel(self.input_frame,text="Length:",font=("Helvetica", 16))
        self.length_var = ctk.StringVar(value=self.LENGTH_OPTIONS[0])
        self.length_menu = ctk.CTkOptionMenu(self.input_frame,values=self.LENGTH_OPTIONS,variable=self.length_var,width=250)
        
        # Language selection
        self.language_label = ctk.CTkLabel(self.input_frame,text="Language:",font=("Helvetica", 16))
        self.language_var = ctk.StringVar(value=self.LANGUAGE_OPTIONS[0])
        self.language_menu = ctk.CTkOptionMenu(self.input_frame,values=self.LANGUAGE_OPTIONS,variable=self.language_var,width=250)
        
        # Generate button
        self.generate_button = ctk.CTkButton(self,text="Generate Post",command=self._generate_post,width=200,height=50,font=("Helvetica", 16, "bold"))
        
        # Output text area
        self.output_text = ctk.CTkTextbox(self,width=800,height=400,font=("Helvetica", 14))
        
        # Status label
        self.status_label = ctk.CTkLabel(self,text="",font=("Helvetica", 14))
        
    # setup_grid_layout:
        # Place title
        self.title_label.grid(row=0, column=0, columnspan=3, pady=(20, 0))
        
        # Place input frame and its contents
        self.input_frame.grid(row=1, column=0, columnspan=3, padx=20, pady=20, sticky="nsew")
        
        # Topic section
        self.topic_label.grid(row=0, column=0, padx=10, pady=(10, 5))
        self.topic_menu.grid(row=1, column=0, padx=10, pady=(0, 30))
        
        # Length section
        self.length_label.grid(row=0, column=1, padx=10, pady=(10, 5))
        self.length_menu.grid(row=1, column=1, padx=10, pady=(0, 30))
        
        # Language section
        self.language_label.grid(row=0, column=2, padx=10, pady=(10, 5))
        self.language_menu.grid(row=1, column=2, padx=10, pady=(0, 30))
        
        # Place generate button
        self.generate_button.grid(row=2, column=0, columnspan=3, pady=20)
        
        # Place output text area
        self.output_text.grid(row=3, column=0, columnspan=3, padx=20, pady=(0, 20), sticky="nsew")
        
        # Place status label
        self.status_label.grid(row=4, column=0, columnspan=3, pady=(0, 20))
    def _generate_post(self):
        # show loading status
        self.status_label.configure(text="Generating post...")
        self.generate_button.configure(state="disabled")
        self.output_text.delete("1.0", "end")
        self.update()
        try:    
            # Get selected values
            topic = self.topic_var.get()
            length = self.length_var.get()
            language = self.language_var.get()
            
            # Generate post
            post = generate_post(length, language, topic)
            
            # Update output
            self.output_text.delete("1.0", "end")
            self.output_text.insert("1.0", post)
            self.status_label.configure(text="Post generated successfully!")
        except Exception as e:
            self.output_text.insert("1.0", f"Error generating post: {str(e)}")
            self.status_label.configure(text="Error occurred while generating post")
        finally:
            self.generate_button.configure(state="normal")
    
app = App()
app.mainloop()
