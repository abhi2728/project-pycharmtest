from Question import question

question_prompt = [
    'What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n',
    'What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n',
    'What color are Strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n'
]

questions = [
    question(question_prompt[0], 'a'),
    question(question_prompt[1], 'c'),
    question(question_prompt[2], 'b'),
    question('Who is indian cricket team caption?\n(a) Dhoni\n(b) Gavskar\n(c) Kohli\n(d) Sharma\n\n', 'd')
]


def test_run(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print('Result : ', score, '/', str(len(questions)))


test_run(questions)
