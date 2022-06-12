import os
from random import randint, sample, choice
from shutil import copy

## helper script to copy a ton of random files to use for the activity


path = "C:\\Users\\chall\\my drive\\Python\\security_activity_test\\ransomware\\random_files"

wanted = ['docx', 'txt', 'pdf', 'jpg']


def distribute(new_path):
	print("Creating files for", new_path)

	file_stubs = "document,my,story,song,listing,information,download,doc,today,untitled,unnamed,research,homework,info,doc,letter,email,info".split(
		",")

	for ftype in wanted:

		this_path = path

		if ftype == "jpg":

			sub = choice('IMG,images,pics,photo,pictures,image_folder'.split(","))
			new_path += f"\\{sub}"

			if os.path.exists(new_path) == False:
				os.mkdir(new_path)

			file_stubs = "pic,img,IMG,this,photo,graphic,gfx,pic,download".split(",")

		files = [f for f in os.listdir(path) if f.endswith(ftype)]

		needed = randint(2, int(len(files) * 0.4))

		files = sample(files, needed)

		for fn in files:

			new_fn = choice(file_stubs)

			x = randint(0, 3)
			if x == 0:
				new_fn = new_fn.upper()
			elif x == 1:
				new_fn = new_fn
			else:
				new_fn = new_fn.title()

			x = randint(0, 3)
			if x > 0:
				if randint(0, 2) == 0:
					num = randint(1, 999)
				else:
					num = randint(1, 99)

				num = str(num)

				if randint(0, 3) == 0:
					num = num.ljust(randint(1, 5), choice("A0_1-"))

				if randint(0, 1):
					num = choice("_- ") + num

			else:
				num = ""

			new_fn = new_fn + num + "." + ftype.upper()

			print("will copy", path + "\\" + fn, "to", new_path + "\\" + new_fn)
			copy(path + "\\" + fn, new_path + "\\" + new_fn)


## distribute files to sandbox network drives
for num in range(1, 23):
	distribute(f"Q:\\Exam\\y8student{num}")
