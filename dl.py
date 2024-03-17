import requests
import argparse
import logging
import urllib.parse
import time

first_point = time.time()

logging.basicConfig(format="%(asctime)s - %(level)s - %(message)s", level=logging.WARNING)

argparser = argparse.ArgumentParser(description="File downloader")

argparser.add_argument("url", help="The url address to get.")
argparser.add_argument("-dst", help="Save the file to the destnation path"
                       ", default to the current working folder", default="")

args = argparser.parse_args()


url = args.url

default_filename = urllib.parse.urlparse(url).path.split("/")[-1]

second_point = time.time()

res = requests.get(url)

third_point = time.time()

print("Request complete, content length %d." % len(res.content))
print("Writing......")
total_writed = 0
if args.dst:
    with open(args.dst, "wb") as file:
        for chunk in res.iter_content(1000000):
            file.write(chunk)
            total_writed += 1000000
            print(total_writed, "writed.")
            
else:
    with open(default_filename, "wb") as file:
        for chunk in res.iter_content(1000000):
            file.write(chunk)
            total_writed += 1000000
            print(total_writed, "writed.")
            
final_point = time.time()

print(f"Completed. (Total time: {final_point - first_point}s,"
      f" Initialize time: {second_point - first_point}s,"
      f" Server response time: {third_point - second_point}s,"
      f" File writing time: {final_point - third_point}s)")
