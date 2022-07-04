#!/usr/bin/python

#   dnf -y install python38
#   alternatives --set python /usr/bin/python3.8

import os, hashlib, time, json
path = "/dev/null"

def find_files_recursively(files_dict = {} ):
  for root,d_names,f_names in os.walk(path,followlinks=False):
    for f in f_names:
        #print (os.path.join(root, f) + ' ' + compute_file_checksum(os.path.join(root, f)))
        files_dict.update({os.path.join(root, f): compute_file_checksum(os.path.join(root, f))})
        #print (compute_file_checksum(os.path.join(root, f)))
  return files_dict 


def compute_file_checksum(path, read_chunksize=32768, algorithm='md5'):
    """Compute checksum of a file's contents.

    :param path: Path to the file
    :param read_chunksize: Maximum number of bytes to be read from the file
     at once. Default is 65536 bytes or 64KB
    :param algorithm: The hash algorithm name to use. For example, 'md5',
     'sha256', 'sha512' and so on. Default is 'sha256'. Refer to
     hashlib.algorithms_available for available algorithms
    :return: Hex digest string of the checksum

    .. versionadded:: 1.0.0
    """
    checksum = hashlib.new(algorithm)  # Raises appropriate exceptions.
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(read_chunksize), b''):
            checksum.update(chunk)
            # Release greenthread, if greenthreads are not used it is a noop.
            time.sleep(0)
    return checksum.hexdigest()


def main():
    #print (find_files_recursively())
    #print (json.dumps(find_files_recursively()))
    f = open('/var/tmp/directory_files_checksum', 'w', encoding="utf-8")
    f.write(json.dumps(find_files_recursively()))
    f.closed

if __name__ == '__main__':
    main()
