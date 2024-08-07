# https://testdriven.io/blog/flask-server-side-sessions/
# https://stackoverflow.com/questions/15995919/how-to-use-curl-to-send-cookies/23039038#23039038
# https://flask.palletsprojects.com/en/2.0.x/config/#SECRET_KEY

from datetime import timedelta

from flask import Flask, render_template_string, request, session, redirect, url_for
from flask_session import Session

app = Flask(__name__)

# NOTE: The secret key is used to cryptographically-sign the cookies used for storing
#       the session identifier.
# a chave secreta é usada para assinar com criptografia os cookies
# usados para armazenar o identificador da sessão
app.secret_key = 'palavra-secreta-deve-ser-bem-dificil-$#EWFGHJUI*&DEGBHYJU&Y%T'

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Create and initialize the Flask-Session object AFTER `app` has been configured
server_session = Session(app)

@app.route('/')
def padrao():
    return '''Testando sessão server-side.
    <a href="/set_email">Iniciar</a>'''
    
@app.route('/set_email', methods=['GET', 'POST'])
def set_email():
    if request.method == 'POST':
        # Save the form data to the session object
        session['email'] = request.form['email_address']
        return 'OK, <a href="/get_email">verifique</a> se o valor está gravado na sessão.'
        # return redirect(url_for('get_email'))

    return """
        <form method="post">
            <label for="email">Informe seu email:</label>
            <input type="email" id="email" name="email_address" required />
            <button type="submit">Enviar</button
        </form>
        """

@app.route('/get_email')
def get_email():
    return render_template_string("""
            {% if session['email'] %}
                <h1>Bem vindo {{ session['email'] }}!</h1>
            {% else %}
                <h1>Bem vindo! Informe seu email: <a href="{{ url_for('set_email') }}">aqui.</a></h1>
            {% endif %}
        """)


@app.route('/delete_email')
def delete_email():
    # Clear the email stored in the session object
    session.pop('email', default=None)
    return '<h1>Sessão removida!</h1>'


if __name__ == '__main__':
    app.run(debug=True)

# teste via curl:
# curl localhost:5000/set_email -X POST -d "email_address=hvescovi@hotmail.com" -c /tmp/cookie
# curl -b "/tmp/cookie"  localhost:5000/get_email    