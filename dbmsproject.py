import os
import io
import openai
import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import messagebox
import PyPDF2
import mysql.connector 
from pytube import YouTube
from io import BytesIO
from PIL import Image, ImageTk
import requests
import webbrowser
import tkinter.font as tkFont
from openai import OpenAI
api_key="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"
#client=OpenAI(api_key = os.environ.get("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"))



class PDFViewerApp:
    def __init__(self, root,api_key=None):
        self.root = root
        self.api_key=api_key
        if api_key:
            openai.api_key=api_key
        self.root.title("DBMS Project")
        self.thumbnail_photos = []
        self.subject_var = tk.StringVar()
        self.grade_var = tk.StringVar()
        self.topic_var = tk.StringVar()


        self.create_widgets()
        self.main_frame = ttk.Frame(root)
        self.main_frame.grid(row=0, column=1, padx=10, pady=10)
        self.left_frame = tk.Frame(self.main_frame, background="black")
        self.video_label = ttk.Label(self.left_frame, text="Resources",font=("Helvetica",12))
        self.video_label.pack(padx=10, pady=10)

        # Create a Canvas to embed the video
        self.canvas = tk.Canvas(self.left_frame, width=300, height=750)
        self.canvas.pack(padx=10, pady=10)

        # Embed a YouTube video (replace the URL with your own)
        video_urls=[("https://www.youtube.com/watch?v=qRE0WicGz4I","Quickly make an Efficient Study Schedule!"),
                    ("https://www.youtube.com/watch?v=N5R-RX4fbbk","Know HOW to study before WHAT to study"),
                    ("https://www.youtube.com/watch?v=dXoizV_0QIc", "The Parents' Guide to Homeschooling")]
        self.embed_youtube_videos(video_urls)

        self.left_frame.grid(row=0, column=0, padx=10, pady=10)
    def on_thumbnail_click(self, url):
        print(f"Thumbnail clicked! Opening video: {url}")
        webbrowser.open(url, new=2)
    

    def embed_youtube_videos(self, video_urls):
        try:
            for i, (url,description) in enumerate(video_urls):
                #yt = YouTube(url)
                thumbnail_url = YouTube(url).thumbnail_url
                response=requests.get(thumbnail_url)

            # Download thumbnail image
                
                thumbnail_image = Image.open(BytesIO(response.content)).resize((300, 200), Image.LANCZOS)
                thumbnail_photo = ImageTk.PhotoImage(thumbnail_image)
        #Create an embedded frame using the Canvas widget
                embedded_frame = ttk.Frame(self.canvas, width=270, height=180)
                embedded_frame.pack()
                

        # Create a label to display the video (adjust the URL accordingly)
                
                video_label = tk.Label(embedded_frame,image=thumbnail_photo)
                self.thumbnail_photos.append(thumbnail_photo)
                video_label.image=thumbnail_photo
                video_label.pack()
        #Binding the video link to the button

                video_label.bind("<Button-1>", lambda event, link=url: self.on_thumbnail_click(link))
        # Create a label for the video text
                text_label = ttk.Label(embedded_frame, text=description, wraplength=280, font=("Helvetica", 11))
                text_label.pack()

        # Embed the video using create_window method
                self.canvas.create_window((0, i*235), window=embedded_frame, anchor='nw')
        except Exception as e:
            print(f"Error embedding video: {e}")

    

    def create_widgets(self):
        root.geometry("1600x800")  # Set the main window geometry

        # Background image with a label
        self.background_image = PhotoImage(file="mainimage.png")
        background_label = tk.Label(self.root, image=self.background_image)
        background_label.place(relwidth=1, relheight=1)

        # Learn button
        learn_button = tk.Button(self.root, text="Learn", command=self.show_learn_options, font=('Arial', 16), bg='black', fg='white')
        learn_button.place(relx=0.5, rely=0.5, anchor='center', width=250, height=100)

        # Revise button
        revise_button = tk.Button(self.root, text="Revise", command=self.show_revise_options, font=('Arial', 16), bg='white', fg='black')
        revise_button.place(relx=0.5, rely=0.7, anchor='center', width=250, height=100)

        #Counselling button
        counselling_button=tk.Button(self.root,text="Get a Free Academic Counselling Session from our Experts!",command=lambda: self.on_button_click("https://calendly.com/sanya1213"),
                                     font=('Arial', 18), bg='lightblue', fg='black',wraplength=150)
        counselling_button.place(relx=0.8, rely=0.6, anchor='center',width=200, height=200)
        
    def on_button_click(self, link):
        print(f"Button clicked! Opening link: {link}")
        webbrowser.open(link, new=2)

    def extract_text_from_pdf(self,pdf_path):
        text=""
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page_num in range(len(pdf_reader.pages)):
            # Extract text from each page
                page = pdf_reader.pages[page_num]
                text += page.extract_text()

        return text

   

    def show_revise_options(self):
        
        revise_options_window=tk.Toplevel(self.root)
        revise_options_window.title("Revise in Short")
        #Subject Selection
        self.subject_var = tk.StringVar()
        subjects = ["English", "Maths"]
        self.subject_menu = ttk.Combobox(revise_options_window, values=subjects, textvariable=self.subject_var)
        self.subject_menu.config(width=40)  # Set width (in characters)
        self.subject_menu.config(font=("Arial", 15))  # Set font family and size
        self.subject_menu.config(background="gray",foreground="blue")
        self.subject_menu.grid(row=0, column=1, padx=10, pady=10)
        self.subject_var.set("Select Subject: ") 

        # Grade selection
        self.grade_var = tk.StringVar()
        grades = ["Primary School", "Middle School", "High School"]
        self.grade_menu = ttk.Combobox(revise_options_window, values=grades, textvariable=self.grade_var)
        self.grade_menu.config(width=40)  # Set width (in characters)
        self.grade_menu.config(font=("Arial", 15))  # Set font family and size
        self.grade_menu.config(background="gray",foreground="blue")
        self.grade_menu.grid(row=1, column=1, padx=10, pady=10)
        self.grade_menu.bind("<<ComboboxSelected>>", self.update_topics)
        self.grade_var.set("Select School Level: ")
        

        self.topic_var = tk.StringVar()
        self.topic_menu = ttk.Combobox(revise_options_window, textvariable=self.topic_var)
        self.topic_menu.config(width=40)  # Set width (in characters)
        self.topic_menu.config(font=("Arial", 15))  # Set font family and size
        self.topic_menu.config(background="gray", foreground="blue")
        self.topic_menu.grid(row=2, column=1, padx=10, pady=10)
        self.update_topics()  # Initialize topics based on the default grade
        self.topic_var.set("Select Topic: ")
        

        # Get Summary button
        self.get_summary_button = tk.Button(revise_options_window, text="Get Summary", command=self.view_summary)
        self.get_summary_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Center the learn_options_window on the screen
        revise_options_window.update_idletasks()
        width = revise_options_window.winfo_width()
        height = revise_options_window.winfo_height()
        x = (revise_options_window.winfo_screenwidth() - width) // 2
        y = (revise_options_window.winfo_screenheight() - height) // 2
        revise_options_window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def askGPT(self,prompt):
        openai.api_key = self.api_key
        model="gpt-3.5-turbo"
        #content=f"What are the key points and quiz questions for the given content?:{prompt}",
        response = openai.chat.completions.create(
            model=model,
            #engine="davinci-codex",
            messages=[{"role": "system", "content": "You are ChatGPT, a large language model."},
            {"role": "user", "content":f"What are the key points and quiz questions for the given content?:{prompt}"},]
            #max_tokens=100,
            )
        reply = response.choices[0].message.content
        return reply
   
    def view_summary(self):
        # Get selected options
        subject = self.subject_var.get()
        grade = self.grade_var.get()
        topic = self.topic_var.get()

        # Fetch PDF path from the database
        pdf_path = self.fetch_pdf_path(subject, grade, topic)

        if pdf_path:
            # Read and display PDF content
            pdf_content = self.extract_text_from_pdf(pdf_path)
            summary_and_questions = self.askGPT(pdf_content)

            # Display summary and quiz questions
            self.display_summary_and_quiz(summary_and_questions)
            
        else:
            messagebox.showerror("Error", "PDF not found for the selected topic.")
    def display_summary_and_quiz(self, summary_and_questions):
        # Display the summary and quiz questions in a new window or widget
        summary_window = tk.Toplevel(self.root)
        summary_label = tk.Label(summary_window, text=summary_and_questions)
        summary_label.pack(padx=10, pady=10)


    def show_learn_options(self):
           

        
        learn_options_window = tk.Toplevel(self.root)
        learn_options_window.title("Learn Options")
        #Subject Selection
        self.subject_var = tk.StringVar()
        subjects = ["English", "Maths"]
        self.subject_menu = ttk.Combobox(learn_options_window, values=subjects, textvariable=self.subject_var)
        self.subject_menu.config(width=40)  # Set width (in characters)
        self.subject_menu.config(font=("Arial", 15))  # Set font family and size
        self.subject_menu.config(background="gray",foreground="purple")
        self.subject_menu.grid(row=0, column=1, padx=10, pady=10)
        self.subject_var.set("Select Subject: ") 

        # Grade selection
        self.grade_var = tk.StringVar()
        grades = ["Primary School", "Middle School", "High School"]
        self.grade_menu = ttk.Combobox(learn_options_window, values=grades, textvariable=self.grade_var)
        self.grade_menu.config(width=40)  # Set width (in characters)
        self.grade_menu.config(font=("Arial", 15))  # Set font family and size
        self.grade_menu.config(background="gray",foreground="purple")
        self.grade_menu.grid(row=1, column=1, padx=10, pady=10)
        self.grade_menu.bind("<<ComboboxSelected>>", self.update_topics)
        self.grade_var.set("Select School Level: ")
        

        self.topic_var = tk.StringVar()
        self.topic_menu = ttk.Combobox(learn_options_window, textvariable=self.topic_var)
        self.topic_menu.config(width=40)  # Set width (in characters)
        self.topic_menu.config(font=("Arial", 15))  # Set font family and size
        self.topic_menu.config(background="gray", foreground="purple")
        self.topic_menu.grid(row=2, column=1, padx=10, pady=10)
        self.update_topics()  # Initialize topics based on the default grade
        self.topic_var.set("Select Topic: ")
        

        # View PDF button
        self.view_pdf_button = tk.Button(learn_options_window, text="View PDF", command=self.view_pdf)
        self.view_pdf_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Center the learn_options_window on the screen
        learn_options_window.update_idletasks()
        width = learn_options_window.winfo_width()
        height = learn_options_window.winfo_height()
        x = (learn_options_window.winfo_screenwidth() - width) // 2
        y = (learn_options_window.winfo_screenheight() - height) // 2
        learn_options_window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

        

    def update_topics(self, event=None):
        grade = self.grade_var.get()
        subject=self.subject_var.get()
        if grade == "Primary School" and subject=="Maths":
            topics = ["Geometry", "Number Operations", "Time"]
        elif grade == "Middle School" and subject=="Maths":
            topics = ["Algebra", "Decimals and Fractions", "Ratios and Proportion"]
        elif grade == "High School" and subject=="Maths":
            topics = ["Calculus", "Probability and Statistics"]
        elif grade == "Primary School" and subject=="English":
            topics = ["Adjectives and Adverbs","Nouns and Pronouns","Verbs"]
        elif grade == "Middle School" and subject=="English":
            topics = ["Active and Passive Voice","Punctuation and Sentence Structure"]
        elif grade == "High School" and subject=="English":
            topics = ["Advanced Grammar","Figures of Speech"]
        else:
            topics = []  # Default to an empty list if grade is unknown

        self.topic_menu["values"] = topics
        self.topic_var.set(topics[0] if topics else "")  # Set the first topic as default if available

    def view_pdf(self):
        # Get selected options
        subject = self.subject_var.get()
        grade = self.grade_var.get()
        topic = self.topic_var.get()

        # Fetch PDF path from the database
        pdf_path = self.fetch_pdf_path(subject, grade, topic)

        if pdf_path:
            # Read and display PDF content
            pdf_content = self.extract_text_from_pdf(pdf_path)
            self.display_pdf_content(pdf_content)
        else:
            messagebox.showerror("Error", "PDF not found for the selected topic.")

    def fetch_pdf_path(self, subject, grade, topic):
        # Connect to the MySQL database
        mycon=mysql.connector.connect(host="localhost",user="root",passwd="sanya1213",database="textbook")
        
        cursor=mycon.cursor()

        # Query the database for the PDF path
        query = "SELECT pdf_path FROM topics WHERE subject=%s AND grade=%s AND topic_name=%s"
        cursor.execute(query, (subject, grade, topic)) 
        result = cursor.fetchone()

        mycon.close()

        return result[0] if result else None

    def display_pdf_content(self, pdf_content):
        # Display PDF content in a new window or widget
       
        pdf_display_window = tk.Toplevel(self.root)
        #pdf_display_window.attributes('fullscreen',True)
        custom_font=tkFont.Font(family="Helvetica,",size=14)
        pdf_display_text = tk.Text(pdf_display_window, wrap='word', font=custom_font, width=300, height=200, foreground="blue", background="#d8bfd8")
       # pdf_display_text = tk.Text(pdf_display_window, wraplength=250, font=custom_font, width=300, height=200, foreground="blue", background="#d8bfd8")
        pdf_display_text.insert(tk.END, pdf_content)
        pdf_display_text.pack()
root=tk.Tk()


chatgpt_instance=PDFViewerApp(root,api_key=api_key)
subject = chatgpt_instance.subject_var.get()
grade = chatgpt_instance.grade_var.get()
topic = chatgpt_instance.topic_var.get()

        # Fetch PDF path from the database
pdf_path = chatgpt_instance.fetch_pdf_path(subject, grade, topic)

if pdf_path:
    pdf_text = chatgpt_instance.extract_text_from_pdf(pdf_path)
    result=chatgpt_instance.askGPT(pdf_text)
    print(result)


root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFViewerApp(root)
    root.mainloop()