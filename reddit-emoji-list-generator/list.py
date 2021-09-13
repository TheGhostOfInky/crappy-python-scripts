import praw, sys
subname = sys.argv[1]
fname = subname + "_emoji_list.txt"
emojilist = open (fname,"a",encoding="utf-8")

reddit = praw.Reddit(
    client_id="",
    client_secret="",
    password="",
    user_agent="Praw script by u/TheGhostOfInky",
    username="",
)

for emoji in reddit.subreddit(subname).emoji:
    print(emoji)
    emojilist.write(str(emoji))
    emojilist.write("\n")
emojilist.close