def custom_resolver(route):
    if route == "profile":
        return "test"

    return route

# def clear_website_cache(path=None):
#     if path:
#         print("Clearing cache for:", path)
#     else:
#         print("Clearing cache for ALL website pages")