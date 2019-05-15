from dataio import getchatid, getmsgid, getfileid, getmsg, sendmsg, sendsticker, sendfile, sendphoto, sendvideo
from mdprivcmd import mdprivcmd


def privtext(data):
    msg = getmsg(data)
    if msg.startswith('/'):
        resp = mdprivcmd(data)
        return resp
    else:
        chatid = getchatid(data)
        resp = sendmsg(chatid, msg)
        return resp


def privsticker(data):
    chatid = getchatid(data)
    sticker = getfileid(data)
    resp = sendsticker(chatid, sticker)
    return resp


def privphoto(data):
    chatid = getchatid(data)
    photo = getfileid(data)
    resp = sendphoto(chatid, photo)
    return resp


def privvideo(data):
    chatid = getchatid(data)
    video = getfileid(data)
    resp = sendvideo(chatid, video)
    return resp


def privfile(data):
    chatid = getchatid(data)
    file = getfileid(data)
    resp = sendfile(chatid, file)
    return resp