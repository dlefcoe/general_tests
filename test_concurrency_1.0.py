'''

Why the Synchronous Version Rocks:
    The great thing about this version of code is that, well, it’s easy.
    It was comparatively easy to write and debug.
    It’s also more straight-forward to think about.
    There’s only one train of thought running through it, so you can predict what the next step is and how it will behave.


The Problems With the Synchronous Version
    The big problem here is that it’s relatively slow compared to the other solutions we’ll provide.
    It waits at each step >>> blocking.


https://realpython.com/python-concurrency/
'''


def main():
    ''' main entry point of the code '''
    threading_version()
    return


# Synchronous Version
def synchronous_version():
    import requests
    import time


    def download_site(url, session):
        with session.get(url) as response:
            print(f"Read {len(response.content)} from {url}")


    def download_all_sites(sites):
        with requests.Session() as session:
            for url in sites:
                download_site(url, session)


    if __name__ == "__main__":
        sites = [
            "https://www.jython.org",
            "http://olympus.realpython.org/dice",
        ] * 80
        start_time = time.time()
        download_all_sites(sites)
        duration = time.time() - start_time
        print(f"Downloaded {len(sites)} in {duration} seconds")




#threading Version
def threading_version():
    import concurrent.futures
    import requests
    import threading
    import time


    thread_local = threading.local()


    def get_session():
        if not hasattr(thread_local, "session"):
            thread_local.session = requests.Session()
        return thread_local.session


    def download_site(url):
        session = get_session()
        with session.get(url) as response:
            print(f"Read {len(response.content)} from {url}")


    def download_all_sites(sites):
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            executor.map(download_site, sites)


    if __name__ == "__main__":
        sites = [
            "https://www.jython.org",
            "http://olympus.realpython.org/dice",
        ] * 80
        start_time = time.time()
        download_all_sites(sites)
        duration = time.time() - start_time
        print(f"Downloaded {len(sites)} in {duration} seconds")



# hoisting
if __name__=='__main__':
    ''' This is executed when run from the command line '''
    main()