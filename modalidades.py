from flask import Flask, render_template

app = Flask(__name__)

@app.route('/modalidades')
def ola():
    return render_template('modalidades_lista.html')

app.run()