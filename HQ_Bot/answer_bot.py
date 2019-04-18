'''

	TODO:
	* Implement normalize func
	* Attempt to google wiki \"...\" part of question
	* Rid of common appearances in 3 options
	* Automate screenshot process
	* Implement Asynchio for concurrency

	//Script is in working condition at all times
	//TODO is for improving accuracy

'''

# to ba able to import from parent dir
import sys

parent_dir_path = ''
parent_dir_path_list = sys.path[0].split('\\')[0:-1]

for dir in parent_dir_path_list:
	parent_dir_path += dir + '\\'
	
parent_dir_path = parent_dir_path[0:-1]

sys.path.append(parent_dir_path)


# answering bot for trivia HQ and Cash Show
#need to clean these up !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
import json
import urllib.request as urllib2
from bs4 import BeautifulSoup
import google
from PIL import Image
import pytesseract
import argparse
import cv2
import os
import pyscreenshot as Imagegrab
import sys
import wx
from halo import Halo


import time


import search_utils
import utils
import colors # need?????????????????????????????????????????????????????????
from project_utils import extract_text # from parent dir


# for terminal colors 
class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

# sample questions from previous games
sample_questions = {}

# list of words to clean from the question during google search
remove_words = []

# negative words
negative_words= []

# GUI interface 
def gui_interface():
	app = wx.App()
	frame = wx.Frame(None, -1, 'win.py')
	frame.SetDimensions(0,0,640,480)
	frame.Show()
	app.MainLoop()
	return None

# load sample questions
def load_json():
	global remove_words, sample_questions, negative_words
	remove_words = json.loads(open("Data/settings.json").read())["remove_words"]
	negative_words = json.loads(open("Data/settings.json").read())["negative_words"]
	sample_questions = json.loads(open("Data/questions.json").read())

# take screenshot of question 
def screen_grab(to_save):
	# 31,228 485,620 co-ords of screenshot// left 50side of screen
	im = Imagegrab.grab(bbox=(31,228,455,710)) #im = Imagegrab.grab(bbox=(31,228,485,640))
	im.save(to_save)
# 	ssssssssssssssssssssssssssssssssssssssssssss


def grab_screen(screenshot_cords, save_path):
	im = Imagegrab.grab(bbox=screenshot_cords) #im = Imagegrab.grab(bbox=(31,228,485,640))
	im.save(save_path)


