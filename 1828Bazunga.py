t = int(input())
i = 1
while t > 0:
    sheldon, ray = (input().split(" "))
    if(sheldon == "tesoura" and ray == "papel"):
        print(f"Caso #{i}: Bazinga!")
    elif(sheldon == "papel" and ray == "pedra"):
        print(f"Caso #{i}: Bazinga!")
    elif(sheldon == "pedra" and ray == "lagarto"):
        print(f"Caso #{i}: Bazinga!")
    elif(sheldon == "lagarto" and ray == "Spock"):
        print(f"Caso #{i}: Bazinga!")
    elif(sheldon == "Spock" and ray == "tesoura"):
        print(f"Caso #{i}: Bazinga!")
    elif(sheldon == "tesoura" and ray == "lagarto"):
        print(f"Caso #{i}: Bazinga!")
    elif(sheldon == "lagarto" and ray == "papel"):
        print(f"Caso #{i}: Bazinga!")
    elif(sheldon == "papel" and ray == "Spock"):
        print(f"Caso #{i}: Bazinga!")
    elif(sheldon == "Spock" and ray == "pedra"):
        print(f"Caso #{i}: Bazinga!")
    elif(sheldon == "pedra" and ray == "tesoura"):
        print(f"Caso #{i}: Bazinga!")
    
    elif(ray == "tesoura" and sheldon == "papel"):
        print(f"Caso #{i}: Raj trapaceou!")
    elif(ray == "papel" and sheldon == "pedra"):
        print(f"Caso #{i}: Raj trapaceou!")
    elif(ray == "pedra" and sheldon == "lagarto"):
        print(f"Caso #{i}: Raj trapaceou!")
    elif(ray == "lagarto" and sheldon == "Spock"):
        print(f"Caso #{i}: Raj trapaceou!")
    elif(ray == "Spock" and sheldon == "tesoura"):
        print(f"Caso #{i}: Raj trapaceou!")
    elif(ray == "tesoura" and sheldon == "lagarto"):
        print(f"Caso #{i}: Raj trapaceou!")
    elif(ray == "lagarto" and sheldon == "papel"):
        print(f"Caso #{i}: Raj trapaceou!")
    elif(ray == "papel" and sheldon == "Spock"):
        print(f"Caso #{i}: Raj trapaceou!")
    elif(ray == "Spock" and sheldon == "pedra"):
        print(f"Caso #{i}: Raj trapaceou!")
    elif(ray == "pedra" and sheldon == "tesoura"):
        print(f"Caso #{i}: Raj trapaceou!")
    else:
        print(f"Caso #{i}: De novo!")
    i = i + 1
    t = t - 1
            