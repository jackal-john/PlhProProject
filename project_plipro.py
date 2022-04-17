import random

def  objective_function(t):
    return  t[0]^2 + t[1]^3 + t[2]^4 + t[0]*t[1]*t[2]

#Η συνάρτηση παράγει μια λίστα λύσεων του προβλήματος
#Παράμετροι
#Ν: πλήθος λύσεων
#Κ: πλήθος επιλεγμένων λύσεων για το επόμενο βήμα
def genetic_algorithm(N, K, p_d=0.3, p_m=0.3, a1=0, a2=10, b1=0, b2=20, c1=0, c2=30):
    population = [] 
    #Αρχικοποιώ τις λύσεις
    for i in range(N):
        x = (a2-a1)*random.random() + a1
        y = (b2-b1)*random.random() + b1
        z = (c2-c1)*random.random() + c1
        atom = (x,y,z)
        population.append(atom)

    #Επανάληψη του Γεννετικού Αλγορίθμου
    
        #Αποτίμηση Λύσεων

    return population
        



#Κυρίως πρόγραμμα
solutions = genetic_algorithm(100,50,2)
for s in solutions:
    print ('{:.2f}'.format(s[0]) + '\t' '{:.2f}'.format(s[1]) + '\t' + '{:.2f}'.format(s[2]))   