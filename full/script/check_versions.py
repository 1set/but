from utils import parse_version_from_stdin, version_string
from config import minimum_version_required


actual_version_got = parse_version_from_stdin()

for lang, min_ver in minimum_version_required.items():
    if lang not in actual_version_got:
        print("{} is missing, required version: {}".format(lang, version_string(min_ver)))
        exit(1)
    else:
        act_ver = actual_version_got[lang]
        if act_ver < min_ver:
            print('{} version {} is lower than the required version {}'.format(lang, version_string(act_ver), version_string(min_ver)))
            exit(2)
        else:
            print("{} version {} - ok".format(lang, version_string(act_ver)))

exit(0)
