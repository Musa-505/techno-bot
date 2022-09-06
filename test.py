import StringIO
import os
import sys
import zipfile
from multiprocessing import Pool, cpu_count

import requests

filePath = os.path.dirname(os.path.abspath(__file__))
print("filePath is %s " % filePath)
sys.path.append(filePath)
url = ["https://resources.cdn-kaspi.kz/medias/sys_master/images/images/hc2/h05/46392662458398/apple-iphone-13-128gb-cernyj-102298404-1-Container.jpg"]


def download_zips(url):
    file_name = url.split("/")[-1]
    response = requests.get(url)
    sourceZip = zipfile.ZipFile(StringIO.StringIO(response.content))
    print("\n Downloaded {} ".format(file_name))
    sourceZip.extractall(filePath)
    print("extracted {} \n".format(file_name))
    sourceZip.close()


if __name__ == "__main__":
    print("There are {} CPUs on this machine ".format(cpu_count()))
    pool = Pool(cpu_count())
    results = pool.map(download_zips, url)
    pool.close()
    pool.join()