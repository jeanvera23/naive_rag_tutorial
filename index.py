from retrieval_system import retrieving_from_db
from retrieval_system import generating_response, generating_response_localhost
import argparse

def main():
    
    # Create CLI.
    parser = argparse.ArgumentParser()
    parser.add_argument("query_text", type=str, help="The query text.")
    args = parser.parse_args()
    
    query_text = args.query_text
    
    results = retrieving_from_db(query_text)
    
    if(results is None):
        return
    
    formatted_response = generating_response(query_text, results)
    print(formatted_response)
    
    
if __name__ == "__main__":
    main()