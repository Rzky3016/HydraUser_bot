""" Userbot module for other small commands. """
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.lhelp$")
async def usit(e):
    await e.edit(
        f"**Hai Raja {DEFAULTUSER} Kalau Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.help` Atau Bisa Minta Bantuan Ke:\n"
        "\n[Owner](t.me/PashaDIE)"
        "\n[Repo](https://github.com/PashaDIE/HydraUser_bot)"
        "\n[Instagram Owner](Instagram.com/Pdie.09)")


@register(outgoing=True, pattern="^.vars$")
async def var(m):
    await m.edit(
        f"**Disini Daftar Vars Dari {DEFAULTUSER}:**\n"
        "\n[DAFTAR VARS](https://raw.githubusercontent.com/PashaDIE/HydraUser_bot/HydraUser_bot/varshelper.txt)")


CMD_HELP.update({
    "hydrahelper":
    "�🐍CMD�🐍`.hhelp`\
\nPenjelasan: Bantuan Untuk saya-Userbot.\
\n�🐍CMD�🐍`.vars`\
\nPenjelasan: Untuk Melihat Beberapa Daftar Vars."
})
