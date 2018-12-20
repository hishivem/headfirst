import os
os.getcwd()
os.chdir('HeadFirstPython/chapter3')
os.getcwd()
import pickle


def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (min, sec) = time_string.split(splitter)
    return(min + '.' + sec)

def get_with_sorted(file):

    try:
        with open(file) as fl:
            data = fl.readline();
            templ = data.strip().split(',');

        return(AthleteList(templ.pop(0),templ.pop(0),templ))

    except IOError as err:
        print('File Error!', str(err))

    except pickle.PickleError as perr:
        print('Pickling error: ' + str(perr))

class AthleteList(list):

    def __init__(self, a_name, a_dob=None, a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)

    def top3(self):
        return(sorted(set([sanitize(each_t) for each_t in self]))[0:3])

def sorting_name_wise(list):

    with open(list) as li:
        data = li.readline()
        split_data = data.split(',')
    return(split_data)

james = get_with_sorted('james2.txt');
julie = get_with_sorted('julie2.txt');
mikey = get_with_sorted('mikey2.txt');
sarah = get_with_sorted('sarah2.txt');

print(james.name + "'s fastest times are: '" + str(james.top3()))
print(julie.name + "'s fastest times are: '" + str(julie.top3()))
print(mikey.name + "'s fastest times are: '" + str(mikey.top3()))
print(sarah.name + "'s fastest times are: '" + str(sarah.top3()))
