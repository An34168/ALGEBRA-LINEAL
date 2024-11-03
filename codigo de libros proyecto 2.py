import pandas as pd
df = pd.read_csv(r'C:\Users\Janeth Yanez\OneDrive\Documentos\TRABAJOS DE DISEÑO 3D\PROYECTOS DE PYTHON\books-en.csv', encoding='latin1', delimiter=';')
количество_длинных_названий = df[df['Book-Title'].str.len() > 30].shape[0]
print(f'Количество записей, у которых поле "Book-Title" длиннее 30 символов: {количество_длинных_названий}')


