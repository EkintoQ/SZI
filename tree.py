import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

from rubbish import *


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
    df = pd.read_excel('trash.xlsx', sheet_name='Sheet1')
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

    # create a decisions tree in terminal
    # model = clf.fit(X, y)
    # text_representation = tree.export_text(clf)
    # print(text_representation)

    clf = clf.fit(x_train, y_train)
    answer = clf.predict([prefer])

    # write results of training to the list
    append_choice(answer, prefer, d, df)

    return answer


def append_df_to_excel(df, excel_path):
    df_excel = pd.read_excel(excel_path)
    result = pd.concat([df_excel, df], ignore_index=True)
    result.to_excel(excel_path, index=False)


def append_choice(answer, prefer, d, df):
    new_row = prefer
    new_row.append(list(d.keys())[list(d.values()).index(int(answer))])
    if new_row[3] == 1:
        new_row[3] = 'paper'
    if new_row[3] == 2:
        new_row[3] = 'wood'
    if new_row[3] == 3:
        new_row[3] = 'glass'
    if new_row[3] == 4:
        new_row[3] = 'metal'
    if new_row[3] == 5:
        new_row[3] = 'plastic'

    if new_row[4] == 1:
        new_row[4] = 'little'
    if new_row[4] == 2:
        new_row[4] = 'medium'
    if new_row[4] == 3:
        new_row[4] = 'huge'
    if new_row[4] == 4:
        new_row[4] = 'large'

    data = {"weight": new_row[0], "density": new_row[1], "fragility": new_row[2], "material": new_row[3],
            "size": new_row[4], "degradability": new_row[5], "renewability": new_row[6], "what to do": new_row[7]}

    n_df = pd.DataFrame(data, index=[len(df) + 1])
    append_df_to_excel(n_df, "trash.xlsx")
