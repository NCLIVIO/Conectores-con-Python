
# ### Conector Mongodb

# Conector con una base en mongodb

import pandas as pd
from pymongo import MongoClient

cliente = MongoClient ("localhost predeterminado", 27017) # IP del localhost predeterminado, 27017
coleccion = cliente ["Base de datos"] ["Colección"] #Base de Datos - Colección
data = coleccion.find()
data = list (data) # Al convertir a una lista, puede filtrar solo los datos que necesita según la situación. (para filtrado transversal)
 
df = pd.DataFrame (data) # leer la tabla completa (DataFrame)
df.head()


