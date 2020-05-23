messages = ['hi how r u', 'whassup', 'lol nm wgwu']
sent_messages = []


def send_messages(messages, sent_messages):
	"""shows sent messages and moves them"""
	while messages:
		for message in messages:
			moved_message = messages.pop()
			print(f"Sending your message of: {moved_message}")
			sent_messages.append(moved_message)

send_messages(messages[:], sent_messages)

print(messages)
print(sent_messages)