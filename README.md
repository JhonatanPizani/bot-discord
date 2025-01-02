# Discord Bot - Envio de Mensagens Diretas para Cargos Específicos

Este é um bot para Discord que permite enviar mensagens diretas (DMs) para todos os membros de um cargo específico em um servidor. 
Ele é útil para administrar servidores e comunicar-se rapidamente com grupos específicos de usuários.

## Recursos

- Envia mensagens diretas para todos os membros de um cargo especificado.
- Filtra bots para evitar envio desnecessário de mensagens.
- Inclui verificação de permissões para garantir que apenas administradores possam usar o comando.
- Lida com exceções, como membros com DMs fechadas.

## Pré-requisitos

Certifique-se de que você tem:

- [Python 3.8+](https://www.python.org/downloads/) instalado.
- A biblioteca `discord.py` instalada. Você pode instalá-la com o seguinte comando:

  ```bash
  pip install discord.py
  ```

- Um token de bot do Discord. Siga [este guia](https://discord.com/developers/docs/getting-started) para criar um bot e obter o token.

## Configuração

1. Clone este repositório ou copie o script para o seu ambiente local.
2. Insira o token do seu bot na variável `TOKEN` no código.

   ```python
   TOKEN = 'seu-token-aqui'
   ```

3. Certifique-se de que o bot tenha as seguintes permissões no servidor:
   - Gerenciar membros.
   - Enviar mensagens diretas.

4. Execute o script com o seguinte comando:

   ```bash
   python seu_script.py
   ```

## Como Usar

1. Após iniciar o bot, ele estará disponível no servidor.
2. Use o comando `!enviar_dm` com a seguinte sintaxe:

   ```
   !enviar_dm @nome_do_cargo Mensagem que você deseja enviar.
   ```

   - **@nome_do_cargo**: O cargo que receberá as mensagens (ex.: `@Membros`).
   - **Mensagem que você deseja enviar**: O conteúdo da mensagem que será enviada para os membros.

3. O bot enviará as mensagens diretas para todos os membros com o cargo especificado.

## Exemplo

Digite no chat do servidor:

```
!enviar_dm @Staff Atenção, equipe! Temos uma reunião amanhã às 14h.
```

O bot enviará a mensagem "Atenção, equipe! Temos uma reunião amanhã às 14h." para todos os membros com o cargo `Staff`.

## Erros Comuns

- **Discord.Forbidden**: O bot não pode enviar mensagens para membros com DMs fechadas.
- **Rate Limits**: Se muitas mensagens forem enviadas em curto período, o Discord pode aplicar limites. O script já inclui uma pausa de 1 segundo para evitar esse problema.

## Contribuindo

Se você quiser contribuir com este projeto, fique à vontade para abrir um pull request ou relatar problemas na seção de [Issues](#).

## Licença

Este projeto está sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.
