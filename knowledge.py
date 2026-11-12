
from sympy import symbols, Not, Implies, Xor
from sympy.logic.inference import satisfiable

Rain = symbols('Rain')
Harry_visited_Hagrid = symbols('Harry_visited_Hagrid')
Harry_visited_Dumbledore = symbols('Harry_visited_Dumbledore')
Peter_visits_MJ = symbols('Peter_visits_MJ')
Peter_visits_Gwen = symbols('Peter_visits_Gwen')

def run_test(test_name, kb):
    print(test_name)
    result = satisfiable(kb)
    print("Satisfiable:", result)

    if result is False:
        print("The knowledge base is unsatisfiable")
    elif Rain in result:
        print("The knowledge base is satisfiable")

        if result[Rain]:
            print("It rained today")
        else:
            print("No rain today")
    else:
        print("Rain undetermined")

kb = (
    Implies(Not(Rain), Harry_visited_Hagrid)
    & Xor(Harry_visited_Hagrid, Harry_visited_Dumbledore)
    & Harry_visited_Dumbledore
)

run_test("INPUT", kb)
