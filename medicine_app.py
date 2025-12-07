import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",                     
            password="sandraisabel022506_",   
            database="medicine_db"            
        )
        if conn.is_connected():
            return conn
        else:
            messagebox.showerror("Database Error", "Unable to connect to the database.")
            return None
    except Error as e:
        messagebox.showerror("Database Error", f"Error connecting to MySQL:\n{e}")
        return None

def fetch_medicines():
    conn = create_connection()
    medicines = {}
    if conn:
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM medicines")
            for row in cursor.fetchall():
                medicines[row['name']] = {"description": row['description'], "image": row['image']}
        except Error as e:
            messagebox.showerror("Database Error", f"Error fetching medicines:\n{e}")
        finally:
            conn.close()
    return medicines

medicine_info = fetch_medicines()

window = tk.Tk()
window.title("Medicine Information")
window.iconbitmap("medi.ico") 
window.geometry("600x550")
window.config(bg="#92b0af")

loaded_images = {}  # store images to prevent garbage collection

#Top Frame
frame_top = tk.Frame(window, bg="#92b0af")
frame_top.pack(pady=10)
title = tk.Label(frame_top, text="Medicine Information", font=("Arial", 18, "bold"), bg="#92b0af")
title.pack()

#Search Frame
frame_search = tk.Frame(window, bg="#92b0af")
frame_search.pack(pady=5)

search_label = tk.Label(frame_search, text="Search Medicine:", font=("Arial", 12), bg="#92b0af")
search_label.grid(row=0, column=0, padx=5)
search_var = tk.StringVar()
search_entry = tk.Entry(frame_search, textvariable=search_var, width=30, font=("Arial", 11))
search_entry.grid(row=0, column=1, padx=5)

#Dropdown Frame
frame_dropdown = tk.Frame(window, bg="#92b0af")
frame_dropdown.pack(pady=5)

dropdown_label = tk.Label(frame_dropdown, text="Or Select Medicine:", font=("Arial", 12), bg="#92b0af")
dropdown_label.grid(row=0, column=0, padx=5)
medicine_var = tk.StringVar()
medicine_dropdown = ttk.Combobox(frame_dropdown, textvariable=medicine_var, width=30, state="readonly")
medicine_dropdown["values"] = list(medicine_info.keys())
medicine_dropdown.grid(row=0, column=1, padx=5)

#Card Frame
frame_card = tk.Frame(window, bg="#FFFFFF", bd=2, relief="groove")
frame_card.pack(pady=20, padx=20, fill="both", expand=True)

image_label = tk.Label(frame_card, bg="#FFFFFF")
image_label.pack(side="left", padx=20, pady=20)

desc_label = tk.Label(frame_card, text="", font=("Arial", 12), wraplength=100, justify="left", bg="#FFFFFF")
desc_label.pack(side="left", padx=10, pady=20)

#Delete Button
btn_delete = tk.Button(window, text="Delete Selected Medicine", font=("Arial", 12, "bold"), bg="#FD1803", fg='white')
btn_delete.pack(pady=5)

#Functions
def display_medicine(name):
    if name in medicine_info:
        desc_label.config(text=medicine_info[name]["description"], wraplength=400)
        try:
            img = tk.PhotoImage(file=medicine_info[name]["image"])
            loaded_images[name] = img
            image_label.config(image=img)
        except:
            image_label.config(image="", text="No Image Found", font=("Arial", 12))
        btn_delete.config(state="normal")
    else:
        desc_label.config(text="Medicine not found.")
        image_label.config(image="", text="")
        btn_delete.config(state="disabled")

def search_medicine(event=None):
    query = search_var.get().strip()
    medicine_dropdown.set("")
    if query in medicine_info:
        display_medicine(query)
    else:
        desc_label.config(text="Medicine not found.")
        image_label.config(image="", text="")
        btn_delete.config(state="disabled")

def select_dropdown(event=None):
    selected = medicine_var.get()
    search_var.set("")
    display_medicine(selected)

def open_add_window():
    add_window = tk.Toplevel(window)
    add_window.title("Add Medicine")
    add_window.geometry("350x320")

    tk.Label(add_window, text="Medicine Name:", font=("Arial", 11)).pack(pady=5)
    name_entry = tk.Entry(add_window, width=30)
    name_entry.pack()

    tk.Label(add_window, text="Description:", font=("Arial", 11)).pack(pady=5)
    desc_entry = tk.Text(add_window, width=35, height=5)
    desc_entry.pack()

    tk.Label(add_window, text="Image Filename (PNG/JPG):", font=("Arial", 11)).pack(pady=5)
    img_entry = tk.Entry(add_window, width=30)
    img_entry.pack()

    def save_medicine():
        name = name_entry.get().strip()
        desc = desc_entry.get("1.0", tk.END).strip()
        img_file = img_entry.get().strip()

        if name == "" or desc == "" or img_file == "":
            messagebox.showerror("Error", "All fields must be filled.")
            return

        # Insert into MySQL
        conn = create_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO medicines (name, description, image) VALUES (%s, %s, %s)",
                               (name, desc, img_file))
                conn.commit()
            except Error as e:
                messagebox.showerror("Database Error", f"Error adding medicine:\n{e}")
            finally:
                conn.close()

        medicine_info[name] = {"description": desc, "image": img_file}
        medicine_dropdown["values"] = list(medicine_info.keys())
        messagebox.showinfo("Success", f"{name} added successfully!")
        add_window.destroy()

    tk.Button(add_window, text="Save", font=("Arial", 11, "bold"), bg="#1AD81A", command=save_medicine)\
        .pack(pady=15)

def delete_medicine():
    selected = medicine_var.get()
    if selected in medicine_info:
        confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete '{selected}'?")
        if confirm:
            # Delete from MySQL
            conn = create_connection()
            if conn:
                try:
                    cursor = conn.cursor()
                    cursor.execute("DELETE FROM medicines WHERE name=%s", (selected,))
                    conn.commit()
                except Error as e:
                    messagebox.showerror("Database Error", f"Error deleting medicine:\n{e}")
                finally:
                    conn.close()

            del medicine_info[selected]
            medicine_dropdown["values"] = list(medicine_info.keys())
            medicine_dropdown.set("")
            search_var.set("")
            desc_label.config(text="")
            image_label.config(image="", text="")
            btn_delete.config(state="disabled")
            messagebox.showinfo("Deleted", f"'{selected}' has been deleted.")

#Bindings
search_entry.bind("<Return>", search_medicine)
medicine_dropdown.bind("<<ComboboxSelected>>", select_dropdown)
btn_delete.config(command=delete_medicine, state="disabled")

#Add Medicine Button
btn_add = tk.Button(window, text="Add Medicine", font=("Arial", 12, "bold"), bg="#1AD81A", fg='gray', command=open_add_window)
btn_add.pack(pady=5)

window.mainloop()

