def book_seats(seats):
    seat_name = input("Введите номер места для бронирования (от Б1 до Б9): ")
    try:
        i = seats.index((seat_name, 'Свободно'))
        seats[i] = (seat_name, 'Забронированно')
        print(f"Место {seat_name} успешно забронированно!")
    except ValueError:
        print(f"Место {seat_name} уже забронированно или не существует")


seats = [(f"Б{i}", 'Свободно') for i in range(1, 10)]
print(seats)

while True:
    book_seats(seats)
    booking = input("Хотите забронировать еще столик? (да/нет): ")
    if booking != 'да':
        break

for seat in seats:
    print(f"{seat[0]}: {seat[1]}")

