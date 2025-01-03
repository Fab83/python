def show_messages(messages):
    for message in messages:
        print(message)


def move_messages(list_1, list_2):
    while list_1:
        popped = list_1.pop()
        list_2.append(popped)


my_messages = ['un message', 'un autre', 'une idée', 'une suite']
sent_messages = []

show_messages(my_messages)
move_messages(my_messages[:], sent_messages)

print(my_messages)
print(sent_messages)
