import train
import generate

class Model():
    prefix_count = 2
    way = 'model'
    dict = {}
    seed = ''
    random_seed = 21
    def __init__(self, prefix_count):
        self.prefix_count = prefix_count
    def fit(self, data = 'data'):
        train.fit(self.prefix_count,data)

    def generate(self,seed = '', length = 20, random_seed = 21):
        self.seed = seed
        self.random_seed = random_seed
        self.length = length
        self.dict = generate.load_model(self.way)
        generate.generate(self.seed, self.length,self.dict,self.prefix_count,self.random_seed)


print("Please enter the number of words in the prefix")
model = Model(int(input()))
print("Enter the name of the data folder to train model")
model.fit(str(input()))
print("Enter first ", model.prefix_count, "words of generating text or leave it empty(the beginning of text will be chosen randomly)")
prefix = input()
print("Enter length of generating text")
length = int(input())
print("Enter the random seed")
random_seed = int(input())
model.generate(prefix,length,random_seed)
