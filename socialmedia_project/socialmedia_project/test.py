from os import name
from django.http import request, response
from django.test import TestCase,Client
from post_app.models import Post
from profile_app.models import UserProfileInfo 
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse
from profile_app.forms import UserForm

class Testing(TestCase):
    #some setup were done
    def setUp(self):
        self.client =Client()
        self.testuser = User.objects.create_user(
            username ='testuser',email ="ron@gmail.com",password ='dragon455'
        )
        self.testuser2 = User.objects.create_user(
            username ='testuser2',email = "many@gmail.com",password ='dragon455'
        )
        user = User.objects.get(username = self.testuser )
     
        self.post_upload = Post.objects.create(
            description = 'django',
            post_image = 'def.jpg',
            author = user

        )
        self.profile_upload = UserProfileInfo.objects.create(
            profile_pic ='def.jpg',
            user = user,
            name ='hero'
        )
        self.login_url = reverse('account:user_login')
        self.register_url = reverse('account:register')

        self.user = {
            'username':'Nischal',
            'password':'dragon455'

        }
        self.user_profile = {
            'bio':'hello',
            'name':'nunu',
        }
      
#login was tested when postin data
    def test_login_in(self):
        response =self.client.post(self.login_url,self.user,format='text/html')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'login_register_app/login.html')

#followers count were tested when follower was added
    def test_profile_follow_count(self):
        self.profile_upload.followers.set([self.testuser.id,self.testuser2.id])
        self.assertEqual(self.profile_upload.followers.count(),2)

#many to many relation was tested when liked 
    def test_post_like_count(self):
        self.post_upload.likes.set([self.testuser.id,self.testuser2.id])
        self.assertEqual(self.post_upload.likes.count(),2)

#home page was tested 
    def test_homepage(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code,200)  
        self.assertTemplateUsed(response,'landing_page.html')


#login page was tested
    def test_login_access_page(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'login_register_app/login.html')
    
#register url was tested    
    def test_register_page(self):
        response = self.client.get( reverse('account:register'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'login_register_app/registration.html')
    

    

#form testing

    def test_invalid_form(self):
        w = User.objects.create(username='Foo', password='')
        data = {'username': w.username, 'password': w.password, }
        form = UserForm(data=data)
        self.assertFalse(form.is_valid())

    
  



    








