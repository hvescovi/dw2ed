from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def padrao():
    return 'flask web server recebendo parâmetros get, post e json'
    
@app.route('/recebe_get', methods=['GET'])
def recebe_get():
    if request.method == 'POST':
        

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