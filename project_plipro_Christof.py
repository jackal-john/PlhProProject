
import random


def  objective_function(t):
    return  t[0]^2 + t[1]^3 + t[2]^4 + t[0]*t[1]*t[2]


#Η συνάρτηση παράγει μια λίστα λύσεων του προβλήματος
#Παράμετροι
#Ν: πλήθος λύσεων
#Κ: πλήθος επιλεγμένων λύσεων για το επόμενο βήμα
def genetic_algorithm(N, K, p_d=0.3, p_m=0.3, a1=0, a2=10, b1=0, b2=20, c1=0, c2=30):
    population = [] 
  