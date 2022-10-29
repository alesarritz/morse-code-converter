art = """
 _, _ _,__, _,__,   _, _,__,__,   _, _,_, __,___,__,_____,__,
 |\/|/ \|_)(_ |_   / `/ \| \|_   / `/ \|\ || /|_ |_) | |_ |_)
 |  |\ /| \, )|    \ ,\ /|_/|    \ ,\ /| \||/ |  | \ | |  | \\
 ~  ~ ~ ~ ~ ~ ~~~   ~  ~ ~  ~~~   ~  ~ ~  ~~  ~~~~ ~ ~ ~~~~ ~                                                                                              
"""
morse = {" ": " ", "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".",
         "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-",
         "l": ".-..", "m": "--", "n": "-.", "o": "---.", "p": ".--.", "q": "--.-",
         "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--",
         "x": "-..-", "y": "-.--", "z": "--..",
         "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....",
         "6": "-....", "7": "--...", "8": "---..", "9": "----.", "0": "-----"}


def convert(text):
    morse_code = ""
    for c in text:
        if c not in morse:
            return f"Symbol ({c}) not allowed. Try again!"
        morse_code += morse[c]
    return morse_code


if __name__ == '__main__':
    print(art)
    keep_going = 'y'
    while keep_going == 'y':
        to_morse = input("Input text: ").lower()
        print("Result:", convert(to_morse))
        keep_going = input("\nTry again (y/n): ").lower()
    print("Goodbye!")
