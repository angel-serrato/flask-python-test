from flask import Flask, render_template, request

app = Flask(__name__, static_folder='../front-end/static', template_folder='../front-end/templates')

TIPO_CAMBIO = 4500

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        try:
            cantidad_cop = int(request.form['cantidad_cop'])
            resultado = cantidad_cop / TIPO_CAMBIO
        except ValueError:
            resultado = 'Por favor ingrese un número válido'
    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)