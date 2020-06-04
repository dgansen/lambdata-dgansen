def enlarge(n):
    """
    Param n is a number 
    Function will enlarge the number 
    """
    return n*100


def train_val_test_split(df):
    from sklearn.model_selection import train_test_split
    train, test = train_test_split(df)
    train, val = train_test_split(train)
    return(train, val, test)


if __name__ == "__main__":
    print('Hello')
    y = int(input('Please choose a number\n'))
    print(y, enlarge(y))

