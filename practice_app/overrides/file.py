def before_write(**kwargs):
    print("FILE IS ABOUT TO BE WRITTEN")

# def write_file(*args, **kwargs):
#     print("My custom write_file() is running")

def delete_file(*args, **kwargs):
    print("CUSTOM DELETE FILE")
    print("ARGS:", args)
    print("KWARGS:", kwargs)