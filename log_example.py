
#dic( date: exercise dic)
#exercise dic( exercise: [sets] )
#[sets] = [(repetitions, weight), (...)]
#[sets] = [(repetitions), (...)] #for calisthenics

#N/9.81m^2
#"dd/mm/yyyy": weight
WEIGHT = {"02/03/2020": 74,
          "02/04/2020": 75}

#"name": weight
WEIGHT_NAMES = {"bar": 20}

#"dd/mm/yyyy": {"exercise": [(weight, number of reps set 1), (weight, number of reps set 2), ... ]}
#or
#"dd/mm/yyyy": {"exercise": [number of reps set 1, number of reps set 2, ...]}

DATA  ={"02/04/2020": { "leg_drops":    [            8,             8,             8],\
                        "dumbell_rows": [("bar", 2*15), ("bar", 2*15), ("bar", 2*17)],\
                        "squats":       [     (60, 20),      (60, 20),      (60, 20)] },
        
        "04/04/2020": { "supermans":     [         15,          15,         15],\
                        "good_mornings": [   (35, 25),    (35, 25),   (35, 30)],\
                        "curls":         [("bar", 17), ("bar", 18), ("bar", 18), ("bar", 20)] },
}
