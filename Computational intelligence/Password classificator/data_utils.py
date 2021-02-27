from csv import reader
from csv import writer
import numpy as np


def adjust_file (input_file_name, output_file_name ):
    csv_out = open(output_file_name, "w",encoding="utf8",newline='')
    csv_writer = writer(csv_out)
    lines = list()

    with open(input_file_name, 'r',encoding="utf8") as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        # Iterate over each row in the csv using reader object
        for row in csv_reader:
            lines.append(row)
            if (len(row) >2):
                lines.remove(row)

    csv_writer.writerows(lines)
    csv_out.close()

def print_predictions(predictions, test_set):
    i = 0
    for pred in predictions:
        pwd = test_set.iloc[i, 0]
        strength = test_set.iloc[i, 1]
        print(pwd, "-", strength, "=>", pred)
        i = i + 1

''' test_ratio: Define the size of test data (usually 20% of dataset) '''
def split_train_test(data, test_ratio):
    ''' permutation: Randomly permute a sequence or return a permuted range (ndarray).
                    If x is a multi-dimensional array, it is only shuffled along its first index.'''
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[:test_set_size] #return the “x-first” values
    train_indices = shuffled_indices[test_set_size:] # return the rest of the dataset
    return data.iloc[train_indices], data.iloc[test_indices] #iloc enables to set dataset based on integer index

