# handlers.py

from telegram import Update, InputFile
from telegram.ext import ContextTypes
from tree_loader import load_tree
from keyboard import build_keyboard

decision_tree = load_tree()
nodes = decision_tree["nodes"]
start_node_id = decision_tree["start_id"]

IMAGE_URL = "https://i.imgur.com/Avla3YL.png"  # Картинка приветствия

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    node = nodes[start_node_id]
    text = node["text"]
    reply_markup = build_keyboard(node["options"])

    # Сначала отправляем изображение
    await update.message.reply_photo(photo=IMAGE_URL)

    # Затем — приветственный текст с кнопками
    await update.message.reply_text(text, reply_markup=reply_markup)

async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    node_id = query.data

    # Проверка: это файл для отправки?
    if node_id.startswith("send_doc:"):
        file_path = node_id.replace("send_doc:", "")
        try:
            await query.message.reply_document(InputFile(open(file_path, "rb")))
        except Exception as e:
            await query.message.reply_text(f"⚠️ Ошибка при отправке файла: {e}")
        return

    node = nodes.get(node_id)
    if not node:
        await query.edit_message_text("Ошибка: Узел не найден.")
        return

    text = node["text"]
    reply_markup = build_keyboard(node.get("options", []))

    # Старый способ — если в узле явно указан файл
    if "document" in node:
        document_path = f"./files/{node['document']}"
        try:
            await query.message.reply_document(InputFile(document_path))
        except FileNotFoundError:
            await query.message.reply_text(f"⚠️ Документ не найден: {node['document']}")

    await query.edit_message_text(text, reply_markup=reply_markup)