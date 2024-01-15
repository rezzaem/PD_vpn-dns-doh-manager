from customtkinter import *
from CTkTable import CTkTable
from PIL import Image

app = CTk()
app.geometry("856x645")
app.resizable(0, 0)

set_appearance_mode("light")

sidebar_frame = CTkFrame(master=app, fg_color="#2A8C55", width=176, height=650, corner_radius=0)
sidebar_frame.pack_propagate(0)
sidebar_frame.pack(fill="y", anchor="w", side="left")

logo_img_data = Image.open("logo.png")
logo_img = CTkImage(dark_image=logo_img_data, light_image=logo_img_data, size=(77.68, 85.42))

CTkLabel(master=sidebar_frame, text="", image=logo_img).pack(pady=(38, 0), anchor="center")

rooms_img_data = Image.open("analytics_icon.png")
rooms_img = CTkImage(dark_image=rooms_img_data, light_image=rooms_img_data)

CTkButton(master=sidebar_frame, image=rooms_img, text="Rooms", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w").pack(anchor="center", ipady=5, pady=(60, 0))

reservations_img_data = Image.open("analytics_icon.png")
reservations_img = CTkImage(dark_image=reservations_img_data, light_image=reservations_img_data)

CTkButton(master=sidebar_frame, image=reservations_img, text="Reservations", fg_color="#fff", font=("Arial Bold", 14), text_color="#2A8C55", hover_color="#eee", anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))

customers_img_data = Image.open("package_icon.png")
customers_img = CTkImage(dark_image=customers_img_data, light_image=customers_img_data)
CTkButton(master=sidebar_frame, image=customers_img, text="Customers", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))

billing_img_data = Image.open("list_icon.png")
billing_img = CTkImage(dark_image=billing_img_data, light_image=billing_img_data)
CTkButton(master=sidebar_frame, image=billing_img, text="Billing", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))

reports_img_data = Image.open("returns_icon.png")
reports_img = CTkImage(dark_image=reports_img_data, light_image=reports_img_data)
CTkButton(master=sidebar_frame, image=reports_img, text="Reports", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))

settings_img_data = Image.open("settings_icon.png")
settings_img = CTkImage(dark_image=settings_img_data, light_image=settings_img_data)
CTkButton(master=sidebar_frame, image=settings_img, text="Settings", fg_color="transparent", font=("Arial Bold", 14), hover_color="#207244", anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))

main_view = CTkFrame(master=app, fg_color="#fff", width=680, height=650, corner_radius=0)
main_view.pack_propagate(0) # Don't allow the widgets inside to determine the main_view's width / height
main_view.pack(side="left")

title_frame = CTkFrame(master=main_view, fg_color="transparent")
title_frame.pack(anchor="n", fill="x", padx=27, pady=(29, 0))

CTkLabel(master=title_frame, text="Hotel Management", font=("Arial Black", 25), text_color="#2A8C55").pack(anchor="nw", side="left")

CTkButton(master=title_frame, text="+ New Reservation", font=("Arial Black", 15), text_color="#fff", fg_color="#2A8C55", hover_color="#207244").pack(anchor="ne", side="right")

metrics_frame = CTkFrame(master=main_view, fg_color="transparent")
metrics_frame.pack(anchor="n", fill="x", padx=27, pady=(36, 0))

# ... (the rest of the metrics_frame code remains unchanged)

search_container = CTkFrame(master=main_view, height=50, fg_color="#F0F0F0")
search_container.pack(fill="x", pady=(45, 0), padx=27)

CTkEntry(master=search_container, width=305, placeholder_text="Search Reservation", border_color="#2A8C55", border_width=2).pack(side="left", padx=(13, 0), pady=15)

CTkComboBox(master=search_container, width=125, values=["Date", "Most Recent Reservation", "Least Recent Reservation"], button_color="#2A8C55", border_color="#2A8C55", border_width=2, button_hover_color="#207244", dropdown_hover_color="#207244", dropdown_fg_color="#2A8C55", dropdown_text_color="#fff").pack(side="left", padx=(13, 0), pady=15)
CTkComboBox(master=search_container, width=125, values=["Status", "Pending", "Confirmed", "Cancelled"], button_color="#2A8C55", border_color="#2A8C55", border_width=2, button_hover_color="#207244", dropdown_hover_color="#207244", dropdown_fg_color="#2A8C55", dropdown_text_color="#fff").pack(side="left", padx=(13, 0), pady=15)

table_data = [
    ["Reservation ID", "Guest Name", "Room Type", "Check-In Date", "Check-Out Date", "Status"],
    ['3833', 'Alice', 'Suite', '2023-01-15', '2023-01-20', 'Confirmed'],
    ['6432', 'Bob', 'Standard', '2023-02-10', '2023-02-15', 'Pending'],
    ['2180', 'Crystal', 'Deluxe', '2023-03-05', '2023-03-10', 'Confirmed'],
    # ... (additional reservation data)
]

table_frame = CTkScrollableFrame(master=main_view, fg_color="transparent")
table_frame.pack(expand=True, fill="both", padx=27, pady=21)
table = CTkTable(master=table_frame, values=table_data, colors=["#E6E6E6", "#EEEEEE"], header_color="#2A8C55", hover_color="#B4B4B4")
table.edit_row(0, text_color="#fff", hover_color="#2A8C55")
table.pack(expand=True)

app.mainloop()
