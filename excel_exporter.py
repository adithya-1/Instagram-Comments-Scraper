import pandas as pd
from pandas import ExcelWriter
import os.path


def export(names, comments, likes, replies):
    fname = 'comments.xlsx'
    temp = {}
    temp_names = []
    temp_comments = []
    temp_likes = []
    temp_replies = []

    if os.path.isfile(fname):
        saved = pd.read_excel(fname)
        temp_names.extend(saved['name'])
        temp_comments.extend(saved['comment'])
        temp_likes.extend(saved['likes'])
        temp_replies.extend(saved['replies'])

    temp_names.extend(names)
    temp_comments.extend(comments)
    temp_likes.extend(likes)
    temp_replies.extend(replies)

    temp.update(
        {'name': temp_names, 'comment': temp_comments, 'likes': temp_likes, 'replies': temp_replies})
    df = pd.DataFrame(temp)
    writer = ExcelWriter(fname)
    df.to_excel(writer, 'ridwan kamil', index=False)
    writer.save()
