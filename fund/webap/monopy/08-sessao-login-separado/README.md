* É preciso executar um servidor web para rodar este projeto.
* Sugestão:

'docker run -p 81:80 -v /home/friend/01-github/dw2ed/fund/webap/monopy/08-sessao-login-separado/front-end/:/usr/share/nginx/html nginx'

O nginx serve páginas na porta 80, mas nós vamos utilizar o servidor no computador na porta 81.
Isso se deve ao fato de que alguns computadores já possuem outro servidor web instalado na porta 80.
Neste exemplo, deve-se acessar o servidor web da seguinte forma:

http://localhost:81/principal.html
