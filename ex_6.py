primeiro=int(input("primeiro termo..:"))
razão=int(input("razão...:"))
decimo=primeiro+(10-1)*razão
for x in range(primeiro,decimo+razão,razão):
    print('{} '.format(x), end='-> ')
print("acabou")