import pickle
import json
import pandas as pd
import numpy as np
import config


class CerealRating():
    def __init__(self,mfr,types,calories,protein,fat,sodium,fiber,carbo,sugars, potass,shelf,cups,name):
        self.mfr = mfr
        self.types = types
        self.calories = calories
        self.protein = protein
        self.fat = fat
        self.sodium = sodium
        self.fiber = fiber
        self.carbo = carbo
        self.sugars = sugars
        self.potass = potass
        self.shelf = shelf
        self.cups = cups
        
        self.name = "name_" + name
        
    def load_file(self):
        with open (config.PICKLE_FILE_PATH,'rb') as f:
            self.cereal_model = pickle.load(f)

        with open (config.JSON_FILE_PATH,'r') as f:
            self.cereal_data = json.load(f)

    def get_predicted_rating(self):
        self.load_file()  #calling mehtod
        
        name_index = self.cereal_data['columns'].index(self.name)

        array = np.zeros(len(self.cereal_data["columns"]))

        array[0] = self.cereal_data["mfr_dict"][self.mfr]
        array[1] = self.cereal_data["type_dict"][self.types]
        array[2] = self.calories
        array[3] = self.protein
        array[4] = self.fat
        array[5] = self.sodium
        array[6] = self.fiber
        array[7] = self.carbo
        array[8] = self.sugars
        array[9] = self.potass
        array[10] = self.shelf
        array[11] = self.cups
        array[name_index] = 1
        
        
        print("Array -->",array)
        predicted_rating = self.cereal_model.predict([array])[0]
        return np.around(predicted_rating, 2)


if __name__ == "__main__":
    mfr = 'K'
    types = 'H'
    calories = 110
    protein = 4
    fat = 2
    sodium = 130
    fiber= 1.5
    carbo = 5
    sugars = 6
    potass = 87.5
    shelf = 3
    cups = 1.22
    name = 'Wheat Chex'


    cr = CerealRating(mfr,types,calories,protein,fat,sodium,fiber,carbo,sugars, potass,shelf,cups,name)
    rating = cr.get_predicted_rating()
    print(f"predicted cereal rating is {rating} %")