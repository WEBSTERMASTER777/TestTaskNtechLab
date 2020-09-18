# def load_config(config_file):
#     with open(config_file) as f:
#         return load(f, Loader=FullLoader)


# def get_classname_file(classes_name):
#     f = open('classes2.txt', 'w')
#     s1 = '\n'.join(classes_name)
#     f.write(s1)
#     f.close()


# def write_json_file(filename, data, indent=2):
#     with open(filename, "w") as write_file:
#         dump(data, write_file, indent=indent)
# import re
# res = re.search('*jpg', 'jpg')
# print(res)
import re 
if re.search("jpg", "male.jpg"): print ("hi")
        # for img in os.listdir(sys.argv[1]):
        #     print(type(img))
        #     if bool(re.search('*jpg',img )):
        #         print(res)