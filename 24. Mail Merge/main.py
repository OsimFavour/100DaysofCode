with open("../mail merge/Input/Names/invited_names.txt", "r") as names_file:
	with open("../mail merge/Input/Letters/starting_letter.txt", "r") as body_file:
		body = body_file.read()
		for name in names_file:
			renamed = name.strip()
			mail = body.replace("[name]", renamed)
			with open(f"../mail merge/Output/ReadyToSend/letter_for_{renamed}.docx", "w") as mail_file:
				mail_file.write(mail)
