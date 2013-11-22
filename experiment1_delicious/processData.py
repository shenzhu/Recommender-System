import random

def loadData():
    """
    load delicious data, returns a data list
    data:[[time, userID, url, tag],
          [time, userID, url, tag],
          [time, userID, url, tag],
          ......]
    """
    f = open("delicious.txt")

    data = []

    for line in f:
        next = line.split()

        # preprocess data, delete the item that do not have a tag
        if len(next) < 4:
            pass
        else:
            data.append(next)

    f.close()

    return data


def splitData(data, m):
    """
    split the data into training set and test set
    """
    test = []
    train = []
    random.seed(1)

    for item in data:
        if random.randint(0, m) == 1:
            test.append(item)
        else:
            train.append(item)

    return train, test


def getRecord(train):
    """
    return a dict: record
    record:{i: [user, item, tag],
            i: [user, item ,tag],
            ......}
    """
    record = {}
    i = 0

    for entry in train:
        user = entry[1]
        item = entry[2]
        tag = entry[3]

        record[i] = [user, item, tag]

        i = i + 1

    return record


def addValueToMat(dic, a, b):
    """
    help function
    """
    if a not in dic:
        dic[a] = {}
        dic[a][b] = 1
    elif b not in dic[a]:
        dic[a][b] = 1
    else:
        dic[a][b] += 1

    return dic


def initStat(record):
    user_tags = {}
    tag_items = {}
    user_items = {}

    for i in range(0, len(record)):
        entry = record[i]
        user = entry[0]
        item = entry[1]
        tag = entry[2]

        addValueToMat(user_tags, user, tag)
        addValueToMat(tag_items, tag, item)
        addValueToMat(user_items, user, item)

    return user_tags, tag_items, user_items
