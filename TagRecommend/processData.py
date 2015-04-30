import random
import datetime
from math import log

def loadData(file):
    """
    load data from dataset and process rawdata, for some lines
    int the original data does not have tag;
    returns a list containing the processed data;
    data:[[time, user, url, tag],
          [time, user, url, tag],
          [time, user, url, tag]
          ......]
    """
    # open file
    f = open(file)

    data = []

    for line in f:
        next = line.split()

        # process data, delete the item that does not have tag
        if len(next) < 4:
            pass
        else:
            data.append(next)

    # close file
    f.close()

    return data


def splitData(data, m):
    """
    split the data into training set and test set;
    return two lists: train and test;
    train:[[time, user, url, tag],
           [time, user, url, tag],
           ......]
    test: [[time, user, url, tag],
           [time, user, url, tag],
           ......]
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


def getRecord(data):
    """
    process data, make a dict to manipulate data more easily;
    input can be data, train or test;
    return a dict: record
    record:{i: [user, item, tag],
            i: [user, item, tag],
            .......}
    """
    record = {}
    i = 0

    for item in data:
        user = item[1]
        url = item[2]
        tag = item[3]

        record[i] = [user, url, tag]

        i = i + 1

    return record


def addValueToMat(dic, a, b):
    """
    help function for initStat;
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
    """
    process data, generate three dicts;
    return three dicts: user_tags, tag_items, user_items;
    user_tags: {user: {tag: i},
                      {tag: i},
                      ...
                user: {tag, i},
                      {tag, i},
                      ...
                ......}
    tag_items: {tag: {item: i},
                     {item: i},
                     ...
                tag: {item: i},
                     {item: i},
                     ...
                ......}
    user_items: {user: {item: i},
                       {item: i},
                       ...
                 user: {item: i},
                       {item: i}
                       ...
                 ......}
    """
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


def getTagFre(train):
    """
    calculate how many differenct users have used one particular tag;
    needs user_tags as global variable;
    return a dict tagFre;
    tagFre: {tag: number,
             tag: number,
             tag: number,
             ......}
    """
    tagFre = {}

    for item in train:
        user = item[1]
        tag = item[3]

        if tag not in tagFre.keys():
            tagFre[tag] = 1
        elif user_tags[user][tag] > 1:
            pass
        else:
            tagFre[tag] += 1

    return tagFre


def getItemFre(train):
    """
    calculate how many different users have tagged one particular item;
    needs user_items as global variable;
    return a dict itemFre;
    itemFre: {item: number,
              item: number,
              item: number,
              .......}
    """
    itemFre = {}

    for entry in train:
        user = entry[1]
        item = entry[2]

        if item not in itemFre.keys():
            itemFre[item] = 1
        elif user_items[user][item] > 1:
            pass
        else:
            itemFre[item] += 1

    return itemFre
