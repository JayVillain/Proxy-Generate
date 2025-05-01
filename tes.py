import requests

def check_proxy(proxy):
    p = {"http": proxy, "https": proxy}
    try:
        r = requests.get("http://example.com", proxies=p, timeout=5)
        return r.status_code
    except Exception:
        return None

if __name__ == "__main__":
    # Baca daftar proxy dari file, satu proxy per baris seperti:
    # http://192.168.1.42:10000
    # http://192.168.1.42:10001
    with open('proxies.txt', 'r') as f:
        proxies = [line.strip() for line in f if line.strip()]

    for proxy in proxies:
        status = check_proxy(proxy)
        if status:
            print(f"{proxy} → OK (status {status})")
        else:
            print(f"{proxy} → FAILED")
