# 🤖 Curso Telegram Bot

Projeto de fins **educacionais** criado para aprender e experimentar a **API do Telegram** (Bot API) utilizando Python. O repositório reúne exemplos práticos de bots, desde o fluxo básico de conversação até o uso de teclados inline e gerenciamento de contexto.

> ⚠️ **Aviso:** Este projeto é apenas para aprendizado. Nunca exponha seu token em produção — use variáveis de ambiente!

## 📚 Sobre o Projeto

O objetivo é explorar os principais recursos da [python-telegram-bot](https://docs.python-telegram-bot.org/) (biblioteca que encapsula a **BotAPI** do Telegram) e entender conceitos como:

- Criação de bots via [@BotFather](https://t.me/botfather) (comando `/newbot`)
- **MTProto** — protocolo de criptografia do Telegram que garante segurança, privacidade e alta velocidade
- Handlers de comandos e mensagens
- Conversas multi-etapas (máquina de estados)
- Teclados inline com botões de callback
- Gerenciamento de contexto e dados do usuário

Credenciais e configuração de API em: https://my.telegram.org/

Existem outras libs como por exemplo:
telethon e aiogram
A diferença é que: 

## 🗂️ Estrutura do Projeto

| Arquivo | Descrição |
|---------|-----------|
| [main.py](main.py) | Bot com conversa multi-etapas: pede o nome do usuário e responde comandos como `/start`, `/sobre` e `/help` |
| [bot1.py](bot1.py) | Bot com teclado inline (`InlineKeyboardMarkup`) e botões de callback (Sobre, Ajuda, Contato) |
| [bot_game.py](bot_game.py) | 🚧 Em construção — esqueleto de um bot de jogo |

## 🚀 Como Executar

Pré-requisitos: Python 3.13+ e [uv](https://docs.astral.sh/uv/).

```bash
# Instalar dependências
uv sync

# Rodar o bot desejado
uv run python main.py
uv run python bot1.py
```

Antes de rodar, defina seu token no código ou (recomendado) em uma variável de ambiente `TELEGRAM_BOT_TOKEN`.

## 🔑 Funções e Conceitos Importantes da Documentação do Telegram

Estes são os blocos fundamentais usados neste projeto, presentes na [documentação oficial da Bot API](https://core.telegram.org/bots/api):

### Handlers

| Conceito | Função |
|----------|--------|
| `CommandHandler` | Responde a comandos como `/start`, `/help` |
| `MessageHandler` | Responde a mensagens de texto comuns |
| `CallbackQueryHandler` | Trata cliques em botões inline |
| `filters` | Filtra tipos de mensagem (`filters.TEXT`, `filters.COMMAND`, etc.) |

### Conversação e Contexto

- **`ConversationHandler`** — gerencia conversas multi-etapas como uma máquina de estados (`entry_points`, `states`, `fallbacks`). Use `ConversationHandler.END` para finalizar o fluxo.
- **`ContextTypes.DEFAULT_TYPE`** — dá acesso ao contexto da conversa, incluindo `context.user_data`, um dicionário persistente por usuário.
- **O Problema do Contexto** — é possível gerenciar o contexto a partir de diferentes registros de usuários para controlar o fluxo de interação (cada usuário tem seu próprio estado independente).

### Interface e Mensagens

- **`InlineKeyboardMarkup` / `InlineKeyboardButton`** — criam botões clicáveis abaixo das mensagens, com `callback_data` para identificar a ação.
- **`update.message.reply_text()`** — envia mensagens de texto.
- **`query.answer()`** — confirma o recebimento de um clique em botão (obrigatório em callbacks).
- **`query.edit_message_text()`** — edita a mensagem original após o clique.

### Ciclo de Vida

- **`Application.builder().token(TOKEN).build()`** — constrói a aplicação do bot.
- **`app.run_polling()`** — inicia o bot em modo *long polling* (ideal para desenvolvimento).

## 🤝 Como Contribuir

Contribuições são muito bem-vindas! Como este é um projeto educacional, sugestões didáticas e exemplos comentados são especialmente valiosos.

1. **Faça um fork** do repositório
2. **Crie uma branch** para sua feature:
   ```bash
   git checkout -b feature/minha-nova-feature
   ```
3. **Commit suas mudanças** com mensagens claras:
   ```bash
   git commit -m "feat: adiciona exemplo de bot com teclado ReplyKeyboard"
   ```
4. **Envie para o seu fork**:
   ```bash
   git push origin feature/minha-nova-feature
   ```
5. **Abra um Pull Request** descrevendo o que foi feito e por quê

### Boas Práticas

- ✅ Comente o código — lembre-se de que o público-alvo são pessoas aprendendo
- ✅ Nunca commite tokens ou credenciais reais
- ✅ Siga o padrão de código existente (PEP 8)
- ✅ Teste seu bot antes de abrir o PR

### Ideias de Contribuição

- Finalizar o `bot_game.py` (jogo de adivinhação, quiz, etc.)
- Exemplos com `telethon` (MTProto)
- Tratamento de erros e logging
- Deploy com webhooks

---

Feito com ⭐ por Mateus Bizzo 