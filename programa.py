from membresia import Gratis

mem = Gratis("mail@mail.com","2345")

print(mem.get_correo())
print(mem.get_numero_tarjeta())
print(mem.get_costo())
print(mem.get_dispositivos())
print(type(mem))
print("")

mem = mem.cambiar_suscripcion(1)
print(mem.get_correo())
print(mem.get_numero_tarjeta())
print(mem.get_costo())
print(mem.get_dispositivos())
print(type(mem))
print("")


mem = mem.cambiar_suscripcion(2)
print(mem.get_correo())
print(mem.get_numero_tarjeta())
print(mem.get_costo())
print(mem.get_dispositivos())
print(type(mem))
print("")

mem = mem.cambiar_suscripcion(3)
print(mem.get_correo())
print(mem.get_numero_tarjeta())
print(mem.get_costo())
print(mem.get_dispositivos())
print(type(mem))
print("")

mem = mem.cambiar_suscripcion(4)
print(mem.get_correo())
print(mem.get_numero_tarjeta())
print(mem.get_costo())
print(mem.get_dispositivos())
print(type(mem))
print("")

mem = mem.cancelar_suscripcion(mem.get_correo(), mem.get_numero_tarjeta())
print(mem.get_correo())
print(mem.get_numero_tarjeta())
print(mem.get_costo())
print(mem.get_dispositivos())
print(type(mem))