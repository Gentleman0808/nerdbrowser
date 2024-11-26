import webbrowser

def search_website(base_url):
    """
    Permet de rechercher un terme sur un site web spécifique.
    
    :param base_url: L'URL de base du site (par exemple, https://votresite.com).
    """
    print("=== Access NerdBrowser ===")
    query = input("You are a white hat:grey hat:black hat ? : ").strip()
    
    if not query:
        print("No answer enter. please try again.")
        return

    search_url = f"{base_url}/search?q={query.replace(' ', '+')}"
    print(f"Access in progress : {search_url}")

    webbrowser.open(search_url)
    print("Search has been launched in your browser.")

def main():
    """
    Fonction principale pour lancer le script.
    """
    
    base_url = "https://www.nerdbrowser.fr/blog-informatique/b0l/Tous"

    print("=== NerdBrowser ===")
    print(f"Website : {base_url}")
    
    while True:
        print("\nOptions :")
        print("1. Access Nerd")
        print("2. Echap")
        
        choice = input("Enter your choice : ").strip()
        
        if choice == "1":
            search_website(base_url)
        elif choice == "2":
            print("See you soon nerd 😎")
            break
        else:
            print("Invalid choice. please try again.")

if __name__ == "__main__":
    main()
