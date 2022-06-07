import random

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


def evaluate_values(values):
    data = []
    if values[0] == 10:
        data.append(10)
    elif values[0] == 15:
        data.append(15)
    elif values[0] == 20:
        data.append(20)
    elif values[0] == 30:
        data.append(30)
    elif values[0] == 40:
        data.append(40)
    else:
        data.append(random.choice([10, 15, 20, 30, 40]))

    if values[1] is True:
        data.append(1)
    elif values[1] is False:
        data.append(0)
    else:
        data.append(random.choice([1, 0]))

    if values[2] == 1:
        data.append(1)
    elif values[2] == 2:
        data.append(2)
    elif values[2] == 3:
        data.append(3)
    elif values[2] == 4:
        data.append(4)
    elif values[2] == 5:
        data.append(5)
    elif values[2] == 6:
        data.append(6)
    elif values[2] == 7:
        data.append(7)
    elif values[2] == 8:
        data.append(8)
    elif values[2] == 9:
        data.append(9)
    elif values[2] == 10:
        data.append(10)
    else:
        data.append(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

    if values[3] == 'plastic':
        data.append(5)
    elif values[3] == 'wood':
        data.append(2)
    elif values[3] == 'metal':
        data.append(4)
    elif values[3] == 'glass':
        data.append(3)
    elif values[3] == 'paper':
        data.append(1)
    else:
        data.append(random.choice([1, 2, 3, 4, 5]))

    if values[4] == 'little':
        data.append(1)
    elif values[4] == 'medium':
        data.append(2)
    elif values[4] == 'huge':
        data.append(3)
    elif values[4] == 'large':
        data.append(4)
    else:
        data.append(random.choice([1, 2, 3, 4]))

    if values[5] == 1:
        data.append(1)
    elif values[5] == 2:
        data.append(2)
    elif values[5] == 3:
        data.append(3)
    elif values[5] == 4:
        data.append(4)
    elif values[5] == 5:
        data.append(5)
    elif values[5] == 6:
        data.append(6)
    elif values[5] == 7:
        data.append(7)
    elif values[5] == 8:
        data.append(8)
    elif values[5] == 9:
        data.append(9)
    elif values[5] == 10:
        data.append(10)
    else:
        data.append(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

    if values[6] == 1:
        data.append(1)
    elif values[6] == 2:
        data.append(2)
    elif values[6] == 3:
        data.append(3)
    elif values[6] == 4:
        data.append(4)
    elif values[6] == 5:
        data.append(5)
    elif values[6] == 6:
        data.append(6)
    elif values[6] == 7:
        data.append(7)
    elif values[6] == 8:
        data.append(8)
    elif values[6] == 9:
        data.append(9)
    elif values[6] == 10:
        data.append(10)
    else:
        data.append(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    return data


def trash_selection(prefer):
    df = pd.read_excel('data.xlsx', sheet_name='list1')
    # print(df)

    d = {'paper': 1, 'wood': 2, 'glass': 3, 'metal': 4, 'plastic': 5}
    df['material'] = df['material'].map(d)

    d = {'little': 1, 'medium': 2, 'huge': 3, 'large': 4}
    df['size'] = df['size'].map(d)

    d = {'leave': 0, 'pick up': 1}
    df['what to do'] = df['what to do'].map(d)

    features = ['weight', 'density', 'fragility', 'material', 'size', 'degradability', 'renewability']
    x = df[features]
    y = df['what to do']
    x_train, x_test, y_train, y_test = train_test_split(x, y)

    clf = DecisionTreeClassifier(criterion='entropy')

    # model = clf.fit(X, y)
    # text_representation = tree.export_text(clf)
    # print(text_representation)

    clf = clf.fit(x_train, y_train)

    return clf.predict([prefer])