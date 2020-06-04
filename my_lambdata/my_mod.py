from sklearn.model_selection import train_test_split
def enlarge(n):
    """
    Param n is a number 
    Function will enlarge the number 
    """
    return n*100

def train_val_test_split(df):
    
    train, test = train_test_split(df)
    train, val = train_test_split(train)
    return(train, val, test)

class coffee_bag():
    def __init__(self, weightKG, source, variety='Natural'):
        self.weightKG = weightKG
        self.source = source
        self.variety = variety
    
    def weight_to_lbs(self):
        return self.weightKG * 2.204623

    @staticmethod
    def quality_reminder():
        print('Single-origin coffee is always better!')

    @property
    def market(self):
        return 'Commodities'


if __name__ == "__main__":
    print('Hello')
    y = int(input('Please choose a number\n'))
    print(y, enlarge(y))

