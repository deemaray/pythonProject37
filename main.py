# Lesson 15: Case's Homework

def errorcode(x):
    match x:
        case 400:
            return ("Bad request")
        case 401:
            return ("unauthorized")
        case 402:
            return ("Payment required")
        case 403:
            return ("Forbidden")
        case 404:
            return ("Not found")

print(errorcode(404))
quit()
