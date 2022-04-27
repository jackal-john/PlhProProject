import random
import time

#=====================================
#Παίρνει ως είσοδο μια πλειάδα t
#και επιστρέφει την τιμή της συνάρτησης f(t0, t1, t2)
# To x**2 σημαίνει x εις την δευτέρα.
def  objective_function(t):
    return  t[0]**2 + t[1]**3 + t[2]**4 + t[0]*t[1]*t[2]
#--------------------------------------


#==============================
#Παίρνει ένα tupple (t0, t1, t2) και θα αλλάζει
#ένα στοιχειο του στην τύχη
#Επιστρέφει το νέο t (new_t)
def   mutation(t, a1, a2, b1, b2, c1, c2):
    #Φτιάχνω μια νέα λίστα με τα 3 πεδία του tuple
    #Γιατί δεν μπορώ να αλλάξω τα πεδία ενός tuple
    new_t = list(t)
    #Επιλέγω ένα τυχαίο από τα 3 πεδία του tupple
    #και το αλλάζω. Σβήνω την παλιά τιμή και βάζω μια καινούρια.
    k = random.randrange(3)
    if k==0:
        new_t[0] = (a2-a1)*random.random() + a1
    elif k==1:
        new_t[1] = (b2-b1)*random.random() + b1
    elif k==2:
        new_t[2] = (c2-c1)*random.random() + c1
    #Στο τέλος μετατρέπω τη λίστα σε tuple για να
    #επιστρέψω tuple
    return tuple(new_t)
#-------------------------------



#===================================
#Θα παίρνει τα tupples t και s και θα
#δημιουργεί ένα νέο tupple με στοιχεία από τα
#t, s  (t0, t1, t2)  (s0, s1, s2)
#Επιλέγω ένα τυχαίο στοιχείο της t  και το αλλάζω με
#το αντίστοιχο στοιχείο της s.
def  crossbreed(t, s):
    #Φτιάχνω μια νέα λίστα με τα 3 πεδία του tuple
    #Γιατί δεν μπορώ να αλλάξω τα πεδία ενός tuple
    new_t = list(t)
    k = random.randrange(3)
    new_t[k] = s[k]
    #Στο τέλος μετατρέπω τη λίστα σε tuple για να
    #επιστρέψω tuple
    return tuple(new_t)
    
#-----------------------------------



#Η συνάρτηση παράγει μια λίστα λύσεων του προβλήματος
#Παράμετροι
#Ν: πλήθος λύσεων
#Κ: πλήθος επιλεγμένων λύσεων για το επόμενο βήμα
#p_d: πιθανότητα διασταύρωσης
#p_m: πιθανότητα μετάλλαξης
#[a1, a2] είναι το διάστημα για την μεταβλητή x στη συνάρτηση f(x,y,z)
#[b1, b2] είναι το διάστημα για την μεταβλητή y στη συνάρτηση f(x,y,z)
#[c1, c2] είναι το διάστημα για την μεταβλητή z στη συνάρτηση f(x,y,z)
#steps: Ο αριθμός βημάτων (γεννεών) του γεννετικού αλγορίθμου.
#printflag: Αν εδώ βάλουμε την τιμή True τότε το πρόγραμμα θα τυπώνει σε κάθε επανάληψη την καλύτερη λύση.
#Επιστρέφει:
def genetic_algorithm(N, K, steps, p_cb=0.3, p_m=0.3, a1=0, a2=10, b1=0, b2=20, c1=0, c2=30, printflag=False):
    population = [] 
    #Αρχικοποιώ τις λύσεις
    #Χρησιμοποιώ την συνάρτηση random.random() από τη βιβλιοθήκη
    #random για να δημιουργήσω μια τυχαία τιμή στο διάστημα [0,1].
    #Ακολούθως για την μεταβλητή x μετατρέπω αυτή την τιμή στο διάστημα [a1, a2] με τον
    #παρακάτω τύπο. Ομοίως και για τις υπόλοιπες μεταβλητές.
    for n in range(N):
        x = (a2-a1)*random.random() + a1
        y = (b2-b1)*random.random() + b1
        z = (c2-c1)*random.random() + c1
        atom = (x,y,z)
        population.append(atom)

    #Αποτίμηση Λύσεων
    #Φτιάχνω ένα λεξικό που θα έχει ως πεδία, μια λύση και την τιμή της (στην f)
    dictionary = {}
    for atom in population:
        value = objective_function(atom)
        dictionary[atom] = value
    #Ταξινομώ το λεξικό ως προς τα values.
    #Kαι κρατάω τα Κ με τις μεγαλύτερες τιμές.
    dictionary = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True)[:K])

    
        
    #Επανάληψη του Γεννετικού Αλγορίθμου
    for n in range(steps):
        #Φτιάχνω μια λίστα με τα keys του λεξικού
        #για να τα χρησιμοποιήσω μετά.
        mylist = list(dictionary)
        for  s  in  mylist:
            x = random.random()
            if x < p_m:
                #Εδώ κάνω mutation. Δηλαδή φτιάχνω με μετάλλαξη μια νέα λύση
                #με βάση τη λύση s.
                new_solution = mutation(s, a1, a2, b1, b2, c1, c2) 
                #Προσθέτω τη λύση στο λεξικό dictionary.
                value = objective_function(new_solution)
                dictionary[new_solution] = value
            elif x < p_m+p_cb:
                #Εδώ κάνω crossbread
                #Πρέπει να επιλέξω και μια ακόμη λύση.
                index = random.randrange(K)
                s2 = mylist[index]
                new_solution = crossbreed(s, s2)
                #Προσθέτω τη λύση στο λεξικό dictionary.
                value = objective_function(new_solution)
                dictionary[new_solution] = value
        dictionary = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True)[:K])
        if printflag == True:
            #Τυπώνω την καλύτερη λύση.
            s = list(dictionary)[0]
            print('iteration ' + str(n+1)  + '\t{:.2f}'.format(s[0]) + '\t' '{:.2f}'.format(s[1]) + '\t' + '{:.2f}'.format(s[2]),   '\t\t value=','{:.2f}'.format(dictionary[s]) )
    

    return dictionary
        



#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#Κυρίως πρόγραμμα
start = time.time()
solutions = genetic_algorithm(100, 20, 1000, 0.2, 0.2)
end = time.time()
print('Time needed = ',  end - start)
for s in solutions:
    print ('{:.4f}'.format(s[0]) + '\t' '{:.4f}'.format(s[1]) + '\t' + '{:.4f}'.format(s[2]),   '\t\t value=','{:.2f}'.format(solutions[s]) )

