from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/battle_endpoint", methods=["GET"])
def battle_endpoint():
    # Aqui você precisa chamar a função de batalha e obter os resultados
    # Substitua o código a seguir pela lógica real de batalha e obtenção de resultados
    player1Wins = True
    draw = False

    # Retorne os resultados como uma resposta JSON
    response = {
        "player1Wins": player1Wins,
        "draw": draw
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run()
