from sklearn.naive_bayes import GaussianNB
from sklearn import preprocessing
from sklearn.neural_network import MLPClassifier


alt = ["Yes", "Yes", "No", "Yes", "Yes", "No",
       "No", "No", "No", "Yes", "No", "Yes"]
bar = ["No", "No", "Yes", "No", "No", "Yes",
       "Yes", "No", "Yes", "Yes", "No", "Yes"]
fri = ["No", "No", "No", "Yes", "Yes", "No",
       "No", "No", "Yes", "Yes", "No", "Yes"]
hun = ["Yes", "Yes", "No", "Yes", "No", "Yes",
       "No", "Yes", "No", "Yes", "No", "Yes"]
pat = ["Some", "Full", "Some", "Full", "Full", "Some",
       "None", "Some", "Full", "Full", "None", "Full"]
price = ["$$$", "$", "$", "$", "$$$", "$$", "$", "$$", "$", "$$$", "$", "$"]
rain = ["No", "No", "No", "Yes", "No", "Yes",
        "Yes", "Yes", "Yes", "No", "No", "No"]
res = ["Yes", "No", "No", "No", "Yes", "Yes",
       "No", "Yes", "No", "Yes", "No", "No"]
type = ["French", "Thai", "Burger", "Thai", "French", "Italian",
        "Burger", "Thai", "Burger", "Italian", "Thai", "Burger"]
est = ["0-10", "30-60", "0-10", "10-30", "60", "0-10",
       "0-10", "0-10", "60", "10-30", "0-10", "30 -60"]
goal = ["Yes", "No", "Yes", "Yes", "No", "Yes",
        "No", "Yes", "No", "No", "No", "Yes"]

alt_transform = preprocessing.LabelEncoder().fit_transform(alt)
bar_transform = preprocessing.LabelEncoder().fit_transform(bar)
fri_transform = preprocessing.LabelEncoder().fit_transform(fri)
hun_transform = preprocessing.LabelEncoder().fit_transform(hun)
pat_transform = preprocessing.LabelEncoder().fit_transform(pat)
price_transform = preprocessing.LabelEncoder().fit_transform(price)
rain_transform = preprocessing.LabelEncoder().fit_transform(rain)
res_transform = preprocessing.LabelEncoder().fit_transform(res)
type_transform = preprocessing.LabelEncoder().fit_transform(type)
est_transform = preprocessing.LabelEncoder().fit_transform(est)
goal_transform = preprocessing.LabelEncoder().fit_transform(goal)
features = list(zip(alt_transform, bar_transform, fri_transform, hun_transform, pat_transform,
                price_transform, rain_transform, res_transform, type_transform, est_transform))
model = GaussianNB()
model.fit(features, goal_transform)
test = [
    [1, 0, 0, 1, 2, 2, 0, 1, 1, 0],
    [1, 0, 0, 1, 0, 0, 0, 0, 3, 2],
    [0, 1, 0, 0, 2, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 1, 0, 3, 1],
    [1, 0, 1, 0, 0, 2, 0, 1, 1, 3],
    [0, 1, 0, 1, 2, 1, 1, 1, 2, 0],
    [0, 1, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 2, 1, 1, 1, 3, 0],
    [0, 1, 1, 0, 0, 0, 1, 0, 0, 3],
    [1, 1, 1, 1, 0, 2, 0, 1, 2, 1],
    [0, 0, 0, 0, 1, 0, 0, 0, 3, 0],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 2]
]
predicted = model.predict(test)

A = [0, 0, 0, 0, 1, 1, 1, 1]
B = [0, 0, 1, 1, 0, 0, 1, 1]
C = [0, 1, 0, 1, 0, 1, 0, 1]
features = list(zip(A, B, C))
target = [0, 1, 1, 0, 1, 0, 1, 0]
clf = MLPClassifier(solver='lbfgs', alpha=1e-5, activation='logistic',
                    hidden_layer_sizes=(5,), random_state=1,
                    max_iter=200)
clf.fit(features, target)
test = [
    [0, 0, 0],
    [0, 0, 1],
    [0, 1, 0],
    [0, 1, 1],
    [1, 0, 0],
    [1, 0, 1],
    [1, 1, 0],
    [1, 1, 1]
]
predicted = clf.predict(test)
print('Predictions:', *predicted, sep=' ')
