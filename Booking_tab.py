from tkinter import *
from tkinter import messagebox as mb




def book_seats(event=None):
    s = seat_entry.get()
    try:
        if seats[s] == 'свободно':
            seats[s] = 'забронировано'
            update_canvas()
            mb.showinfo('Успех', f"Место {s} успешно забронировано!")
        else:
            mb.showinfo("Ошибка",f"Место {s} уже забронировано или не существует.")
    except KeyError:
        mb.showinfo("Ошибка",f"Место {s} не существует!")

def update_canvas():
    canvas.delete('all')
    for i, (seat, status) in enumerate(seats.items()):
        x = i * 40 + 20
        y = 20
        color = "green" if status == "свободно" else "red"
        canvas.create_rectangle(x, y, x + 30, y + 30, fill=color)
        canvas.create_text(x + 15, y + 15, text=seat)


def cancel_booking(event=None):
    s = cancel_entry.get()
    try:
        if seats[s] == 'забронировано':
            seats[s] = 'свободно'
            update_canvas()
            mb.showinfo('Успех', f"Бронь места {s} успешно отменена!")
        else:
            mb.showinfo("Ошибка",f"Место {s} не забронировано или не существует.")
    except KeyError:
        mb.showinfo("Ошибка",f"Место {s} не существует!")


#=========================================================



root = Tk()
root.title("Бронирование мест")
root.geometry("450x350+400+400")

canvas = Canvas(root, width=400, height=60)
canvas.pack(pady=10)

seats = {f"Б{i}": "свободно" for i in range(1, 10)}
update_canvas()

info_canvas_green = Canvas(root, width=400, height=60)
info_canvas_green.create_rectangle(15, 15, 45,  45, fill='green', outline='black')
info_canvas_green.create_text(110, 27.5, text="Свободно")
info_canvas_green.create_rectangle(205, 15, 175,  45, fill='red', outline='black')
info_canvas_green.create_text(270, 27.5, text="Забронировано")
info_canvas_green.pack()


seat_entry = Entry()
seat_entry.pack(pady=10)
seat_entry.focus()
seat_entry.bind("<Return>", book_seats)


Button(text="Забронировать места", command=book_seats).pack(pady=10)

cancel_entry = Entry()
cancel_entry.pack(pady=10)
cancel_entry.focus()
cancel_entry.bind("<Return>", cancel_booking)


Button(text="Отменить бронь", command=cancel_booking).pack(pady=10)


root.mainloop()