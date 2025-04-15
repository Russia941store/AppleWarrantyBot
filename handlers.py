#handlers.py
from telegram import Update
from telegram.ext import ContextTypes
from tree_loader import load_tree
from keyboard import build_keyboard

decision_tree = load_tree()
nodes = decision_tree["nodes"]
start_node_id = decision_tree["start_id"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    node = nodes[start_node_id]
    text = node["text"]
    reply_markup = build_keyboard(node["options"])
    await update.message.reply_text(text, reply_markup=reply_markup)

async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    node_id = query.data
    node = nodes.get(node_id)

    if not node:
        await query.edit_message_text("Ошибка: Узел не найден.")
        return

    text = node["text"]
    reply_markup = build_keyboard(node.get("options", []))
    await query.edit_message_text(text, reply_markup=reply_markup)