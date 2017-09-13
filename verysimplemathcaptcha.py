import string
from random import random, choice

class VerySimpleMathCaptcha:
    def __init__(self, using_settings=True, using_pil=True):
        if using_settings:
            import settings
            self.using_pil = settings.VERYSIMPLEMATHCAPTCHA_USING_PIL
        else:
            self.using_pil = using_pil

        if self.using_pil:
            from PIL import ImageFont, Image, ImageDraw
            self.font = ImageFont.truetype("/usr/share/fonts/dejavu/DejaVuSans.ttf", 25)


    def isValid(self, test, answer):
        # for correct base64 decoding
        test += '==\n'
        test_arr = test.decode('base64').split(';')
        test_case = [int(test_arr[0]), test_arr[1], int(test_arr[2])]
        if test_case[1] == '+':
            return test_case[0]+test_case[2] == int(answer)
        elif test_case[1] == '-':
            return test_case[0]-test_case[2] == int(answer)
        elif test_case[1] == '*':
            return test_case[0]*test_case[2] == int(answer)
        elif test_case[1] == '/':
            return test_case[0]/test_case[2] == int(answer)

    def genImageTest(self, text):
        img = Image.new("RGBA", (200,200), (255,255,255))
        draw = ImageDraw.Draw(img)
        draw.text((5, 5), text, (0,0,0), font=self.font)
        return img.getdata()

    # return (test, test_str)
    def genTest(self):
        first_num = str(int(random()*10))
        second_num = str(int(random()*10))
        operation = choice(['+','-','*','/'])
        test_text = first_num+' '+operation+' '+second_num
        if self.using_pil:
            test_text = genImageTest(test_text)
        return (
                (first_num+';'+operation+';'+second_num).encode('base64')[:-2],
                test_text
        )

