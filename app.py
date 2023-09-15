from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        print("Dados recebidos: E-mail -> {} Senha -> {}".format(email, senha))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)