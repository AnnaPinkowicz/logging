def sprawdzam_palindrom(wyraz): 
    print(f" Wpisany przez Ciebie wyraz to >{wyraz}<")
    print("-----------------------")
    for letter in wyraz:
      if letter.isalpha() !=True:
        wyraz = wyraz.replace(letter,"")
    for letter in wyraz:
      if letter.isdigit == True:
        wyraz = wyraz.replace(letter,"")

    wyraz = wyraz.lower()
    wyraz = wyraz.replace(" ","")
    print(f"Rozumiem, ze moglo Ci chodzic o wyraz >{wyraz}< - \n jak nie - wpisz ponownie!")
    
    if wyraz == wyraz[::-1]: 
      print(" Twoj wyraz jest palindromem!") 
      return True
    else:  
      print(" To cos nie jest palindromem \n ")
      return False 