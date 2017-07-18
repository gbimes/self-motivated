import pandas as pd


df = pd.read_csv('/EOD-WMT.csv')
print(df.head())


df.fillna(-999.99, inplace=true)
x_train, x_test, y_train, y_test = cross_validation.train_test_split(x,y,test_size = 0.2)

# save classifier in a pickle 
with open('linearregression.pickle', wb) as f:
	pickle.dump(clf, f)


# open saved up classifier 
pickle_in = open('linearregression.pickle','rb')
clf = pickle.load(pickle_in)