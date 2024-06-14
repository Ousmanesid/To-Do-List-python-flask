from flask import Flask, render_template, request, redirect, url_for
import todo_controller as controller
import datetime

app = Flask(__name__)



@app.route('/')
def index():
    tasks = controller.get_all_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/ajouter', methods=('POST',))
def ajouter():
    titre = request.form['titre']
    description = request.form['description']
    controller.add_task(titre, description)
    return redirect(url_for('index'))

@app.route('/supprimer/<int:id>')
def supprimer(id):
    controller.delete_task(id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)