def extract_text_from_image(img_path):
	#prepare argparse
	ap = argparse.ArgumentParser(description='HQ_Bot')
	ap.add_argument("-i", "--image", required=False,default=img_path,help="path to input image to be OCR'd")
	ap.add_argument("-p", "--preprocess", type=str, default="thresh", help="type of preprocessing to be done")
	args = vars(ap.parse_args())

	# load the image 
	image = cv2.imread(args["image"])
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	if args["preprocess"] == "thresh":
		gray = cv2.threshold(gray, 0, 255,
			cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
	elif args["preprocess"] == "blur":
		gray = cv2.medianBlur(gray, 3)

	# store grayscale image as a temp file to apply OCR
	filename = "Screens/{}.png".format(os.getpid())
	cv2.imwrite(filename, gray)

	# load the image as a PIL/Pillow image, apply OCR, and then delete the temporary file
	text = pytesseract.image_to_string(Image.open(filename))#, lang = 'Circular')
	return text




QUESTION_SC_COORDS = (31,228,455,710)
OPTION_1_SC_COORDS = (31,228,455,710)
OPTION_2_SC_COORDS = (31,228,455,710)
OPTION_3_SC_COORDS = (31,228,455,710)

QUESTION_IMG_PATH = 'question_temp.jpg'
OPTION_1_IMG_PATH = 'option_1_temp.jpg'
OPTION_2_IMG_PATH = 'option_2_temp.jpg'
OPTION_3_IMG_PATH = 'option_3_temp.jpg'


def read_questions_and_options_from_screen():
	qo_dict = {'question': '',
				'options': []}
	
	grab_screen(QUESTION_SC_COORDS, QUESTION_IMG_PATH)
	grab_screen(OPTION_1_SC_COORDS, OPTION_1_IMG_PATH)
	grab_screen(OPTION_2_SC_COORDS, OPTION_2_IMG_PATH)
	grab_screen(OPTION_3_SC_COORDS, OPTION_3_IMG_PATH)



# get OCR text //questions and options
def read_screen():
	print("\033[1;33;40m  reading screen...")
# 	spinner = Halo(text='Reading screen', spinner='bouncingBar')
# 	spinner.start()
	screenshot_file="Screens/to_ocr.png"
	screen_grab(screenshot_file)
#
	#prepare argparse
	ap = argparse.ArgumentParser(description='HQ_Bot')
	ap.add_argument("-i", "--image", required=False,default=screenshot_file,help="path to input image to be OCR'd")
	ap.add_argument("-p", "--preprocess", type=str, default="thresh", help="type of preprocessing to be done")
	args = vars(ap.parse_args())

	# load the image 
	image = cv2.imread(args["image"])
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	if args["preprocess"] == "thresh":
		gray = cv2.threshold(gray, 0, 255,
			cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
	elif args["preprocess"] == "blur":
		gray = cv2.medianBlur(gray, 3)

	# store grayscale image as a temp file to apply OCR
	filename = "Screens/{}.png".format(os.getpid())
	cv2.imwrite(filename, gray)

	# load the image as a PIL/Pillow image, apply OCR, and then delete the temporary file
	text = pytesseract.image_to_string(Image.open(filename))#, lang = 'Circular')
	os.remove(filename)
	os.remove(screenshot_file)
	
	# show the output images

# 	cv2.imshow("Image", image)
# 	cv2.imshow("Output", gray)
# 	os.remove(screenshot_file)
# 	if cv2.waitKey(0):
# 		cv2.destroyAllWindows()
# 	print(text)
	
# 	spinner.succeed()
# 	spinner.stop()
	return text

# get questions and options from OCR text
def parse_question():
	text = read_screen()
	lines = text.splitlines()
	question = ""
	options = list()
	flag=False

	for line in lines :
		if not flag :
			question=question+" "+line
		
		if '?' in line :
			flag=True
			continue
		
		if flag :
			if line != '' :
				options.append(line)
			
	return question, options

# simplify question and remove which,what....etc //question is string
def simplify_ques(question):
	neg=False
	qwords = question.lower().split()
	if [i for i in qwords if i in negative_words]:
		neg=True
	cleanwords = [word for word in qwords if word.lower() not in remove_words]
	temp = ' '.join(cleanwords)
	clean_question=""
	#remove ?
	for ch in temp: 
		if ch!="?" or ch!="\"" or ch!="\'":
			clean_question=clean_question+ch

	return clean_question.lower(),neg


# get web page
def get_page(link):
	try:
		if link.find('mailto') != -1:
			return ''
		req = urllib2.Request(link, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'})
		html = urllib2.urlopen(req).read()
		return html
	except (urllib2.URLError, urllib2.HTTPError, ValueError) as e:
		return ''

# split the string
def split_string(source):
	splitlist = ",!-.;/?@ #"
	output = []
	atsplit = True
	for char in source:
		if char in splitlist:
			atsplit = True
		else:
			if atsplit:
				output.append(char)
				atsplit = False
			else:
				output[-1] = output[-1] + char
	return output

# normalize points // get rid of common appearances // "quote" wiki option + ques
def normalize():
	return None	

# take screen shot of screen every 2 seconds and check for question
def check_screen():
	return None

# wait for certain milli seconds 
def wait(msec):
	return None

# answer by combining two words
def smart_answer(content,qwords):
	zipped= zip(qwords,qwords[1:])
	points=0
	for el in zipped :
		if content.count(el[0]+" "+el[1])!=0 :
			points+=1000
	return points

# use google to get wiki page
def google_wiki(sim_ques, options, neg):
	spinner = Halo(text='Googling and searching Wikipedia', spinner='dots2')
	spinner.start()
	num_pages = 1
	points = list()
	content = ""
	maxo=""
	maxp=-sys.maxsize
	words = split_string(sim_ques)
	for o in options:
		
		o = o.lower()
		original=o
		o += ' wiki'

		# get google search results for option + 'wiki'
		search_wiki = google.search(o, num_pages)

		link = search_wiki[0].link
		content = get_page(link)
		soup = BeautifulSoup(content,"lxml")
		page = soup.get_text().lower()

		temp=0

		for word in words:
			temp = temp + page.count(word)
		temp+=smart_answer(page, words)
		if neg:
			temp*=-1
		points.append(temp)
		if temp>maxp:
			maxp=temp
			maxo=original
	spinner.succeed()
	spinner.stop()
	return points,maxo


# return points for sample_questions
def get_points_sample():
	simq = ""
	x = 0
	for key in sample_questions:
		x = x + 1
		points = []
		simq,neg = simplify_ques(key)
		options = sample_questions[key]
		simq = simq.lower()
		maxo=""
		points, maxo = google_wiki(simq, options,neg)
		print("\n" + str(x) + ". " + bcolors.UNDERLINE + key + bcolors.ENDC + "\n")
		for point, option in zip(points, options):
			if maxo == option.lower():
				option=bcolors.OKGREEN+option+bcolors.ENDC
			print(option + " { points: " + bcolors.BOLD + str(point) + bcolors.ENDC + " }\n")


def get_question_and_options():
	neg= False
	question,options=parse_question()
	simq = ""
	points = []
	simq, neg = simplify_ques(question)
	maxo=""
	m=1 
	if neg:
		m=-1
		
# 	for letter in simq:#`````````````````````````````````````````````````````````````````````````````
# 		print(letter)
			
# 	print('simq: ', simq)#``````````````````````````````````````````````````````````````````````````
	return simq, options

# return points for live game // by screenshot
def get_points_live():
	neg= False
	question,options=parse_question()
# 	print('question: ', question)
# 	print('options : ', options)
	simq = ""
	points = []
	simq, neg = simplify_ques(question)
	maxo=""
	m=1 
	if neg:
		m=-1

	points,maxo = google_wiki(simq, options, neg)
	
	print("\n" + bcolors.UNDERLINE + question + bcolors.ENDC + "\n")
	for point, option in zip(points, options):
		if maxo == option.lower():
			option=bcolors.OKGREEN+option+bcolors.ENDC
		print(option + " { points: " + bcolors.BOLD + str(point*m) + bcolors.ENDC + " }\n")


def valid_read(question, options):
	if (question == '' or len(options) == 0):
		return False
	return True







def main():
	times = []
	print ('')
	print ('')
	print ('')
	print ('')
	
	while(1):
# 		print("\033[1;33;40m reading screen tttttttttttttest...")
		print('')
		print('')
		keypressed = input(colors.ORANGE + 'Press q to quit, Press anything else to read screen:' + colors.ENDC)
		print('')
		print('')
		start = time.time()
		
		if keypressed == 'q':
			print("QUIT")
			print('average time: ', utils.avg_time(times))
			exit()
		else:
			try:
				question = ''
# 				question, options = get_question_and_options()
				qo_d = extract_text.read_questions_and_options_from_screen()
				question = qo_d['question']
				options = [qo_d['option_1'], qo_d['option_2'], qo_d['option_3']]

# 				start_t = time.time()#```````````````````````````````````````````

				utils.print_question_and_options(question, options)
				print('')
				search_utils.chrome_search(options + [question])
				
				if valid_read(question, options):
# 					end_t = time.time()#`````````````````````````````````````````````````````
# 					print(end_t - start_t)#``````````````````````````````````````````````````````````````
					search_utils.show_relation_stats(question, options)
					pass
				else:
					try_count = 0
					while(try_count < 3 and not valid_read(question, options)):
						try_count += 1
						print('BAD READ, TRYING AGAIN...')
						question, options = get_question_and_options()
			except:
				print (colors.BRIGHT_RED + "FAIL! TRY AGAIN")
				
				
				
			end = time.time()
			print('time: ', end - start)
			times.append(end - start)





#stuff to look at
#quotes
#weird symbols

# menu// main func
if __name__ == "__main__":
	main()
# 	screen_grab('temp.png')
# 	print ('done')
