from flask import Flask, render_template, redirect, request, flash
import requests

app = Flask(__name__)
# Chave secreta para mensagens de flash
app.secret_key = 'void_key_999'

ENDPOINT_API = "https://api.thecatapi.com/v1/images/search"

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/cat', methods=['POST'])
def cat():
    nome = request.form.get('nome', None)

    if not nome:
        flash('O NOME É NECESSÁRIO PARA O RITUAL.')
        return redirect('/')
    
    try:
        resposta = requests.get(ENDPOINT_API)
        dados = resposta.json()
        if dados:
            url_imagem = dados[0]['url']
            return render_template('index.html', nome=nome, url_imagem=url_imagem)
        else:
            flash('O VAZIO NÃO RESPONDEU. TENTE NOVAMENTE.')
    except:
        flash('SISTEMA FORA DO AR. OS GATOS ESTÃO DORMINDO.')
    
    return redirect('/')

if __name__ == '__main__': 
    app.run(debug=True)