#Calcular IMC

peso= float(input('Qual é o seu peso?')) 
altura = float(input ('Qual é sua altura? (Ex:1.90)'))

imc = (peso/altura**2) 

if imc <= 18.5 and isinstance(imc, float):
    print('Seu imc é:', "%.2f" % imc , "(magreza)")
elif imc < 24.9 and isinstance(imc, float):
    print('Seu imc é:', "%.2f" % imc , "(Normal)")
elif imc < 29.9 and isinstance(imc, float):
    print('Seu imc é:', "%.2f" % imc , "(Sobrepeso)")
<<<<<<< HEAD
elif imc < 39.9 and isinstance(imc, float):
    print('Seu imc é:', "%.2f" % imc , "(Obesidade)")
=======
elif (imc > 30) and (imc < 39.9):
     print('Seu imc é:', "%.2f" % imc , "(Obesidade)")
>>>>>>> 8de790e22e45fbaecad5abc3368bcd02e87cde9c
else:
    print('Seu imc é:', "%.2f" % imc , "(Obesidade Grave)")



      



    
    

          
      


     
    


    



