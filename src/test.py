import sys

class test:
   def  __init__(self):
        self.my_string = sys.stdin.read()

   def get_val(self):
       return self.my_string

def get_my_var():
    return sys.argv[1]


def do_some_things(x):
    print('nanana')
    print('doing something')
    return x

x = lambda a : sys.argv[a]

my_var = x(1)

var2 = do_some_things(my_var)

t = test()

mx = t.get_val()

argumenty = sys.argv[1]
# eval(sys.arv[1])

daj_mi_te_argumenty_ty_lambdo = lambda x : argumenty

val2 = mx.strip()
val3 = val2.upper()
#my_var =  get_my_var()
run_it = eval

def check_it(arg):
    print("checking arg...{}".format(arg))

def finish_it(arg):
    print("finishing pipeline with arg: {}".format(arg))

actions = [
    check_it,
    run_it,
    finish_it
]

params = [
    val3,
    sys.argv[1],
    argumenty,
    daj_mi_te_argumenty_ty_lambdo(2)
]

for param in params:
    for action in actions:
        action(param)

