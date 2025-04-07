#Write a programm to ask the user on which browser to run automation

browser_name=input("Enter the browser name- \n")
browser_name = browser_name.lower()
match browser_name:
    case ("firefox"):
        if browser_name == "firefox":
            print("Hello")
        print("Execute firefox code")
    case ("chrome"):
        print("Execute chrome code")
    case ("mozilla"):
        print("Execute Mozilla code")

