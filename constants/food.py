from internals.food import Food

Fondue_lal = Food("auto", 
                  "Fondue",
                  "Food",
                  {"Big": 10, "Small": 0},
                  20)

Fondue_lal1 = Food("auto",
                  "Fondue",
                  "Food",
                  {"Big": 10, "Small": 0},
                  210)

Capuliato_pop = Food("auto", "Capuliato","Drinks",
                          {"Large": 20, "Medium": 15, "Small": 0},
                          315)

Capuliato_pop1 = Food("auto", "Capuliato","Drinks",
                          {"Large": 20, "Medium": 15, "Small": 0},
                          35)


maccu_lano = Food("auto", "maccu",
                       "Drinks",
                       {"Grande":40, "Large":35,"Small":0},
                       514)

maccu_lano2 = Food("auto", "maccu",
                       "Drinks",
                       {"Grande":40, "Large":35,"Small":0},
                       54)

tomyum = Food("auto", "Tom yum kung", "Food", {"Large":47, "Small":8}, 45)

italian_dishes1 = [
    Fondue_lal, Capuliato_pop, maccu_lano
]
italian_dishes2 = [
    Fondue_lal1
]
italian_dishes3 = [
    Capuliato_pop1, maccu_lano2
]
italian_dishes4 = [
    tomyum
]

fried_chicken = Food("auto",
                     "Fried Chicken",
                     "Food",
                     {"Large":20,"Medium":15,"Small":10},
                     30
)

grilled_chicken = Food("auto",
                       "Grilled Chicken",
                       "Food",
                       {"Large":20,"Medium":15,"Small":10},
                       30
)

kfc_dishes = [
    fried_chicken, grilled_chicken
]