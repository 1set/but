from utils import parse_version_from_stdin, version_string

version_got = parse_version_from_stdin()
versions = sorted(version_got.items(), key=lambda x:(x[0], x[1]))

lang_versions = []
for lang, ver in versions:
    lang_versions.append("{}-{}".format(lang, version_string(ver)))

tagname = str.join("_", lang_versions)
print(tagname)
