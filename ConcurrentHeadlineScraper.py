'''
Author: Annija Balode

Algorithm: Concurrent Headline Scraper
'''

# Import necessary modules.
# Module for asynchronously executing callables.
import concurrent.futures
# Package for opening and reading URLs.
import urllib.request
import newspaper
from newspaper import Article

def get_articles(url):
        result = newspaper.build(url, memoize_articles=False)
        print('\n''The headlines from %s are' % url, '\n')
        articles = []
        # For each URL..
        for i in range(1,6):
            # Set art to the current article.
            art = result.articles[i]
            # Download the URL path.
            art.download()
            # Parse the current URL string into components.
            art.parse()
            # Print the title of the current article.
            print(art.title)
            # Append the current article to articles.
            articles.append(art.title)
        # Return articles.
        return articles
    
def get_headlines():
    # The list of URLs.
    URLs = ['http://www.foxnews.com/',
            'http://www.cnn.com/',
            'http://www.derspiegel.de/',
            'http://www.bbc.co.uk/',
            'https://theguardian.com',]

    # Use an executor with a pool of 5 threads to execute tasks asynchronously.
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        future_to_url = {executor.submit(get_articles, url): url for url in URLs}
        # Continue cycling while there are processes to complete.
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            
            # Go through each URL, try to open it.
            try:
                data = future.result()
            # Raise an exception.
            except Exception as exc:
                print('%r generated an exception: %s' % (url, exc))
            # Else, return the URL and the size of the data.
            else:
                print('%r page is %d bytes' % (url, len(data)))
                

if __name__ == '__main__':
    import timeit
    # Stores the time taken to run get_headlines().
    elapsed_time = timeit.timeit("get_headlines()", setup="from __main__ import get_headlines", number=2)/2
    # Outputs the total elapsed time.             
    print(elapsed_time) 
