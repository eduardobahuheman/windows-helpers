from flask import Flask, render_template, request

import random

app = Flask(__name__)


# Simulação de uma IA básica para detectar problemas
def diagnose_problem(description):
    # IA pode usar um modelo real ou API GPT
    common_problems = {
        "lento": "O sistema está lento, tente desativar programas em segundo plano e verificar vírus,para isso podemos Desativar programas iniciados com o Windows: Pressione Ctrl + Shift + Esc > vá em Inicializa > desative programas desnecessários,Verificar por malware: Use o Windows Defender ou outro antivírus,Desinstalar programas indesejados: Vá em Configurações > Aplicativos > Aplicativos e recursos,Ajustar as opções de energia: Configurações > Sistema > Energia e suspensão > Configurações adicionais de energia.",
        "tela azul": "Tela azul detecada, tente verificar drivers e possíveis erros de hardware.",
        "crash": "Travamento detectado, verifique as atualizações recentes e a integridade dos arquivos do sistema."
    }

    for key in common_problems:
        if key in description.lower():
            return common_problems[key]

    return "Desculpe, não consegui identificar o problema. Tente mais detalhes."


@app.route('/', methods=['GET', 'POST'])
def index():
    solution = None
    if request.method == 'POST':
        problem_description = request.form['description']
        solution = diagnose_problem(problem_description)

    return render_template('index.html', solution=solution)


if __name__ == '__main__':
    app.run(debug=True)
