from kivymd.app import MDApp
from kivy.lang import Builder 
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.uix.behaviors import  FakeRectangularElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout
#from String.py import mainStr

mainStr = """
<Home@Screen>
<Login@Screen>
<Picture@Screen>
<Code@Screen>
ScreenManager:
	id:sm_manager
	Home:
	Login:
	Code:
	Picture:
		
#	Login:
#		name:"loginPage"
#		MDFloatLayout:
#			md_bg_color:(1,1,1,1)
#			padding:"20dp"
#			MDCard:
#				name:"loginBg"
#				size_hint:None,None
#				height:"760dp"
#				width:"420dp"
#				md_bg_color:0,.3,.5,.8
#				pos_hint:{"center_x":.5,"center_y":.5}
#				padding:"20dp"
#				MDFloatLayout:
#					size:self.size
#					pos_hint:{"center_x":.5,"center_y":.5}
#					MDLabel:
#						name:"loginH1"
#						text:"Login to your Dreams"
#						font_name:"Ubuntu-Bold"
#						font_size:"40sp"
#						color:(1,1,1,1)
#						pos_hint:{"center_x":.5,"center_y":.85}
#					MDFloatLayout:
#						size_hint: 1, .06
#						pos_hint:{"center_x":.5,"center_y":.65}
#						canvas:
#							Color:
#								rgb:(1,1,1,1)
#							RoundedRectangle:
#								size:self.size
#								pos:self.pos
#								radius:[6]
#						canvas.before:
#							Color:
#								rgb:230/255,230/255,230/255,1
#							Line:
#								width:2
#								rounded_rectangle: self.x,self.y,self.width,self.height,6,6,6,6,100
#						TextInput:
#							id:USERNAME
#							hint_text:"username"
#							hint_text_color:170/255,170/255,170/255,1
#							font_name:"Ubuntu/Ubuntu-Bold"
#							background_color:1,1,1,0
#							size_hint:1,None
#							height:self.minimum_height
#							cursor_color:0,0,0,1
#							padding:13
#							pos_hint:{"center_x":.5,"center_y":.5}
#					MDFloatLayout:
#						size_hint: 1, .06
#						pos_hint:{"center_x":.5,"center_y":.55}
#						canvas:
#							Color:
#								rgb:(1,1,1,1)
#							RoundedRectangle:
#								size:self.size
#								pos:self.pos
#								radius:[6]
#						canvas.before:
#							Color:
#								rgb:230/255,230/255,230/255,1
#							Line:
#								width:2
#								rounded_rectangle: self.x,self.y,self.width,self.height,6,6,6,6,100
#						TextInput:
#							id:USERPASS
#							hint_text:"password"
#							hint_text_color:170/255,170/255,170/255,1
#							font_name:"Ubuntu/Ubuntu-Bold"
#							background_color:1,1,1,0
#							size_hint:1,None
#							height:self.minimum_height
#							cursor_color:0,0,0,1
#							padding:13
#							pos_hint:{"center_x":.5,"center_y":.5}
#					Button:
#						id:logInBtn
#						text:"login"
#						font_name:"Ubuntu/Ubuntu-Bold"
#						size_hint: 1, .06
#						pos_hint:{"center_x":.5,"center_y":.45}
#						color:0,0,0,1
#						background_color:.1,1,1,0
#						on_release:
#							app.login(USERNAME,USERPASS)
#						canvas.before:
#							Color:
#								rgb:255/255,255/255,255/255,1
#							RoundedRectangle:
#								size:self.size
#								pos:self.pos
<Home>:
	name:"home"
	MDFloatLayout:
	#orientation:"vertical"
		size:1,1
		md_bg_color:0,.3,.5,.8
		ProfileCard:
			size_hint_y:.65
			pos_hint:{"center_y":.7}
			md_bg_color:.9,.9,.9,1
			elevation:10
			radius:[0,0,80,80]
			MDIconButton:
				icon:"arrow-left"
				pos_hint:{"center_y":.90}
				user_font_size:"20sp"
				theme_text_color:"Custom"
				text_color:0,.3,.5,.8
			MDIconButton:
				icon:"dots-vertical"
				pos_hint:{"center_x":.90,"center_y":.90}
				user_font_size:"20sp"
				theme_text_color:"Custom"
				text_color:0,.3,.5,.8
			MDLabel:
				text:"My Profile"
				halign:"center"
				font_name:"Ubuntu/Ubuntu-Bold"
				font_size:"25sp"
				pos_hint:{"center_y":.80,"center_x":.25}
			MDLabel:
				id:homelabel
				text:"welcome"
				halign:"center"
				font_name:"Ubuntu/Ubuntu-Medium"
				font_size:"28sp"
				color:0,.3,.5,1
				pos_hint:{"center_y":.36,"center_x":.5}
			MDLabel:
				id:profilelabel
				text:"Student (PCM + CS)"
				halign:"center"
				font_name:"Ubuntu/Ubuntu-Light"
				font_size:"20sp"
				color:0,.3,.5,.6
				pos_hint:{"center_y":.30,"center_x":.5}
			Image:
				source:"Logo.jpg"
				size_hint:None,None
				height:"150dp"
				width:"150dp"
				pos_hint:{"center_y":.55,"center_x":.5}
				canvas.before:
					Color:
						rgb:235/255,235/255,235/255,1
					RoundedRectangle:
						size:self.size
						pos:self.pos
			MDIconButton:
				icon:"home"
				pos_hint:{"center_y":.050,"center_x":.2}
				user_font_size:"25sp"
				theme_text_color:"Custom"
				text_color:0,.3,.5,.6
			MDIconButton:
				icon:"image-outline"
				pos_hint:{"center_y":.050,"center_x":.5}
				user_font_size:"25sp"
				theme_text_color:"Custom"
				text_color:0,.3,.5,.6
				on_press:
					root.manager.current = "Picture"
			MDIconButton:
				icon:"codepen"
				pos_hint:{"center_y":.050,"center_x":.8}
				user_font_size:"25sp"
				theme_text_color:"Custom"
				text_color:0,.3,.5,.6									
<Picture>:
	name:"Picture"
	MDFloatLayout:
	#orientation:"vertical"
		size:1,1
		md_bg_color:0,.3,.5,.8
		ProfileCard:
			size_hint_y:.65
			pos_hint:{"center_y":.7}
			md_bg_color:.9,.9,.9,1
			elevation:10
			radius:[0,0,80,80]
			MDIconButton:
				icon:"arrow-left"
				pos_hint:{"center_y":.90}
				user_font_size:"20sp"
				theme_text_color:"Custom"
				text_color:0,.3,.5,.8
				hint_animation: False
				on_press:
					root.manager.current = "home"
					
			MDIconButton:
				icon:"dots-vertical"
				pos_hint:{"center_x":.90,"center_y":.90}
				user_font_size:"20sp"
				theme_text_color:"Custom"
				text_color:0,.3,.5,.8
"""
class ProfileCard(MDFloatLayout, FakeRectangularElevationBehavior):
	pass
"""class Home(Screen):
	pass
class Login(Screen):
	pass	"""
	
class App(MDApp):
	def build(self):
		main = Builder.load_string(mainStr)
		return main	
	def login(self, username,password):
		print(username.text,"\n",password.text)
		user = ["harshit","12345","crown","crown@1"]
		if username.text in user and password.text in user:
			self.root.current = "home"
			self.root.ids.homelabel.text = username.text
if __name__ == "__main__":
	App().run()