
from sklearn.naive_bayes import GaussianNB
from sklearn import tree
from sklearn import datasets
import pickle


wine = datasets.load_wine()
wine.keys()
print(wine)

labels_names = wine.target_names 
pickle.dump(labels_names, open('names.pkl','wb'))
nomeswine = pickle.load(open('names.pkl','rb'))


x = wine.data
y = wine.target

#realizando o split da base para teste
from sklearn.model_selection import train_test_split
x_treino,x_teste,y_treino,y_teste = train_test_split(x,y,test_size=0.3)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(x_treino, y_treino)

preditos = clf.predict(x_teste)
print("Preditos:",preditos)
print("Real    :",y_teste)

from sklearn.metrics import accuracy_score
print("Acuracia:", accuracy_score(y_teste,preditos))

pickle.dump(clf, open('model.pkl','wb'))
model = pickle.load(open('model.pkl','rb'))


