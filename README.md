README
hice este proyecto un viernes a la noche, pensando en como podia tener optimizados y chequeados mis gastos,
entonces quise crear este experimento el cual ire actualizando para automatizarlo lo maximo posible pero,
la mayoria de los bancos y wallets en argentina no ofrecen APIs abiertas (mercado pago tiene pero solo para
vendedores),pero algunos bancos y wallets te envian gmails a la hora de haber realizado un pago, en alguna actualizacion 
algun scrip podra hacer algo de ese estilo con esos datos y automatizarlo lo maximo posible.


Qué hace
Lee los movimientos desde gastos.csv
Elimina filas duplicadas
Imprime en consola el total gastado, el total por categoría y el top 3 de gastos más grandes
Muestra un gráfico de barras con el gasto por categoría
Requisitos
Python 3.9 o superior
pandas y matplotlib
bash
pip install pandas matplotlib
Cómo usarlo
Cloná el repo y entrá a la carpeta del proyecto:
bash
   cd analizador-gastos
Copiá el archivo de ejemplo con el nombre que espera el script:
bash
   # Windows
   copy gastos_ejemplo.csv gastos.csv

   # Linux / Mac
   cp gastos_ejemplo.csv gastos.csv
Corré el script:
bash
   python analizar.py

Para usar tus propios gastos, editá gastos.csv (o reemplazalo por tus movimientos exportados del banco o la billetera virtual).

Formato del CSV

El archivo tiene que tener estas cuatro columnas:

columna	ejemplo
fecha	2026-10-15
descripcion	Coto
monto	21000
categoria	supermercado

Tip: escribí las categorías siempre igual (salidas, no Salidas ni salida), porque el script las agrupa por texto exacto.

Privacidad

gastos.csv está en el .gitignore, así que tus gastos reales no se suben al repositorio. Solo se versiona gastos_ejemplo.csv, que tiene datos inventados.
