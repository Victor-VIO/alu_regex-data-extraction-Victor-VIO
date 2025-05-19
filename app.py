import re

class DataExtractor:
    @staticmethod
    def extract_emails(text):
        """Extracts email addresses from text."""
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        return re.findall(pattern, text)
    
    @staticmethod
    def extract_urls(text):
        """Extracts URLs from text."""
        pattern = r'https?://(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[^\s]*)?'
        return re.findall(pattern, text)
    
    @staticmethod
    def extract_phone_numbers(text):
        """Extracts phone numbers in various formats."""
        pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
        return re.findall(pattern, text)
    
    @staticmethod
    def extract_time(text):
        """Extracts time in 12-hour and 24-hour formats."""
        pattern = r'\b(1[0-2]|0?[1-9]):([0-5][0-9])(?:\s?[AP]M)?\b|\b(?:[01]?[0-9]|2[0-3]):[0-5][0-9]\b'
        matches = re.finditer(pattern, text)
        return [match.group() for match in matches]
    
    @staticmethod
    def extract_html_tags(text):
        """Extracts HTML tags from text."""
        pattern = r'<[^>]+>'
        return re.findall(pattern, text)
    
    @staticmethod
    def extract_hashtags(text):
        """Extracts hashtags from text."""
        pattern = r'#\w+'
        return re.findall(pattern, text)
    
    @staticmethod
    def extract_currencies(text):
        """Extracts currency amounts from text."""
        pattern = r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'
        return re.findall(pattern, text)

def main():
    test_text = """
    Contact us at support@example.com or sales@company.co.uk.
    Visit our website at https://www.example.com or https://sub.example.org/page.
    Call us at (123) 456-7890, 123-456-7890, or 123.456.7890.
    Store hours: 9:00 AM to 6:00 PM, or until 11:00.
    HTML content: <p>Hello</p> <div class="container">Content</div> <img src="banner.jpg" alt="Sale Banner">.
    Social media tags: #OpenAI #ArtificialIntelligence #ThisIsAHashtag.
    Prices: $19.99, $1,234.56, and $0.99.
    """
    
    extractor = DataExtractor()
    
    # Print all results in the exact format shown in the screenshot
    print("Time")
    print(extractor.extract_time(test_text))
    
    print("\nHTML Tags")
    print(extractor.extract_html_tags(test_text))
    
    print("\nHash Tags (#)")
    print(extractor.extract_hashtags(test_text))
    
    print("\nCurrencies($)")
    print(extractor.extract_currencies(test_text))
    
    print("\n" + "="*50 + "\n")
    
    print("Extracted Emails:", extractor.extract_emails(test_text))
    print("Extracted URLs:", extractor.extract_urls(test_text))
    print("Extracted Phone Numbers:", extractor.extract_phone_numbers(test_text))
    print("Extracted HTML Tags:", extractor.extract_html_tags(test_text))
    print("Extracted Hashtags:", extractor.extract_hashtags(test_text))

if __name__ == "__main__":
    main()