#with open("new.txt","r") as f:
 #   x=f.readlines()
  #  x = new.txt. split("")
   # for line in x:
    #    print(line)
with open("new.txt") as f:
    content = f.readlines()
    print (content)

    with open("output.txt", "w+") as nf:
        for lines in content[0].split():
            for word in lines.split(','):
                print(word)
                nf.write("IP\t datetime\t Request type \t browser type \t search engin \t url\t")
                nf.write("{}\t {}\t {}\t {}\t {}\t {}\t".format (str(lines[0])(lines[2])(lines[3])(lines[4])(lines[5])(lines[6])))