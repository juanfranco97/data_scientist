import random
import collections
from bokeh.plotting import figure, show
# Además de lo visto en clase tuve que importar lo siguiente:
from bokeh.models import ColumnDataSource, Label, LabelSet, FixedTicker

def tirar_dados(numero_de_tiros):
    secuencia_de_tiros = []

    for _ inrange(numero_de_tiros):
        tiro1 = random.choice([1,2,3,4,5,6])
        tiro2 = random.choice([1,2,3,4,5,6])
        secuencia_de_tiros.append(tiro1 + tiro2)

    return secuencia_de_tiros

if __name__ == "__main__":
    numero_de_tiros = 10000
    secuencia_de_tiros = tirar_dados(numero_de_tiros)
    
    counter = dict(collections.Counter(secuencia_de_tiros))

    x = list(counter.keys())
    y = list(counter.values())
    
    # Las etiquetas solo pueden editarse usando un tipo "ColumnDataSource"que básicamente
    # es una estructura de datos que surge de dictionary. En el "ColumnDataSource"se listan
    # las especificaciones quenoestán incluidas por default.
    source = ColumnDataSource(dict(x = x, y = y))

    grafica = figure(title='Distribucióndela suma de los resultados de lanzar dos dados',
        x_axis_label='Resultados',
        y_axis_label='Número de incidencias')

    # Si ya creaste un "ColumnDataSource" tambiénse puede usar para crear gráficas.
    grafica.vbar(source=source,x='x',top='y',width=0.75)

    # Esto solo es para quela escala en el eje dela x sea igual que los valores de los
    # resultados de los lanzamientos de dados.
    grafica.xaxis.ticker = FixedTicker(ticks=x)

    # Aquí es donde se especifica el label haciendo referencia al "ColumnDataSource".
    labels = LabelSet(
        x='x',
        y='y',
        text='y',
        level='glyph',
        source=source,
        text_align='center')
    
    # Aquí añadimos los labels a lagráfica.
    grafica.add_layout(labels)

    show(grafica)```

Y aquí están las fuentes:
[Stackoverflow: hos to add data labels](https://stackoverflow.com/questions/39401481/how-to-add-data-labels-to-a-bar-chart-in-bokeh)
[Para ajustar el eje x](https://docs.bokeh.org/en/latest/docs/reference/models/axes.html)
[Sobre como configurar LabelSet](https://docs.bokeh.org/en/latest/docs/reference/models/annotations.html)