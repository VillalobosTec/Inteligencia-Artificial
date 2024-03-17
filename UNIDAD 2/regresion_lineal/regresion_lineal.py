import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

# hice esta madre porque los data sets no jalaban como debia
try:
    df = pd.read_csv(r'UNIDAD 2\regresion_lineal\spotify.csv', encoding='utf-8')
    print('soy utf-8')
except UnicodeDecodeError:
    try:
        df = pd.read_csv(r'UNIDAD 2\regresion_lineal\spotify.csv', encoding='latin1')
        print('soy latin1')
    except UnicodeDecodeError:
        try:
            df = pd.read_csv(r'UNIDAD 2\regresion_lineal\spotify.csv', encoding='ISO-8859-1')
            print('soy ISO-8859-1')
        except UnicodeDecodeError:
            df = pd.read_csv(r'UNIDAD 2\regresion_lineal\spotify.csv', encoding='cp1252')
            print('soy cp1252')

print(df.describe())  
print(df.isnull().sum())  
df.dropna(inplace=True)

X = df[['danceability_%', 'energy_%', 'valence_%']]


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


X_train, X_test = train_test_split(X_scaled, test_size=0.2, random_state=42)

kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X_train)

#aqui muestro con clusteres la agrupacion de las canciones, es decir, 
#que separo en 3 los clusteres para representar danceability, energy, valence, esto de manera 
#en que podamos ver la cantidad de canciones pertenecen a la cada seccion.
plt.scatter(X_train[:, 0], X_train[:, 1], c=kmeans.labels_, cmap='viridis')
plt.title('Spotify')
plt.xlabel('Danceability') 
plt.ylabel('Energy')
plt.show()
