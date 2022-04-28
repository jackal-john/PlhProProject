from tkinter import *
import random
import time



#=====================================
#Παίρνει ως είσοδο μια πλειάδα t
#και επιστρέφει την τιμή της συνάρτησης f(t0, t1, t2)
# To x**2 σημαίνει x εις την δευτέρα.
def  objective_function(t):
    return  t[0]**2 + t[1]**3 + t[2]**4 + t[0]*t[1]*t[2]
    #Μπορούμε να δοκιμάσουμε και άλλες συνάρτησεις.
    #return  (t[0] - 5)**2  +  (t[1] - 10)**2  + (t[2]- 15)**2
#--------------------------------------
    


#=======================================
#Δημιουργεί έναν τυχαίο πραγματικό αριθμό στο διάστημα [α,b]
#Χρησιμοποιώ την συνάρτηση random.random() από τη βιβλιοθήκη
#random για να δημιουργήσω μια τυχαία τιμή στο διάστημα [0,1].
#Ακολούθως για την μεταβλητή x μετατρέπω αυτή την τιμή στο διάστημα [a, b] με τον
#παρακάτω τύπο.
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
        if type(new_t[i]) == int:
            new_t[i] = random.randint(a[i],b[i])
        else:
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




#Ο παρακάτω γενετικός αλγόριθμος δουλεύει για όλες 
#τις συναρτήσεις.
#Η συνάρτηση παράγει μια λίστα λύσεων του προβλήματος
#Παράμετροι
#Ν: πλήθος λύσεων
#Κ: πλήθος επιλεγμένων λύσεων για το επόμενο βήμα
#input_type : Ο τύπος των δεδομένων που χειρίζεται ο αλγόριθμος
#0:  for integers 
#1:  for reals
#p_m: πιθανότητα μετάλλαξης  (1-p_m) η πιθανότητα διασταύρωσης
#a = [a1, a2, a3]
#b = [b1, b2, b3]
#Το a και το b περιγράφουν τα άκρα των πεδίων των μεταβλητών.
#steps: Ο αριθμός βημάτων (γεννεών) του γεννετικού αλγορίθμου.
#printflag: Αν εδώ βάλουμε την τιμή True τότε το πρόγραμμα θα τυπώνει σε κάθε επανάληψη την καλύτερη λύση.
#Επιστρέφει:
def genetic_algorithm(N, K, steps, input_type, p_m=0.3, a=[0, 0, 0], b=[10, 20, 30], printflag=False):
    #Αρχικοποιώ τις λύσεις
    #To παρακάτω loop δημιουργεί μια λίστα (population) από 
    #N tuples.
    population = []
    for n in range(N):
        if (input_type == 1):
            x = random_number(a[0], b[0])
            y = random_number(a[1], b[1])
            z = random_number(a[2], b[2])
        else:
            x = random.randint(a[0], b[0])
            y = random.randint(a[1], b[1])
            z = random.randint(a[2], b[2])
        atom = (x,y,z)
        population.append(atom)

    #Αποτίμηση Λύσεων
    #Φτιάχνω ένα λεξικό που θα έχει ως πεδία, μια λύση και την τιμή της
    #(στην f) Το λεξικό θα περιέχει πεδία της μορφής:
    #{tupple : number}
    #π.χ.
    #{(1.2,  3.4,  5.1) :  25.12,
    # (2.4,  4.12,  3.5) :  24.12}
    #
    dictionary = {}
    for atom in population:
        value = objective_function(atom)
        dictionary[atom] = value
    #Ταξινομώ το λεξικό ως προς τα values.
    #Kαι κρατάω τα Κ με τις μεγαλύτερες τιμές.
    dictionary = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True)[:K])

    
    #---------------------------------------------
    #Επανάληψη (βρόγχος) του Γεννετικού Αλγορίθμου
    for n in range(steps):
        #Φτιάχνω μια λίστα με τα keys του λεξικού
        #για να τα χρησιμοποιήσω μετά.
        mylist = list(dictionary)
        items = 1 #μετράω τα items που σαρώνω
        for  s  in  mylist:
            x = random.random()
            #Επέλεξε τι από τα δύο θα γίνει
            if x < p_m:
                #Εδώ κάνω mutation. Δηλαδή φτιάχνω με μετάλλαξη μια νέα λύση
                #με βάση τη λύση s.
                new_solution = mutation(s, a, b) 
                #Προσθέτω τη νέα υποψήφια λύση στο λεξικό dictionary.
                value = objective_function(new_solution)
                dictionary[new_solution] = value
            else:
                #Εδώ κάνω crossbread
                #Πρέπει να επιλέξω και μια ακόμη λύση.
                index = random.randrange(K)
                s2 = mylist[index]
                new_solution1 = crossbreed(s, s2)
                new_solution2 = crossbreed(s2, s)
                #Προσθέτω τις νέες υποψήφιες λύσεις στο λεξικό dictionary.
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
        






