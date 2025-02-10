from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import qrcode
import io

"""
um bot para o telegram que gera um qrcode, permitindo o usuário fazer vendas
"""



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("envie /pagar")

async def pagar(update: Update, context: ContextTypes.DEFAULT_TYPE):

    dados_pagamento = "CODIGO PIX"

    qr = qrcode.QRCode()
    qr.add_data(dados_pagamento)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
#envia imagem
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    await update.message.reply_photo(photo=buffer, caption="qrcode")

def main():
    #botfather

    TOKEN = "TOKEN BOTFATHER"


    application = Application.builder().token(TOKEN).build()

  #comandos
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("pagar", pagar))


    application.run_polling()

if __name__ == "__main__":
    main()

