from flask import Flask, request
import csv
from datetime import datetime

app = Flask(__name__)

# Função para capturar cliques no link malicioso simulado
@app.route('/atualizar-senha', methods=['GET'])
def phishing_page():
    user_ip = request.remote_addr  # Captura o IP do usuário
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Captura o horário do clique
    
    # Salvar os dados no arquivo CSV
    with open('resultados.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([user_ip, timestamp, 'Clique no link'])

    return "<h1>Erro ao atualizar senha. Tente novamente mais tarde.</h1>"

if __name__ == '__main__':
    # Execute o servidor Flask na porta 8080
    app.run(host='0.0.0.0', port=8080)
