import random

inp = input()
splitSen = inp.split()
numWord = len(splitSen)
newSen = ""
emojiWord = {
    "happy": ["😆", "😄", "😁", "😊", "😸"],
    "sad": ["😢", "😞", "🙁", "😕", "😔", "😿"],
    "cry": ["😢", "😭", "🥲", "😿"],
    "laugh": ["😆", "🤣", "😹"],
    "laughing": ["😆", "🤣", "😹"],
    "dead": ["🪦", "💀", "😵"],
    "crying": ["😭"],
    "lmao": ["😭", "😹", "🤣"],
    "lol": ["😭", "😹", "😆"],
    "rofl": ["🤣"],
    "blow": ["🌬️", "😗", "😙", "🐡"],
    "dog": ["🐶", "🐕", "🦮", "🐩", "🐕‍🦺"],
    "cat": ["🐱", "🐈", "🐈‍⬛", "😺", "😸"],
    "girl": ["👧"],
    "boy": ["👦"],
    "um": ["🫥", "😶", "🫤", "🦫"],
    "umm": ["😶", "🫤", "🦫"],
    "ummm": ["🫤", "🦫"],
    "ummmm": ["🦫"],
    "erm": ["🤓"],
    "acktually": ["☝️"],
    "think": ["🤔", "💭", "🧐"],
    "thinking": ["🤔", "💭", "🧐"],
    "thought": ["🤔", "💭"],
    "give": ["👐"],
    "gift": ["🎁"],
    "okay": ["👌"],
    "yes": ["👍", "🙌", "🙂‍↕️", "✅", "🙆"],
    "no": ["❌", "👎", "🚫", "🙅", "❎"],
    "idk": ["🤔", "🤷"],
    "say": ["🗣️"],
    "preach": ["🗣️"],
    "talk": ["🗣️"],
    "said": ["🗣️"],
    "talking": ["🗣️"],
    "love": ["🩷", "😍", "🥰", "😘", "💕", "💞", "💓", "💗", "💖", "💘", "💝", "💟"],
    "good": ["👍"],
    "bad": ["👎"],
    "boo": ["👎"],
    "james": ["👴"],
    "angry": ["😠", "😡", "😾", "🤬"],
    "mad": ["😠", "😡", "😾"],
    "eat": ["🍽️"],
    "munch": ["🦫"],
    "yay": ["🥳", "😆", "🎊", "🎉", "👏", "🙌"],
    "olivia": ["😇"],
    "hurt": ["🤕"],
    "sick": ["🤒", "🤧", "🤢", "🤮"],
    "sleep": ["😴", "😪"],
    "snooze": ["😴", "😪"],
    "zzz": ["😴", "💤"],
    "yawn": ["🥱"],
    "shower": ["🚿"],
    "showering": ["😶‍🌫️"],
    "bath": ["🛁"],
    "anxious": ["😣"],
    "nervous": ["😣", "😥", "😰", "😬"],
    "mwah": ["😘", "💋", "😚", "😽", "👩‍❤️‍💋‍👩"],
    "kiss": ["😗", "💋", "😚", "😽", "😙", "👩‍❤️‍💋‍👩", "💏", "👩‍❤️‍💋‍👨", "👨‍❤️‍💋‍👨"],
    "fire": ["🔥"],
    "omg": ["😱", "🤯", "😨", "🙊", "🙀", "😧"],
    "smirk": ["😏", "😼"],
    "ugh": ["😒", "🙄", "😑"],
    "ughh": ["😕", "😒", "🙄", "😑"],
    "ughhh": ["😞", "😕", "😒", "🙄", "😑"],
    "hate": ["🤬"],
    "alien": ["👽"],
    "hug": ["🫂"],
    "pray": ["🙏"],
    "wow": ["😯", "😧"],
    "woww": ["😲", "🙊"],
    "wowww": ["🤯", "😱", "🤯", "🙀"],
    "agree": ["🙂‍↕️", "👍"],
    "agreed": ["🙂‍↕️"],
    "iktr": ["🙂‍↕️"],
    "hear": ["👂"],
    "listen": ["👂"],
    "heard": ["👂"],
    "see": ["👁️"],
    "saw": ["👀"],
    "on": ["🔛"],
    "loop": ["🔁"],
    "time": ["⏰", "⏱️", "🕰️", "🕑", "🕓", "🕥", "🕝", "🕗"],
    "email": ["📧", "📩", "📨"],
    "bang": ["💥"],
    "earth": ["🌎", "🌍", "🌏"],
    "snowman": ["⛄️"],
    "plant": ["🌱", "🌿", "🪴"],
    "mouse": ["🐭", "🐁"],
    "bear": ["🐻"],
    "panda": ["🐼"],
    "moon": ["🌚", "🌝", "🌜", "🌛", "🌙", "🌕"],
    "sun": ["🌞"],
    "star": ["💫", "🌟", "⭐️", "🤩"],
    "planet": ["🪐"],
    "sunrise": ["🌅", "🌄", "🌇", "🌆"],
    "sunset": ["🌅", "🌄", "🌇", "🌆"],
    "rain": ["🌧️"],
    "raining": ["🌧️"],
    "pig": ["🐷", "🐽", "🐖"],
    "bird": ["🐥", "🦜", "🦆", "🪿", "🐓", "🦢", "🕊️", "🐦‍⬛", "🦉", "🦤", "🦅", "🐦", "🐤", "🐧"],
    "huh": ["🤨"],
    "punch": ["👊", "🥊", "🤜", "🤛"],
    "fight": ["👊", "🥊", "🤜", "🤛", "🤺"],
    "evil": ["😈", "👿"],
    "dance": ["💃", "🕺", "👯", "👯‍♀️", "👯‍♂️"],
    "camera": ["📷", "📸"],
    "video": ["🎥", "📽️"],
    "picture": ["📸", "🤳"],
    "mountain": ["⛰️", "🏔️", "🗻"],
    "america": ["🇺🇸", "🦅"],
    "usa": ["🇺🇸", "🦅"],
    "fruit": ["🍏", "🍎", "🍐", "🍊", "🍋", "🍒", "🍓", "🍉", "🍑", "🥝", "🥭", "🫐", "🍈", "🍍", "🍌"],
    "drive": ["🚘", "🚗", "🚙"],
    "car": ["🚘", "🚗", "🚙"],
    "train": ["🚃", "🚋", "🚞", "🚝", "🚄", "🚅", "🚈", "🚂", "🚆", "🚇", "🚊", "🚉"],
}

splitSen = inp.split()
numWord = len(splitSen)
newSen = ""
for i in range(numWord):
    if splitSen[i].lower() in emojiWord:
        if len(emojiWord[splitSen[i]]) > 1:
            rand = random.randint(0, (len(emojiWord[splitSen[i]]) - 1))
            emojiList = emojiWord[splitSen[i]]
            randEmoji = emojiList[rand]
            newSen = newSen + " " + randEmoji
        else:
            emoList = emojiWord[splitSen[i]]
            newSen = newSen + " " + emoList[0]
    else:
        newSen = newSen + " " + splitSen[i]
        
print(newSen)