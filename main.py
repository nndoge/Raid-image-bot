import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor


def write_attachment(peer_id, attachment):
	vk.method("messages.send", {"user_id": user_id, "attachment": attachment})

count = 0
id_group =  169224066
token_group = "1119aadf4f950a3632c3a1512d2c5ad44f356152c2a577c3f08ce6090c27c40fb3b288fe83bd4362e10c0"
vk_session = vk_api.VkApi(token=token_group) #токен вашей группы
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, 169224066) #цифровой id вашей группы
def main():

	keyboard1 = VkKeyboard(one_time=False) # False - клавиатура после нажатия не будет закрываться. True - будет.

	keyboard1.add_button('HhH vto.pe', color=VkKeyboardColor.POSITIVE)	
	
	keyboard1.add_button('DdD vto.pe', color=VkKeyboardColor.POSITIVE)
	
	keyboard1.add_button('WwW vto.pe', color=VkKeyboardColor.POSITIVE)
	
	keyboard1.add_button('WwW vto.pe', color=VkKeyboardColor.POSITIVE)
	keyboard1.add_line() 
	keyboard1.add_button('HhH vto.pe', color=VkKeyboardColor.POSITIVE)	
	
	keyboard1.add_button('DdD vto.pe', color=VkKeyboardColor.POSITIVE)
	
	keyboard1.add_button('WwW vto.pe', color=VkKeyboardColor.POSITIVE)
	
	keyboard1.add_button('WwW vto.pe', color=VkKeyboardColor.POSITIVE)
	keyboard1.add_line() 
	keyboard1.add_button('HhH vto.pe', color=VkKeyboardColor.NEGATIVE)	
	
	keyboard1.add_button('DdD vto.pe', color=VkKeyboardColor.NEGATIVE)
	
	keyboard1.add_button('WwW vto.pe', color=VkKeyboardColor.NEGATIVE)
	
	keyboard1.add_button('WwW vto.pe', color=VkKeyboardColor.NEGATIVE)			
	print("yes")
	while True: 
		try: 
			for event in longpoll.listen():

				if event.type == VkBotEventType.MESSAGE_NEW:
					print("успешно")
					while 1 > 0:
						vk.messages.send(peer_id=event.object.peer_id, message="GG",keyboard=keyboard1.get_keyboard(), random_id=0, attachment="photo441986030_457246812")
					
			
		except Exception as e:
			print('') 

if __name__ == '__main__':
	main()
