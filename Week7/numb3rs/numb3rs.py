import re



def main():
    try:
     ip = input("IPv4 Address: ").strip()
    except: ValueError
    print(validate(ip))


def validate(ip):
     pattern = re.compile(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", re.IGNORECASE)
     match = pattern.match(ip)
     if match:
          for i in match.groups():
               if  not (0 <= int(i) <= 255):
                    return False

          return True

     return False



if __name__ == "__main__":
    main()
