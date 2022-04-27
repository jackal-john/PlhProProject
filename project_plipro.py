
import random
import time


#=====================================
#Παίρνει ως είσοδο μια πλειάδα t
#και επιστρέφει την τιμή της συνάρτησης f(t0, t1, t2)
# To x**2 σημαίνει x εις την δευτέρα.
def  objective_function(t):
    return  t[0]**2 + t[1]**3 + t[2]**4 + t[0]*t[1]*t[2]
    #return  (t[0] - 5)**2  +  (t[1] - 10)**2  + (t[2]- 15)**2
#--------------------------------------
    


#=======================================
#Δημιουργεί έναν τυχαίο πραγματικό αριθμό στο διάστημα [α,b]
def  random_number(a, b):
    return (b-a)*random.random() + a
#---------------------------------------

#==============================
#Παίρνει ένα tupple (t0, t1, t2) και θα αλλάζει
#ένα στοιχειο του στην τύχη
#Επιστρέφει το νέο t (new_t)
# a = [0, 0, 0]
# b = [10, 20, 30]
def   mutation(t, a, b):
    #Φτιάχνω μια νέα λίστα με τα 3 πεδία του tuple
    #Γιατί δεν μπορώ να αλλάξω τα πεδία ενός tuple
    new_t = list(t)
    #Επιλέγω ένα k στην τύχη (μεταξύ του 1 και του 3)
    #αυτό δείχνει πόσες θέσεις θα αλλάξω από το αρχικό
    #tupple
    k = random.randint(1,3)
    #Φτιάχνω μια λίστα από k δείκτες του new_t που
    #θα αλλάξουν (mutation)  -->  αν κ=2  [0, 2]
    indices = random.sample(range(3), k)
    #αλλάζω όλα τα στοιχεία που είναι σε αυτές τις θέσεις
    #στη λίστα
    for i in indices:
        new_t[i] = random_number(a[i],b[i])
    #Στο τέλος μετατρέπω τη λίστα σε tuple για να
    #επιστρέψω tuple
    return tuple(new_t)
#-------------------------------



#===================================
#Θα παίρνει τα tupples t και s και θα
#δημιουργεί ένα νέο tupple με στοιχεία από τα
#t, s  (t0, t1, t2)  (s0, s1, s2)
#Επιλέγω κάποια στοιχείο του t  και τα αλλάζω με
#τα αντίστοιχα στοιχεία της s.
def  crossbreed(t, s):
    #Φτιάχνω μια νέα λίστα με τα 3 πεδία του tuple
    #Γιατί δεν μπορώ να αλλάξω τα πεδία ενός tuple
    new_t = list(t)
    #Επιλέγω ένα k στην τύχη (μεταξύ του 1 και του 3)
    #Το κ περιγράφει το πλήθος των στοιχείων του t που
    #θα αλλάξω (1, 2, ή 3).
    k = random.randint(1,3)
    #Φτιάχνω μια λίστα από k δείκτες του new_t που
    #θα αλλάξουν (crossbreed) αν κ=2 -->  [0, 2]
    indices = random.sample(range(3), k)
    #αλλάζω όλα τα στοιχεία που είναι σε αυτές τις θέσεις
    #στη λίστα με στοιχεία από το s
    for i in indices:
        new_t[i] = s[i]
    #Στο τέλος μετατρέπω τη λίστα σε tuple για να
    #επιστρέψω tuple
    return tuple(new_t)
    
#-----------------------------------




