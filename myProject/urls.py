"""
URL configuration for myProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


# from django.contrib import admin
# from django.urls import path
# from django.conf import settings
# from django.conf.urls.static import static
# from myProject import views 


from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myProject.views import *
from myProject.myAdminviews import *
from myProject.studentviews import *
from myProject.teacherviews import *
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signinPage/', signinPage, name='signinPage'),
    path('signupPage/', signupPage, name='signupPage'),
    path('logoutPage/', logoutPage, name='logoutPage'),
    
    
    
    #------Admin Route-----------
    path('adminDashboard/', adminDashboard, name='adminDashboard'),
    path('teacherdashboard/', teacherdashboard, name='teacherdashboard'),
    path('studentdashboard/', studentdashboard, name='studentdashboard'),
    
    
    #------Admin Teacher Route-----------
    path('teacherlist/', teacherlist, name='teacherlist'),
    path('teacheradd/', teacheradd, name='teacheradd'),
    path('teacherview/', teacherview, name='teacherview'),
    path('teacheredit/', teacheredit, name='teacheredit'),
    
    
    
    #------Admin Student Route-----------
    path('studentlist/', studentlist, name='studentlist'),
    path('studentview/', studentview, name='studentview'),
    path('studentadd/', studentadd, name='studentadd'),
    path('studentedit/', studentedit, name='studentedit'),
    
    
    #------Admin Department Route-----------
    path('departmentlist/', departmentlist, name='departmentlist'),
    path('departmentadd/', departmentadd, name='departmentadd'),
    path('departmentview/', departmentview, name='departmentview'),
    
    
    #------Admin Subject Route-----------
    path('subjectlist/', subjectlist, name='subjectlist'),
    path('subjectadd/', subjectadd, name='subjectadd'),
    path('subjectedit/', subjectedit, name='subjectedit'),
    
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)