#Επιστρέφει True αν το string x είναι ακέραιος
def   is_integer(x):
    try:
        y = int(x)
        return True
    except:
        return False
#--------------------------------------

#Επιστρέφει True αν το string x είναι θετικός ακέραιος
def   is_positive_integer(x):
    try:
        y = int(x)
        if y>0:
            return True
        else:
            return False
    except:
        return False
#--------------------------------------



#Επιστρέφει True αν το string x είναι '0' ή '1'
def   is_binary_digit(x):
    try:
        y = int(x)
        if y==0 or y==1:
            return True
        else:
            return False
    except:
        return False
#--------------------------------------


#Επιστρέφει True αν το string x είναι μεταξύ του 0 και του 1
def   is_prob(x):
    try:
        y = float(x)
        if y>=0 and y<=1:
            return True
        else:
            return False
    except:
        return False
#--------------------------------------
    


#tkinter function
def  run_genetic():
    #Καθαρίζω τα προηγούμενα κείμενα αν υπάρχουν.
    result_outpout.delete(0.0,END)
    solutions_outpout.delete(0.0,END)
    
    #ελέγχω αν οι τιμές είναι σωστές
    N_entered = N_entry.get()
    if is_positive_integer(N_entered):
        N = int(N_entered)
    else:
        msg = 'Λάθος τιμή στο πλήθος αρχικών λύσεων'
        result_outpout.insert(END,msg)
        return
    
    K_entered = K_entry.get()
    if  is_positive_integer(K_entered):
        K = int(K_entered)
    else:
        msg = 'Λάθος τιμή στο πλήθος λύσεων επόμενης γενιάς'
        result_outpout.insert(END,msg)
        return
    
    steps_entered = steps_entry.get()
    if  is_positive_integer(steps_entered):
        steps = int(steps_entered)
    else:
        msg = 'Λάθος τιμή στο πλήθος βημάτων'
        result_outpout.insert(END,msg)
        return
    
    type_entered = type_entry.get()
    if  is_binary_digit(type_entered):
        input_type = int(type_entered)
    else:
        msg = 'Λάθος τιμή στον τύπο λύσεων'
        result_outpout.insert(END,msg)
        return
    
    pm_entered = pm_entry.get()
    if  is_prob(pm_entered):
        p_m = float(pm_entered)
    else:
        msg = 'Λάθος τιμή στην πιθανότητα μετάλλαξης'
        result_outpout.insert(END,msg)
        return
    
    
    #Τρέχω τον γενετικό αλγόριθμο
    msg = 'Ο Γεννετικός Αλγόριθμος Ξεκίνησε'
    result_outpout.insert(END,msg)
    start = time.time()
    solutions = genetic_algorithm(N, K, steps, input_type, p_m, printflag=False)
    end = time.time()
    result_outpout.delete(0.0,END)
    msg = 'Ο Γεννετικός Αλγόριθμος Ολοκληρώθηκε! Συνολικός χρόνος: ' + str(end-start) + ' sec'
    result_outpout.insert(END,msg)
    
    #Τύπωσε τις 20 πρώτες λύσεις
    n = 0
    msg = ''
    for s in solutions:
         msg += 'x = '+'{:.4f}'.format(s[0]) + '\t\t' + 'y = ' +'{:.4f}'.format(s[1]) + '\t\t' + 'z = ' + '{:.4f}'.format(s[2]) +   '\t\t value='  +  '{:.2f}'.format(solutions[s]) + '\n'
         n = n + 1 
         if n>19:
             break
    solutions_outpout.insert(END, msg)



