<h1>Spy Python</h1>

<h4>
Este código implementa um servidor TCP que fica escutando indefinidamente por conexões de clientes.
Cada vez que um cliente se conecta e envia dados (uma imagem em formato BMP), o servidor recebe esses dados,
salva como um arquivo na pasta 'screenshots' com um nome sequencial (received_screenshot_1.bmp, received_screenshot_2.bmp, etc)
e permanece ativo para aceitar novas conexões até que seja encerrado manualmente pelo usuário.

Funcionalidades principais:
- Aceita conexões TCP na porta 8888 (por padrão) e no IP 0.0.0.0 (todas interfaces).
- Recebe dados binários enviados pelo cliente e salva como arquivo BMP.
- Mantém o servidor rodando continuamente para múltiplas conexões.
- Cria uma pasta 'screenshots' para armazenar as imagens recebidas.
- Encerra o servidor de forma limpa ao pressionar Ctrl+C
- Entretanto, uma vez compilado para um executável, há a possibilidade do programar rodar em "background" sem o usuário saber.
</h4>
