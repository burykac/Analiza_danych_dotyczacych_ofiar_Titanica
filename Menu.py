# jakie sa opcje do wyboru?
# A - podglad danych w calosci
# B -
def Menu():
    while(True):
        decyzja = str(input("Menu programu do analizy danych katastrofy Titanica. Aby wyświetlić interesujące Cię dane \n"
                        "wybierz odpowiednią literę. Aby poznać dane dotyczące zgonów wybierz A."))
        if(decyzja == "A" or decyzja == "a"):
            jakie_dane1 = str(input("A - zależność zgonów do płci"))
            if(jakie_dane1 == "A" or jakie_dane1 = "a"):
