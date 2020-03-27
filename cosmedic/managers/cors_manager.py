from subprocess import Popen, PIPE, STDOUT

"""
Do a search on cosdna, return the result page content.
"""
def get_search_content(keyword):
    sort_key = "date"
    cmd = "./lib/get-cors https://www.cosdna.com/eng/product.php\?q\=" + keyword + "\&sort\=" + sort_key

    return run_cors_proxy(cmd)

""""
Visit and return the item page content.
"""
def get_item_content(url):
    cmd = "./lib/get-cors https://www.cosdna.com" + url
    return run_cors_proxy(cmd)

"""
Use a local built executable file to get the page content
"""
def run_cors_proxy(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE, stderr=STDOUT)
    return p.stdout.read()
