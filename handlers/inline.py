from pprint import pprint
from googlesearch import search
import hashlib
from aiogram import types ,Dispatcher


def finder(text):
    textt = search(text, num_results=7)
    for texty in textt:
        return texty

async def inline_google_search(query : types.inline_query):
    text = query.query or "echo"
    links = finder(text)
    articles = [types.InlineQueryResultArticle(
        id=hashlib.md5(text.encode()).hexdigest(),
        title="Google: ",
        url=links,
        input_message_content=types.InputMessageContent(
            message_text=links
        )
    )]
    await query.answer(articles, cache_time=60)

def register_handlers_inline(dp: Dispatcher):
    dp.register_inline_handler(inline_google_search)

"""

Версия через googlesearch

"""


#
# import hashlib
# from aiogram import types ,Dispatcher
#
# async def inline_google_search(query : types.inline_query):
#     text = query.query or "echo"
#     links = f"https://www.google.com/search?q={text}"
#     articles = [types.InlineQueryResultArticle(
#         id=hashlib.md5(text.encode()).hexdigest(),
#         title="Google: ",
#         url=links,
#         input_message_content=types.InputMessageContent(
#             message_text=links
#         )
#     )]
#     await query.answer(articles, cache_time=60)
#
# def register_handlers_inline(dp: Dispatcher):
#     dp.register_inline_handler(inline_google_search)
#
#


"""

Прошлая версия работала чутка криво из за кривой работы googlesearch

P.S. 
Обе версии работают исправно!

"""

