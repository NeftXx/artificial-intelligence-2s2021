from sklearn.neighbors import NearestCentroid
import numpy as np

x = np.array([[6, 3, 1, 3, 7, 4, 3, 6], [7, 4, 0, 4, 8, 5, 4, 7], [8, 5, 1, 5, 6, 3, 5, 7],
              [7, 4, 2, 4, 8, 5, 4, 7], [8, 5, 1, 5, 7, 4, 5, 8], [
                  7, 4, 0, 3, 4, 2, 0, 0], [8, 5, 0, 3, 5, 1, 0, 0],
              [7, 4, 2, 5, 4, 0, 0, 0]])

y = np.array(['N', 'N', 'N', 'N', 'N', 'P', 'P', 'P'])

clf = NearestCentroid()

clf.fit(x, y)

print(clf.predict([[7, 4, 0, 4, 6, 3, 4, 8]])) # N
print(clf.predict([[7, 4, 0, 3, 4, 2, 0, 0]])) # P
print(clf.predict([[8, 5, 1, 4, 6, 3, 0, 0]])) # P
