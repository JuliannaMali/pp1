facebook = str(input("Facebook (True or False): "))
twitter = str(input("Twitter: "))
instagram = str(input("Instagram: "))

list = []
if facebook == "True" or facebook == "true":
    list.append(facebook)
if twitter == "True" or twitter == "true":
    list.append(twitter)
if instagram == "True" or instagram == "true":
    list.append(instagram)
if len(list) == 2:
    print("A person can be a good influencer")