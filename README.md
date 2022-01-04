# gRPC-poc em Python

Para executar a aplicação, primeiramente devemos instalar as dependências.
Após realizar o download da aplicação do Git, entrar na pasta do projeto baixado, abrir um terminal e digitar:
    
    pip install -r requirements.txt

Assim que a instalação das dependências concluírem com sucesso, podemos executar a aplicação.

Primeiramente, vamos deixar o server rodando em background. 
De dentro do diretório do projeto execute o seguinte comando no terminal:

    python server.py

Agora abra outro terminal e digite:

    python client.py 100 10000 81 25 100000000 987656328

Você terá o seguinte resultado:

    Square Root of 100 is 10.0
    Square Root of 10000 is 100.0
    Square Root of 81 is 9.0
    Square Root of 25 is 5.0
    Square Root of 100000000 is 10000.0
    Square Root of 987656328 is 31427.0

    
