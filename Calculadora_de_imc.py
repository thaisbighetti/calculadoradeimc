#Calcular IMC

peso=float(input('Qual é o seu peso?')) 
altura = float(input ('Qual é sua altura? (Ex:1.90)'))

imc = (peso/altura**2) 

if imc <= 18.5:
    print('Seu imc é:', "%.2f" % imc , "(magreza)")
elif (imc > 18.5) and (imc < 24.9):
    print('Seu imc é:', "%.2f" % imc , "(Normal)")
elif (imc > 25) and (imc < 29.9):
    print('Seu imc é:', "%.2f" % imc , "(Sobrepeso)")
elif (imc > 30) and (imc < 39.9):
        print('Seu imc é:', "%.2f" % imc , "(Obesidade)")
else:
    print('Seu imc é:', "%.2f" % imc , "(Obesidade Grave)")



      



    
    

          
      


     
    


    



