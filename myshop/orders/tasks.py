from celery import shared_task
from django.core.mail import send_mail
from .models import Order


@shared_task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    order_email = order['email']
    subject = f'Order nr. {order_id}'
    message = f'Dear {order.first_name},\n\n You have successfully placed an order. Your order ID is {order_id}.'
    mail_sent = send_mail(subject=subject, message=message, from_email='i-baykov@internet.ru',
                          recipient_list=[order.email])
    return mail_sent
