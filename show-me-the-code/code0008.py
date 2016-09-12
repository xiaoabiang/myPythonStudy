import requests

def main():
    result = requests.get('http://www.lagou.com/zhaopin/Python/')
    print(result.text)


if __name__ == "__main__":
    main()
