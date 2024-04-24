#usando a keyword break

print("BREAK: \n")
for i in range(1, 6):
    if i == 3:
        break
    else:
        print(f"Number atual: {i}")
print("Fim break...\n")

#usando a keyword contiue

print("CONTINUE: \n")
for i in range(1, 6):
    if i == 3:
        continue
    else:
        print(f"Numero atual: {i}")
print("Fim do contine...")