import subprocess
from pprint import pprint
import re

def ipconf_cmd():
    text = subprocess.check_output('ipconfig')
    decoded = text.decode('cp866')
    # Path('~/output.txt').expanduser().write_text(decoded)
    decoded_2 = re.sub("\\r\\n", "", decoded)
    pprint(decoded_2)

ipconf_cmd()