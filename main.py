import os
from telegram import Update
from dotenv import load_dotenv
load_dotenv()

from telegram.ext import (
    Application, # Para criar a aplicação do bot
    CommandHandler, # Para lidar com comandos como /start e /curse
    ContextTypes, # Para acessar o contexto da conversa
    MessageHandler, # Para lidar com mensagens de texto
    ConversationHandler, # Para gerenciar conversas multi-etapas
    filters # Para filtrar tipos específicos de mensagens
)

NOME = range(1)
TOKEN = os.getenv("TOKEN")

async def start(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
):
    await update.message.reply_text("Olá, mochileiro! 👋")
    await update.message.reply_text("Digite seu nome:")

    return NOME

async def curse(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
):
    await update.message.reply_text("Helloooww looser! 😜")


async def receber_nome(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
):
    context.user_data["nome"] = update.message.text
    await update.message.reply_text(f"Prazer em te conhecer, {context.user_data['nome']}! 😎")
    await update.message.reply_text("Obrigado por fornecer seu nome! Agora posso usá-lo nas próximas interações.")

    return ConversationHandler.END


async def receber_gastos(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
):
    await update.message.reply_text("Digite quanto você gastou agora: [nome]:[valor]")
    context.user_data["gastos"] = update.message.text
    nome_do_gasto, valor_do_gasto = update.message.text.split(":")
    # TODO: lembrar de validar dados
    # TODO: lembrar de sanitizar os valores
    if "gastos_detalhados" not in context.user_data:
        context.user_data["gastos_detalhados"] = []
    context.user_data["gastos_detalhados"].append((nome_do_gasto, valor_do_gasto))
    await update.message.reply_text(f"Detalhes dos gastos: {context.user_data['gastos_detalhados']}")

    return ConversationHandler.END


async def sobre(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
):
    await update.message.reply_text("Este é um bot criado por Mateus Bizzo. ⭐")


async def help(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
):
    await update.message.reply_text("Aqui estão os comandos disponíveis:" \
                                    "\n/start - Iniciar a conversa" \
                                    "\n/curse - Receber uma mensagem divertida" \
                                    "\n/sobre - Saber mais sobre o bot" \
                                    "\n/gastos - Registrar seus gastos" \
                                    "\n/help - Mostrar esta mensagem de ajuda")


def main():
    app = Application.builder().token(TOKEN).build()

    #app.add_handler(CommandHandler("start", start))
    #app.add_handler(CommandHandler("curse", curse))

    conversa = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            NOME: [MessageHandler(filters.TEXT & ~filters.COMMAND, receber_nome)]
        },
        fallbacks=[]
    )

    app.add_handler(conversa)
    app.add_handler(CommandHandler("help", help))
    app.add_handler(CommandHandler("sobre", sobre))
    app.add_handler(CommandHandler("gastos", receber_gastos))

    app.run_polling()


if __name__ == "__main__":
    main()
