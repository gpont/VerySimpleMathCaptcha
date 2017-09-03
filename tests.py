from verysimplemathcaptcha import VerySimpleMathCaptcha

outputStr = """
Welcome to tests for VerySimpleMathCaptcha

Test string: {}
Test id: {}
"""

def testCaptcha():
    captcha = VerySimpleMathCaptcha(using_settings=False)
    test = captcha.genTest()
    print(outputStr.format(
        test[1],
        test[0]
    ))
    for i in range(2):
        print("===============")
        answer = raw_input("Answer: ")
        print("Result: "+str(captcha.isValid(test[0], answer)))

if __name__ != "__init__":
    testCaptcha()

