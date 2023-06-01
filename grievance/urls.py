from django.urls import path
from .views import ticketDetails, comment, ticketStatus
urlpatterns =[
    path('<int:id>',ticketDetails, name="ticketDetails"),
    path('<int:ticket_id>/comment', comment),
    path('<int:ticket_id>/status/<int:value>', ticketStatus)
]