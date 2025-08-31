import json
import pickle
import numpy as np  
__locations = None
__data_columns = None
__model = None

def get_estimated_price(location, sqft, bhk, bath):
    loc_index = __data_columns.index(location.lower())

    x = np.zeros(len(X.columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
    return __model.predict([x])
def get_location_names():
    return __locations

def load_saved_artifacts():
    print("Loading saved artifacts...")
    global __data_columns
    global __locations

    with open('server/artifacts/columns.json', 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]
    
    with open('server/artifacts/banglore_home_prices_model.pickle', 'rb') as f:
        global __model
        __model = pickle.load(f)
    print("Artifacts loaded successfully")

if __name__ == "__main__":
    load_saved_artifacts()
    print(get_location_names())