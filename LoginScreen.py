import customtkinter as ctk
from PIL import Image
from CTkMessagebox import CTkMessagebox as Msg

loginWindow = ctk.CTk()

WIDTH = 600
HEIGHT = 400
screen_width = loginWindow.winfo_screenwidth()
screen_height = loginWindow.winfo_screenheight()
x = (screen_width - WIDTH) // 2
y = (screen_height - HEIGHT) // 2
loginWindow.resizable(False, False)

loginWindow.title('Login Screen')
loginWindow.geometry(f'{WIDTH}x{HEIGHT}+{x}+{y}')


my_email = 'admin@admin.com'
my_pass = '1234'


# FUNCTIONS
def login():
    email = email_entry.get()
    password = password_entry.get()
    if email == my_email and password == my_pass:
        Msg(master=loginWindow, title='Success', message='Login Successful!')
        print('Login Successful')
        password_entry.delete(0, ctk.END)
    elif email == '' or password == '':
        Msg(master=loginWindow, title='Warning', message='Email/Password cannot be empty', icon="warning")
    else:
        Msg(master=loginWindow, title='error', message='Wrong password/email!', icon='cancel')
        print('Wrong password/email!')
        # email_entry.delete(0, ctk.END)
        password_entry.delete(0, ctk.END)


# FRAMES
left_frame = ctk.CTkFrame(master=loginWindow, width=300)
left_frame.pack(side=ctk.LEFT, fill=ctk.Y)
right_frame = ctk.CTkFrame(master=loginWindow, width=300, fg_color='#fff')
right_frame.pack(side=ctk.RIGHT, fill=ctk.Y)

left_image = ctk.CTkImage(light_image=Image.open('assets/left-img.jpg'), dark_image=Image.open('assets/left-img.jpg'),
                          size=(300, 400))
left_image_label = ctk.CTkLabel(master=left_frame, image=left_image, text='')
left_image_label.pack()

welcome_txt = ctk.CTkLabel(right_frame, text='Welcome back!!!'.upper(), text_color='#012640', width=300, anchor=ctk.NW,
                           font=('Poppins', 24, 'bold'))
welcome_txt.pack(fill=ctk.BOTH, pady=(20, 5), padx=15)
below_txt = ctk.CTkLabel(right_frame, text='Login and find out what you missed', text_color='#555',
                         font=('Poppins', 12, 'normal'), anchor=ctk.W)
below_txt.pack(fill=ctk.BOTH, pady=0, padx=15)

email_label = ctk.CTkLabel(right_frame, text='Email:', text_color='#012640', anchor=ctk.W, font=('Poppins', 16, 'bold'))
email_label.pack(fill=ctk.BOTH, pady=(15, 0), padx=15)
email_entry = ctk.CTkEntry(right_frame, height=35, border_color='#012640', border_width=1, fg_color='#fff',
                           placeholder_text='Enter Your Email...', text_color='#012640', font=('Poppins', 14))
email_entry.pack(fill=ctk.BOTH, pady=(0, 0), padx=15)

password_label = ctk.CTkLabel(right_frame, text='Password:', text_color='#012640', anchor=ctk.W,
                              font=('Poppins', 16, 'bold'))
password_label.pack(fill=ctk.BOTH, pady=(10, 0), padx=15)
password_entry = ctk.CTkEntry(right_frame, height=35, border_color='#012640', border_width=1, fg_color='#fff', show='*',
                              placeholder_text='Enter Your Password...', text_color='#012640', font=('Poppins', 14))
password_entry.pack(fill=ctk.BOTH, pady=(0, 0), padx=15)

login_btn = ctk.CTkButton(right_frame, text='Login', font=('Poppins', 14), width=100, fg_color='#012640',
                          cursor="pointinghand", hover_color='#001726', command=login)
login_btn.pack(pady=(15, 0), padx=15)

or_label = ctk.CTkLabel(right_frame, text='or login with:', font=('Poppins', 13, 'normal'), anchor=ctk.W,
                        text_color='#555')
or_label.pack(pady=(15, 5), padx=15)

google_image = ctk.CTkImage(light_image=Image.open('assets/google.png'), dark_image=Image.open('assets/google.png'))
google_btn = ctk.CTkButton(right_frame, text='Google', font=('Poppins', 14), width=100, fg_color='#fff',
                           border_color='#fff', cursor="pointinghand", hover_color='#eeeeee', image=google_image,
                           border_width=1, text_color='#001726')
google_btn.pack(pady=(0, 0), padx=15)

fb_image = ctk.CTkImage(light_image=Image.open('assets/fb.png'), dark_image=Image.open('assets/fb.png'))
fb_btn = ctk.CTkButton(right_frame, text='Facebook', font=('Poppins', 14), width=100, fg_color='#fff',
                       border_color='#fff', cursor="pointinghand", hover_color='#eeeeee', image=fb_image,
                       border_width=1, text_color='#001726')
fb_btn.pack(pady=(7, 0), padx=15)

loginWindow.update_idletasks()
loginWindow.mainloop()
