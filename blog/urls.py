from django.urls import path
from .views import *


urlpatterns=[
  path('',index ,name="index"),
  path('about/',about ,name="about"),
  path('team/',team ,name="team"),
  path('booking/',booking ,name="booking"),
  path('404/',a404 ,name="404"),
  path('contact/',contact ,name="contact"),
  path('service/',service ,name="service"),
  path('testimonial/',testimonial ,name="testimonial"),
  path('package/',package ,name="package"),
  path('destination/',destination ,name="destination"),
  path("about/<int:id>", aboutdetailview, name='aboutDetail'),
  path("lenov/<int:id>", lenovdetailview, name='lenovDetail'),
  path("shadow/<int:id>", shadowdetailview, name='shadowDetail'),
  path('add-comment/<int:shadow_id>/', add_comment, name='add_comment'),
  path('search/',search_view,name='search')
]