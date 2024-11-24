import requests as req

def get_api(url):
    try:
        response = req.get(url)
        response.raise_for_status() 
        return response.json()
        
    except req.exceptions.RequestException as e:
        print("Error: ", e)

def main():
    url = "https://jsonplaceholder.typicode.com/todos"
    
    res = get_api(url)
    res_list = list(res)
    
    search_str = 'qui'

    titles = [x['title'] for x in res_list if search_str in x['title']]
    
    for title in titles:
        str_title = str(title)
        
        if isinstance(str_title, str):
            print(f"Title: {str_title}")
        else: 
            print("Title is not a string")
            
    print("\nchecking if a title is a string===")
    
    random_title = titles[5]
    print("Title is int: ", isinstance(random_title, int))
    print("Title is string: ", isinstance(random_title, str))
    
if __name__ == '__main__':
    main()