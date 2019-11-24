from utils import parse_version_from_stdin, version_string
from config import tagname_lang

version_got = parse_version_from_stdin()

lang_versions = []
for lang in tagname_lang:
    ver = version_got.get(lang, None)
    if ver is not None:
        lang_versions.append(lang + version_string(ver))

tagname = str.join("-", lang_versions)
print(tagname)
