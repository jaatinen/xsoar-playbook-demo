import requests

def check_url_reputation(url):
    # Mock URL reputation check - in real case integrate with VirusTotal or similar
    malicious_urls = ["http://phishing-site.com", "http://malware-domain.org"]
    
    if url in malicious_urls:
        return {
            "url": url,
            "reputation": "malicious",
            "confidence": 95
        }
    else:
        return {
            "url": url,
            "reputation": "clean",
            "confidence": 90
        }

if __name__ == "__main__":
    test_url = "http://phishing-site.com"
    result = check_url_reputation(test_url)
    print(f"URL: {result['url']}, Reputation: {result['reputation']}, Confidence: {result['confidence']}%")
