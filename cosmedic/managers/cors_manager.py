from subprocess import Popen, PIPE, STDOUT
import sys

"""
Assign different binaries based on environment.
In production mode, django is ran with different commands that does not have more than 1 argument in sys.
Hence, we can guarantee that only in development mode we will run with 'runserver'.
"""
binary = "./lib/get-cors"
try:
    if sys.argv[1] == 'runserver':
        binary = "./lib/get-cors-macos"
except:
    print("This is production mode")
print("Binary used for get-cors is", binary)

"""
Do a search on cosdna, return the result page content.
"""
def get_search_content(keyword):
    sort_key = "date"
    cmd = binary + " https://www.cosdna.com/eng/product.php\?q\=" + keyword + "\&sort\=" + sort_key

    return run_cors_proxy(cmd)

""""
Visit and return the item page content.
"""
def get_item_content(url):
    cmd = binary + " https://www.cosdna.com" + url
    return run_cors_proxy(cmd)

"""
Use a local built executable file to get the page content
"""
def run_cors_proxy(cmd):
    # TODO: when error happens on binary, we need to output log and return a different value
    p = Popen(cmd, shell=True, stdout=PIPE, stderr=STDOUT)
    return p.stdout.read()
