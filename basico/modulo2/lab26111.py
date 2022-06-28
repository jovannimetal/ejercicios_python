hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

# Escribe tu código aqui.
minutos = (mins + dura) % 60
horas = int(hour + (mins +dura) / 60) % 24


print(horas,":",minutos)