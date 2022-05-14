from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Fala meu querido(a), pessoa recheada de amor e sentimento"

if __name__ == '__main__':
    app.run()