#Η συνάρτηση παράγει μια λίστα λύσεων του προβλήματος
#Παράμετροι
#Ν: πλήθος λύσεων
#Κ: πλήθος επιλεγμένων λύσεων για το επόμενο βήμα
#p_m: πιθανότητα μετάλλαξης  (1-p_m) η πιθανότητα διασταύρωσης
#[a1, a2] είναι το διάστημα για την μεταβλητή x στη συνάρτηση f(x,y,z)
#[b1, b2] είναι το διάστημα για την μεταβλητή y στη συνάρτηση f(x,y,z)
#[c1, c2] είναι το διάστημα για την μεταβλητή z στη συνάρτηση f(x,y,z)
#steps: Ο αριθμός βημάτων (γεννεών) του γεννετικού αλγορίθμου.
#printflag: Αν εδώ βάλουμε την τιμή True τότε το πρόγραμμα θα τυπώνει σε κάθε επανάληψη την καλύτερη λύση.
#Επιστρέφει:
def genetic_algorithm(N, K, steps, p_m=0.3, a=[0, 0, 0], b=[10, 20, 30], printflag=False):
    #Αρχικοποιώ τις λύσεις
    #Χρησιμοποιώ την συνάρτηση random.random() από τη βιβλιοθήκη
    #random για να δημιουργήσω μια τυχαία τιμή στο διάστημα [0,1].
    #Ακολούθως για την μεταβλητή x μετατρέπω αυτή την τιμή στο διάστημα [a1, a2] με τον
    #παρακάτω τύπο. Ομοίως και για τις υπόλοιπες μεταβλητές.
    #To παρακάτω loop δημιουργεί μια λίστα (population) από 
    #N tuples.
    population = []
    for n in range(N):
        x = random_number(a[0], b[0])
        y = random_number(a[1], b[1])
        z = random_number(a[2], b[2])
        atom = (x,y,z)
        population.append(atom)

    #Αποτίμηση Λύσεων
    #Φτιάχνω ένα λεξικό που θα έχει ως πεδία, μια λύση και την τιμή της (στην f)
    #{tupple : number}
    dictionary = {}
    for atom in population:
        value = objective_function(atom)
        dictionary[atom] = value
    #Ταξινομώ το λεξικό ως προς τα values.
    #Kαι κρατάω τα Κ με τις μεγαλύτερες τιμές.
    dictionary = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True)[:K])

    
    #---------------------------------------------
    #Επανάληψη του Γεννετικού Αλγορίθμου
    for n in range(steps):
        #Φτιάχνω μια λίστα με τα keys του λεξικού
        #για να τα χρησιμοποιήσω μετά.
        mylist = list(dictionary)
        items = 1 #μετράω τα items που σαρώνω
        for  s  in  mylist:
            #Δες αν γίνει μετάλλαξη ή crossbreed
            if items > 10:
                x = random.random()
                #Επέλεξε τι από τα δύο θα γίνει
                if x < p_m:
                    #Εδώ κάνω mutation. Δηλαδή φτιάχνω με μετάλλαξη μια νέα λύση
                    #με βάση τη λύση s.
                    new_solution = mutation(s, a, b) 
                    #Προσθέτω τη λύση στο λεξικό dictionary.
                    value = objective_function(new_solution)
                    dictionary[new_solution] = value
                else:
                    #Εδώ κάνω crossbread
                    #Πρέπει να επιλέξω και μια ακόμη λύση.
                    index = random.randrange(K)
                    s2 = mylist[index]
                    new_solution1 = crossbreed(s, s2)
                    new_solution2 = crossbreed(s2, s)
                    #Προσθέτω τις λύσεις στο λεξικό dictionary.
                    value1 = objective_function(new_solution1)
                    dictionary[new_solution1] = value1
                    value2 = objective_function(new_solution2)
                    dictionary[new_solution2] = value2
            items = items + 1
        dictionary = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True)[:K])
        if printflag == True:
            #Τυπώνω την καλύτερη λύση.
            s = list(dictionary)[0]
            print(n, ' ', s)
    #Τέλος Επανάληψης Γεννετικού 
    #----------------------------------------------
    return dictionary
        



#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#Κυρίως πρόγραμμα
start = time.time()
solutions = genetic_algorithm(5000, 1000, 100, 0.2, printflag=False)
end = time.time()
print('Time needed = ',  end - start)
n = 0
for s in solutions:
    print ('{:.4f}'.format(s[0]) + '\t' '{:.4f}'.format(s[1]) + '\t' + '{:.4f}'.format(s[2]),   '\t\t value=','{:.2f}'.format(solutions[s]) ) 
    n = n + 1 
    if n>20:
        break
