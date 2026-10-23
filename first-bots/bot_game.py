import os
from dotenv import load_dotenv
from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

from telegram.ext import (
    Application,
    CallbackQueryHandler, # Para lidar com cliques em botões inline
    CommandHandler,
    ContextTypes,
    MessageHandler,
    ConversationHandler,
    filters
)

load_dotenv()

# Projeto para criar um bot de jogo interativo
# o usuário pode jogar Rock, Paper, Scissors (Pedra, Papel, Tesoura)
# ou jogar dados (rolar um dado virtual).

NOME, = range(1)
TOKEN = os.getenv("TOKEN")

async def start (update: Update,
                 context: ContextTypes.DEFAULT_TYPE
):
    await update.message.reply_text("Olá! Eu sou seu bot de jogo interativo.\
                                    \nQual o seu nome?")

    return NOME

async def receber_nome(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
):
    context.user_data["nome"] = update.message.text
    await update.message.reply_text(f"Prazer em te conhecer, {context.user_data['nome']}! 😎")
    await update.message.reply_text("Você pode escolher um jogo: Rock, Paper, Scissors (Pedra, Papel, Tesoura) ou rolar um dado virtual!")

    keyboard = [
        [InlineKeyboardButton("Rock, Paper, Scissors", callback_data="rps")],
        [InlineKeyboardButton("Roll Dice", callback_data="dice")]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Escolha um jogo:", reply_markup=reply_markup)

    return ConversationHandler.END

async def button(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
):
    query = update.callback_query
    await query.answer()

    if query.data == "rps":
        await query.edit_message_text(text="Você escolheu Rock, Paper, Scissors!")
    elif query.data == "dice":
        await query.edit_message_text(text="Você escolheu Roll Dice!")


def main():
    if not TOKEN:
        raise RuntimeError("TOKEN não encontrado.")

    app = Application.builder().token(TOKEN).build()

    conversa = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            NOME: [MessageHandler(filters.TEXT & ~filters.COMMAND, receber_nome)]
        },
        fallbacks=[]
    )

    app.add_handler(conversa)
    app.add_handler(CallbackQueryHandler(button))

    print("Executando bot de jogo interativo...")
    app.run_polling()


if __name__ == "__main__":
    main()