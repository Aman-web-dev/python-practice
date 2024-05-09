from bs4 import BeautifulSoup;
import requests
import re


# scraped_data= requests.get()


def remove_extra_spaces(paragraph):
    # Use a regular expression to replace one or more spaces with a single space
    clean_paragraph = re.sub(r'\s+', ' ', paragraph)
    return clean_paragraph


def scrapWithUrl(url):
    scraped_data= requests.get(url);

    if scraped_data.status_code==200:
        soup = BeautifulSoup(scraped_data.text,"html.parser")

        blog_text=  soup.findAll("div",attrs={"class":"entry-content wp-block-post-content is-layout-flow wp-block-post-content-is-layout-flow"})
        blog_data=''


        for index, paragraphs in enumerate(blog_text) :
          blog_data=remove_extra_spaces(blog_data+paragraphs.text)
   


        authorname_div=soup.findAll("div",attrs={"class":"wp-block-tc23-author-card-name"})
        author_link = authorname_div[0].find('a')
        author_name=author_link.text



        blog_image_src=soup.findAll("img",attrs={"class":"attachment-post-thumbnail size-post-thumbnail wp-post-image","alt":"Walmart/Sam's Club AI exit tech"})[0]["src"]

        return {"blogData":blog_data, "AuthorName":author_name, "thumbnail Source":blog_image_src} 
 

    else:
        print("There was an Error while requesting The data the error might be in the code")

       

print(scrapWithUrl("https://techcrunch.com/2024/04/30/sams-clubs-ai-powered-exit-tech-reaches-20-of-stores/"))
 

   