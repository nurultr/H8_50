import pickle
import sys
import numpy as np

def open_pickle_file(file_path):
    model = pickle.load(open(file_path,'rb'))
    return model

def predict_customer_bank(file_path,data_array):
    model = open_pickle_file(file_path)
    prediction_result = model.predict(data_array)
    if prediction_result == 0:
        plot_prediksi = 'Attrited Customer/Churn Customer'
    else:
        plot_prediksi = 'Existing Customer'
    return prediction_result, plot_prediksi

            
def main(file_path,data):
    data_array = np.array(list(data.split(','))).reshape(1,-1)
    prediction_result = predict_customer_bank(file_path,data_array)
    print('Prediction Result: ', prediction_result)
    
if __name__ == '__main__':
    main(sys.argv[1],sys.argv[2])