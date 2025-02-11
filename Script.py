import pandas as pd

materia_1 = []
materia_2 = []
materia_3 = []
resultado = []

for mat1 in range(11):
    for mat2 in range(11):
        for mat3 in range(11):
            r = (mat1*4 + mat2*3 + mat3*3)
            if r>=70 and mat3>=4 and mat1>=4 and mat2>=4:
                materia_1.append(f'{mat1} x 4 = {mat1*4}')
                materia_2.append(f'{mat2} x 3 = {mat2*3}')
                materia_3.append(f'{mat3} x 3 = {mat3*3}')
                resultado.append(r)

df = pd.DataFrame({
    "Materia_1": materia_1,
    "Materia_2": materia_2,
    "Materia_3": materia_3,
    "Resultado": resultado
})

df.to_excel("resultados.xlsx", index=False)

print("Archivo Excel generado correctamente: resultados.xlsx")
