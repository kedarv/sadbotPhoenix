import random

magic_eight_ball_options = [
    "It is certain",
    "It is decidedly so",
    "Without a doubt",
    "Yes definitely",
    "You may rely on it",
    "You can count on it",
    "As I see it, yes",
    "Most likely",
    "Outlook good",
    "Yes",
    "Signs point to yes",
    "Absolutely",
    "Reply hazy try again",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Concentrate and ask again",
    "Don't count on it",
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful",
    "Chances aren't good",
]


def magic8_command(update, context):
    """Send a message when the command /8ball is issued."""
    user_id = update.message.from_user.id
    user_name =update.message.from_user.first_name
    mention = "[" + user_name + "](tg://user?id=" + str(user_id) + ")"

    update.message.reply_markdown(
        mention + ": " + random.choice(magic_eight_ball_options), quote=False
    )
