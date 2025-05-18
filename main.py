from flask import Flask, request, render_template

app = Flask(__name__)

def sumar(a, b):
    return a + b

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        try:
            a = float(request.form['a'])
            b = float(request.form['b'])
            resultado = sumar(a, b)
        except ValueError:
            resultado = 'Por favor, ingresa números válidos.'
    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run()


