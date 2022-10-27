from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions
import time
import random

# Login Credentials
username = 'OfficialMicroEffect@gmail.com'
username = 'EffectMicro'
password = 'Myxbox360'
url = 'https://twitter.com/login'
user = 'tohar_daniell'

MessageToBeSent = "אהלן, קוראים לי רועי גרבר ואני חייל משוחרר בן 23. כתבתי ספר היסטוריה מצחיק ומעניין במהלך השירות ואשמח אם תעזור לי לפרסם אותו:) אני אשמח לשלוח לך את הספר וגם לשלם 250 שקל על ציוץ מפרגן. נשמע טוב?"
MessageToBeSent = MessageToBeSent +'\n'+ 'https://www.roigerber.co.il'
MessageToBeSent = MessageToBeSent.split(" ")

PeopleWhoGetMessages = "Elinorigby@ArielaGoesFake@DorDugy@noamginger@Ssoya_abulafia@SonicScrw@TheMisterKhan@DanaGat1@galchs@LinorDeutsch@CatRobotIL@YaelSherer@dorosenblum@MadaGadol@midaat@nitayp@PonyPrincipessa@Noa_Liberator@Avinoam_Y@smallweed@gilibugg@skoopit@Eli_Barbel@MeytalinkaVan@DysonProgram@lo_greisas@YiftachDayan@Elinorigby@ArielaGoesFake@DorDugy@noamginger@Ssoya_abulafia@SonicScrw@TheMisterKhan@DanaGat1@galchs@LinorDeutsch@CatRobotIL@YaelSherer@dorosenblum@MadaGadol@midaat@TogetherKulan@nitayp@PonyPrincipessa@Noa_Liberator@Avinoam_Y@smallweed@gilibugg@skoopit@Eli_Barbel@MeytalinkaVan@DysonProgram@lo_greisas@YiftachDayan@Elinorigby@ArielaGoesFake@DorDugy@noamginger@skoopit@Eli_Barbel@DysonProgram@lo_greisas@YiftachDayan@Elinorigby@ArielaGoesFake@DorDugy@noamginger@Ssoya_abulafia@SonicScrw@TheMisterKhan@DanaGat1@galchs@LinorDeutsch@CatRobotIL@YaelSherer@dorosenblum@MadaGadol@midaat@TogetherKulan@nitayp@PonyPrincipessa@Noa_Liberator@Avinoam_Y"
PeopleWhoGetMessages = PeopleWhoGetMessages.split("@")
def path():
	global chrome
	
	# starts a new chrome session
	chrome = webdriver.Chrome() # Add path if required


def url_name(url):
	chrome.get(url)

	# adjust sleep if you want
	time.sleep(4)


def login(username, your_password):
#	log_but = chrome.find_element_by_class_name("L3NKy")
#	time.sleep(2)
#	log_but.click()
#	time.sleep(4)
#	
	# finds the username box
	############for i in range(1):
	usern = chrome.find_element_by_class_name("r-30o5oe.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-t60dpp.r-1dz5y72.r-fdjqy7.r-13qz1uu")	
	# sends the entered username
	for letter in username:
		usern.send_keys(letter)
		time.sleep(0.1)
	

	# finds the password box
	passw = chrome.find_element_by_name("session[password]")
	for letter in your_password:
		passw.send_keys(letter)
		time.sleep(0.1)
	
	passw.send_keys(Keys.RETURN)
	time.sleep(5.5)
	# Finding Not Now button
	#notk = chrome.find_element_by_name("Not Now")
	#notk.click()
	#time.sleep(3)

def Go_To_Messages():
	# Find message button
	message = chrome.find_element_by_class_name('css-1dbjc4n.r-1awozwy.r-sdzlij.r-18u37iz.r-1777fci.r-dnmrzs.r-xyw6el.r-o7ynqc.r-6416eg')
	print("a")
	message.click()
	time.sleep(1.2)

def Send_Message(ContactList):
	global User
	global MessageToBeSent
	for User in ContactList:
		url_name('https://twitter.com/messages/compose')
		UserField = chrome.find_element_by_class_name('r-30o5oe.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-xyw6el.r-y0fyvk.r-1dz5y72.r-fdjqy7.r-13qz1uu')
		print("a")
		UserField.send_keys(User)
		time.sleep(1)
		try:
			ChooseUser = chrome.find_element_by_class_name('css-1dbjc4n.r-1awozwy.r-18u37iz.r-1wtj0ep')
			ChooseUser.click()
			time.sleep(1)
			NextButton = chrome.find_element_by_class_name('css-18t94o4.css-1dbjc4n.r-urgr8i.r-42olwf.r-sdzlij.r-1phboty.r-rs99b7.r-19u6a5r.r-15ysp7h.r-4wgw6l.r-1ny4l3l.r-1fneopy.r-o7ynqc.r-6416eg.r-lrvibr')
			NextButton.click()
			time.sleep(2)
			print("\n\n\nPRESSED NEXT\n\n\n")
			TextArea = chrome.find_element_by_class_name('public-DraftStyleDefault-block.public-DraftStyleDefault-ltr')
			for word in MessageToBeSent:
				TextArea.send_keys(word+' ')
				TimeToBeWaited = 0.1
				time.sleep(TimeToBeWaited)
			time.sleep(1)
			TextArea.send_keys(Keys.RETURN)
			time.sleep(1)
		except:
			print("\n\n\nEXCEPTED\n\n\n")
			pass


path()
time.sleep(1)
print("A")
url_name(url)
print("B")
login(username, password)
#print("C")
#url_name(url+user)
print("D")
Send_Message(PeopleWhoGetMessages)
print("E")

chrome.close()
