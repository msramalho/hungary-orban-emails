day = input("what is the date in yyyy-mm-dd format?")
full_date = input("what is the datetime in 'DoW date time'?")
source = input("what is the source (gov, orban, ...)?")

def do_for_lang(lang):
    title = input("what is the title of the email in %s?" % lang)
    body = input("what is the body of the email in %s?" % lang)

    with open("%s/template.md" % lang, "r", encoding="utf-8") as template:
        doc = template.read().strip()

    doc = doc.replace("[[DAY]]", day)
    doc = doc.replace("[[FULL_DATE]]", full_date)
    doc = doc.replace("[[TITLE]]", title)
    doc = doc.replace("[[BODY]]", body)

    with open("%s/%s.md" % (lang, day), "w", encoding="utf-8") as outf:
        outf.write(doc)

    return title


title_hu = do_for_lang("hu")
title_en = do_for_lang("en")

print(
f"""
* `[{day}]` from **{source}**: 
  * en - [{title_en}](en/{day}.md)
  * hu - [{title_hu}](hu/{day}.md)
  """
)