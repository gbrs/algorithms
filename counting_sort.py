from random import choice

text = ''
text_length = 1000
random_string = 'jhjkYhxKl kGxh3470->?/<Q'
alphabet = tuple(
                sorted(
                    list(
                        set(random_string)
                    )
                )
            )

for _ in range(text_length):
    text = ''.join((text, choice(alphabet)))
print(text)
