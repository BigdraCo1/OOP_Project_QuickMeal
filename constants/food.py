from internals.food import Food

Fondue_lal = Food('1',"Fondue",
                       "Food",
                       {"Big":10,"Small": 0},
                       20)

Capuliato_pop = Food('2',"Capuliato",
                          "Drinks",
                          {"Large":20,"Medium":15,"Small":0},
                          35)

maccu_lano = Food('3',"maccu",
                       "Drinks",
                       {"Grande":40, "Large":35,"Small":0},
                       54)

fried_chicken = Food('4',"Fried Chicken",
                          "Food",
                          {"Large":20,"Medium":15,"Small":0},
                          30)

grilled_chicken = Food('5',"Grilled Chicken",
                            "Food",
                            {"Large":20,"Medium":15,"Small":0},
                            30)

italian_dishes1 = [
    Fondue_lal, Capuliato_pop, maccu_lano
]
italian_dishes2 = [
    Fondue_lal
]
italian_dishes3 = [
    Capuliato_pop, maccu_lano
]
italian_dishes4 = [
    Fondue_lal, maccu_lano
]
kfc_dishes = [
    fried_chicken, grilled_chicken
]