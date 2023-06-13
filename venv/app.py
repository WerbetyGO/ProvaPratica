from flask import Flask, render_template, request, redirect

app = Flask(__name__)

pets = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastrar-pet', methods=['GET', 'POST'])
def cadastrar_pet():
    if request.method == 'POST':
        nome = request.form['nome']
        idade = request.form['idade']
        pets.append({'nome': nome, 'idade': idade})
        return redirect('/listar-cadastro')
    return render_template('cadastrar_pet.html')

@app.route('/editar-cadastro/<int:pet_id>', methods=['GET', 'POST'])
def editar_cadastro(pet_id):
    if request.method == 'POST':
        nome = request.form['nome']
        idade = request.form['idade']
        pets[pet_id]['nome'] = nome
        pets[pet_id]['idade'] = idade
        return redirect('/listar-cadastro')
    pet = pets[pet_id]
    return render_template('editar_cadastro.html', pet=pet)

@app.route('/ver-cadastro/<int:pet_id>')
def ver_cadastro(pet_id):
    pet = pets[pet_id]
    return render_template('ver_cadastro.html', pet=pet)

@app.route('/listar-cadastro')
def listar_cadastro():
    return render_template('listar_cadastro.html', pets=pets)

@app.route('/excluir-pet/<int:pet_id>')
def excluir_pet(pet_id):
    pets.pop(pet_id)
    return redirect('/listar-cadastro')

if __name__ == '__main__':
    app.run(debug=True)
