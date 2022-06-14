1) https://stackoverflow.com/questions/12583930/use-pipe-for-curl-data

ativar o servidor:
python3 server.py

cliente:
```
$ cat teste.json | curl -H "Content-Type: application/json" -X POST -d @- localhost:5000
```
resultado:
```
{
  "email": "josilva@gmail.com", 
  "nome": "Jo\u00e3o"
}
```

2) https://stackoverflow.com/questions/16640054/minimal-web-server-using-netcat

ativar o servidor:
```
$ while true; do echo -e "HTTP/1.1 200 OK\n\n Obrigado, dados recebidos em $(date)" | nc -l -p 1500 -q 1; done
```

cliente:
```
$ curl -d 'teste: receba meus dados' localhost:1500
```
 
3) https://superuser.com/questions/501218/sending-text-file-contents-to-server-using-netcat

ativar o servidor: idem item 2)

cliente:
```
$ cat exemplo.txt | nc -N localhost 1500
```

