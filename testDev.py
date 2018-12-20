import os
os.getcwd()
os.chdir('HeadFirstPython/chapter3')
os.getcwd()
import nester as ns
import pickle

new_man= []

try:

    with open('man_data.txt', 'rb') as man_file:
         new_man = pickle.load(man_file)

except IOError as err:
    print('File Error!', str(err))

except pickle.PickleError as perr:
    print('Pickling error: ' + str(perr))

ns.print_lol(new_man)
