from django.urls import path
from .views import ticketDetails, comment, ticketUpdate
urlpatterns =[
    path('<int:id>',ticketDetails, name="ticketDetails"),
    path('<int:ticket_id>/comment', comment),
    path('<int:id>/update', ticketUpdate)
]