#tkinter function
def close_window():
    window.destroy()
    return










#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#Κυρίως πρόγραμμα

#initial values
#N: Πλήθος αρχικών λύσεων (x, y, z) που θα ξεκινήσουν τον αλγόριθμο
N = 5000
#Κ: Πλήθος λύσεων που κρατάει κάθε γενιά (κρατώ τις Κ καλύτερες)
K = 1000
#steps: Βήματα που θα κάνει ο γεννετικός αλγόριθμος
steps = 100
#input_type:  0 για ακέραιους,  1 για πραγματικούς
input_type = 1
#p_m: Πιθανότητα μετάλαξης
p_m = 0.4
#printflag
printflag = False

window = Tk()
window.title("Genetic Algorithm Project")
#labels
N_label = Label(window, text="Πλήθος Αρχικών Λύσεων: ", fg="black", font ="none 14 bold" ) .grid(row=0,  column=0, sticky=W)
K_label = Label(window, text="Πλήθος λύσεων επόμενης γενιάς: ", fg="black", font ="none 14 bold" ) .grid(row=1,  column=0, sticky=W)
steps_label = Label(window, text="Βήματα: ", fg="black", font ="none 14 bold" ) .grid(row=2,  column=0, sticky=W)
type_label = N_label = Label(window, text="Τύπος Λύσεων (0: ακέραιοι, 1: πραγματικοί): ", fg="black", font ="none 14 bold" ) .grid(row=3,  column=0, sticky=W)
pm_label =  Label(window, text="Πιθανότητα Μετάλλαξης: ", fg="black", font ="none 14 bold" ) .grid(row=4,  column=0, sticky=W)



#text entries
N_entry = Entry(window, width=6, bg="white", font="none 14")
N_entry.grid(row=0, column=1, sticky=W)
N_entry.insert(END, N)  #Βάζω αρχική τιμή
K_entry = Entry(window, width=6, bg="white", font="none 14")
K_entry.grid(row=1, column=1, sticky=W)
K_entry.insert(END, K)
steps_entry = Entry(window, width=6, bg="white", font="none 14")
steps_entry.grid(row=2, column=1, sticky=W)
steps_entry.insert(END, steps)
type_entry = Entry(window, width=3, bg="white", font="none 14")
type_entry.grid(row=3, column=1, sticky=W)
type_entry.insert(END, input_type)
pm_entry = Entry(window, width=6, bg="white", font="none 14")
pm_entry.grid(row=4, column=1, sticky=W)
pm_entry.insert(END, p_m)

#Buttons
run_button = Button(window, text="RUN", width=10, font ="none 18 bold", command=run_genetic).grid(row = 15,  column = 0, sticky=W)
exit_button = Button(window, text="EXIT", width=10, font ="none 18 bold", command=close_window).grid(row = 15,  column = 1, sticky=E)

#Outputs!
result_outpout = Text(window, width=100, height=1, wrap=WORD, background="white")
result_outpout.grid(row = 20, column=0, columnspan=2, sticky=W)
space_outpout = Text(window, width=100, height=1, wrap=WORD, background="white")
space_outpout.grid(row = 21, column=0, columnspan=2, sticky=W)
solutions_outpout = Text(window, width=100, height=20, wrap=WORD, background="white")
solutions_outpout.grid(row = 22, column=0, columnspan=2, sticky=W)

#Εδώ τρέχει ο κώδικας για το παράθυρο
window.mainloop()



#console code
# start = time.time()
# solutions = genetic_algorithm(5000, 1000, 200, 1, 0.4, printflag=False)
# end = time.time()
# print('Time needed = ',  end - start)
# n = 0
# for s in solutions:
#     print ('{:.4f}'.format(s[0]) + '\t' '{:.4f}'.format(s[1]) + '\t' + '{:.4f}'.format(s[2]),   '\t\t value=','{:.2f}'.format(solutions[s]) ) 
#     n = n + 1 
#     if n>20:
#         break