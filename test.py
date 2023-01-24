#import data_preprocessing_lr_model as dp
import pickle


#m = dp.DataPreprocessingLrModel("ai4i2020.csv","Air temperature [K]","UDI")
#m.build_regression(train_size_=0.2, type="lasso")
#m.get_profile_report()
#print(m.predict(['L55331','L',310.7,1472,40.9,104,0,0,0,0,0,0]))
#pickle.dump(m,open("linear_model.pickle",'wb'))
loaded_model = pickle.load(open("linear_model.pickle", 'rb'))
print(loaded_model.predict(['L55331','L',310.7,1472,40.9,104,0,0,0,0,0,0]))