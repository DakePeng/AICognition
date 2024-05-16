from arxiv2text import arxiv_to_text
import re

def getArchiveLinks(filePath):
    # Open the text file
    with open(filePath, 'r') as file:
        # Initialize an empty list to store the second elements
        research_links = []
        
        # Read each line in the file
        for line in file:
            # Split the line by whitespace
            links = line.strip().split()
            
            # Check if the second element exists and is not "None"
            if len(links) > 1 and links[1] != "None":
                # Add the second element to the list
                research_links.append(links[1])

    # Print the list of second elements
    return research_links

def archiveLinkAbsToPdf(url):
    # Define the regex pattern to match the URL
    pattern = r".+arxiv.org/abs/(\d+\.\d+)"
    # Check if the pattern matches the URL
    match = re.match(pattern, url)
    # If there's a match, perform the substitution
    if match:
        # Perform the substitution by replacing 'abs' with 'pdf'
        new_url = "https://arxiv.org/pdf/" + match.group(1)
        return new_url
    return url
        
if __name__ == "__main__":
    # list = getArchiveLinks("./Links/OpenAI_Research.txt")
    newlist = [
        "http://arxiv.org/abs/2110.14168",
        "http://arxiv.org/abs/1908.08016",
        "http://arxiv.org/abs/1907.04534",
        "http://arxiv.org/abs/1903.08689",
        "http://arxiv.org/abs/1903.00784",
        "https://distill.pub/2021/multimodal-neurons/",
        "https://openaipublic.blob.core.windows.net/neuron-explainer/paper/index.html",
        "https://distill.pub/2019/safety-needs-social-scientists"
    ]
    
    for link in newlist:
        url = archiveLinkAbsToPdf(link)
        try:
            arxiv_to_text(url, "./Articles/OpenAI") 
        except:
            print("Error on: " + url)